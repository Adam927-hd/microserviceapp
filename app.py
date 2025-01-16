from flask import Flask, request, jsonify, render_template
from utils import calculate_bmi, calculate_bmr
from http import HTTPStatus

app = Flask(__name__)

def validate_numeric_value(value, name, min_value=0):
    """
    Valide une valeur numérique.
    Retourne (value, error_message)
    """
    try:
        value = float(value)
        if value <= min_value:
            return None, f"Le {name} doit être supérieur à {min_value}."
        return value, None
    except (TypeError, ValueError):
        return None, f"Le {name} doit être un nombre valide."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmi', methods=['POST'])
def bmi():
    if not request.is_json:
        return jsonify({
            "error": "Le contenu doit être au format JSON"
        }), HTTPStatus.BAD_REQUEST

    data = request.get_json()
    
    # Vérification de la présence des champs requis
    required_fields = ['height', 'weight']
    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"Le champ '{field}' est requis"
            }), HTTPStatus.BAD_REQUEST

    # Validation de la taille
    height, height_error = validate_numeric_value(
        data.get("height"), "taille", min_value=0
    )
    if height_error:
        return jsonify({"error": height_error}), HTTPStatus.BAD_REQUEST

    # Validation du poids
    weight, weight_error = validate_numeric_value(
        data.get("weight"), "poids", min_value=0
    )
    if weight_error:
        return jsonify({"error": weight_error}), HTTPStatus.BAD_REQUEST

    try:
        bmi = calculate_bmi(height, weight)
        return jsonify({
            "bmi": round(bmi, 2),
            "status": "success"
        }), HTTPStatus.OK
    except Exception as e:
        return jsonify({
            "error": f"Erreur lors du calcul du BMI: {str(e)}"
        }), HTTPStatus.INTERNAL_SERVER_ERROR

@app.route('/bmr', methods=['POST'])
def bmr():
    if not request.is_json:
        return jsonify({
            "error": "Le contenu doit être au format JSON"
        }), HTTPStatus.BAD_REQUEST

    data = request.get_json()

    # Vérification de la présence des champs requis
    required_fields = ['height', 'weight', 'age', 'gender']
    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"Le champ '{field}' est requis"
            }), HTTPStatus.BAD_REQUEST

    # Validation de la taille
    height, height_error = validate_numeric_value(
        data.get("height"), "taille", min_value=0
    )
    if height_error:
        return jsonify({"error": height_error}), HTTPStatus.BAD_REQUEST

    # Validation du poids
    weight, weight_error = validate_numeric_value(
        data.get("weight"), "poids", min_value=0
    )
    if weight_error:
        return jsonify({"error": weight_error}), HTTPStatus.BAD_REQUEST

    # Validation de l'âge
    try:
        age = int(data.get("age"))
        if age <= 0 or age > 150:  # Limite d'âge raisonnable
            return jsonify({
                "error": "L'âge doit être compris entre 1 et 150 ans"
            }), HTTPStatus.BAD_REQUEST
    except (TypeError, ValueError):
        return jsonify({
            "error": "L'âge doit être un nombre entier valide"
        }), HTTPStatus.BAD_REQUEST

    # Validation du genre
    gender = data.get("gender", "").lower()
    if gender not in ['male', 'female']:
        return jsonify({
            "error": "Le genre doit être 'male' ou 'female'"
        }), HTTPStatus.BAD_REQUEST

    try:
        bmr = calculate_bmr(height, weight, age, gender)
        return jsonify({
            "bmr": round(bmr, 2),
            "status": "success"
        }), HTTPStatus.OK
    except Exception as e:
        return jsonify({
            "error": f"Erreur lors du calcul du BMR: {str(e)}"
        }), HTTPStatus.INTERNAL_SERVER_ERROR

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
