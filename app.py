from flask import Flask, request, jsonify, render_template
from utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmi')
def bmi():
    data = request.get_json()
    height = data.get("height")
    weight = data.get("weight")
    if not height or not weight:
        return jsonify({"error": "La taille et le poids sont requis."}), 400
    bmi = calculate_bmi(height, weight)
    return jsonify({"bmi": round(bmi, 2)})

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.get_json()
    height = data.get("height")
    weight = data.get("weight")
    age = data.get("age")
    gender = data.get("gender")
    if not all([height, weight, age, gender]):
        return jsonify({"error": "La taille, le poids, l'âge et le sexe sont requis."}), 400
    bmr = calculate_bmr(height, weight, age, gender)
    return jsonify({"bmr": round(bmr, 2)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
