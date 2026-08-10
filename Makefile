.PHONY: env
env: generate-venv

.PHONY: regenerate-env
regenerate-env: generate-lockfiles generate-venv 

.PHONY: check
check: 
	pants lint check ::

.PHONY: fmt
fmt:
	pants fmt ::

.PHONY: generate-lockfiles
generate-lockfiles:
	pants generate-lockfiles
	
.PHONY: generate-venv
generate-venv:
	pants export --resolve=global --resolve=machine-learning --resolve=web

.PHONY: titanic-download-dataset
titanic-download-dataset:
	@ projects/machine-learning/titanic/scripts/get-dataset.sh

.PHONY: titanic-train
titanic-train:
	PYTHONPATH=projects/machine-learning/titanic python3 -m model.train

.PHONY: titanic-serve
titanic-serve:
	PYTHONPATH=projects/machine-learning/titanic python3 -m serving.main

.PHONY: web-serve
web-serve:
	uvicorn --app-dir projects/web main:app

.PHONY: update-pants-image
update-pants-image:
	@ docker buildx build \
		--push \
		-t mikaelsouza/pants:latest \
		-f dockerfiles/pants.Dockerfile \
		--platform linux/arm64 .