init:
	pip install -r requirements.txt

run:
	python app.py

test:
	python -m unittest test.py

# Nom de l'image Docker
IMAGE_NAME=health-calculator-service

# Nom du conteneur Docker
CONTAINER_NAME=health-calculator-container

# Port d'exposition du service
PORT=5000

# Commande pour construire l'image Docker
build:
	docker build -t $(IMAGE_NAME) .

# Commande pour exécuter le conteneur Docker
run:
	docker run --name $(CONTAINER_NAME) -p $(PORT):5000 $(IMAGE_NAME)

# Commande pour arrêter et supprimer le conteneur Docker
stop:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

# Commande pour exécuter les tests unitaires dans un environnement Docker
test:
	docker run --rm $(IMAGE_NAME) python3 -m unittest test.py

# Commande pour nettoyer les images Docker inutilisées
clean:
	docker system prune -f

# Commande pour déployer : build, test et run
deploy: build test run

# Commande pour supprimer l'image Docker
remove-image:
	docker rmi $(IMAGE_NAME)

# Commande pour exécuter l'application localement (hors Docker)
start:
	python3 app.py

