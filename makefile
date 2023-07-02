docker-up:
	docker compose up --build -d

docker-dev-up:
	docker compose -f=docker-compose.develop.yml up --build

docker-down:
	docker compose down