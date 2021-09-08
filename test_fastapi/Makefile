.PHONY: init
init:
	docker-compose build

.PHONY: run
run:
	docker-compose run --rm --service-ports app

distribute: init
	docker push test_fastapi_app eu.gcr.io/ma-dev2/dev-images/test_fastapi_app:latest
