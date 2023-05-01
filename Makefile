.PHONEY: dev
dev:
	poetry run uvicorn openapi_server_sample.main:app --reload --port 8081

.PHONEY: generate
generate:
	poetry run python openapi_server_sample/generate.py > openapi.json

.PHONEY: lint
lint:
	black openapi_server_sample
