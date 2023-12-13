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
	pants export ::

.PHONY: titanic-download-dataset
titanic-download-dataset:
	@ projects/titanic/scripts/get-dataset.sh

.PHONY: update-pants-image
update-pants-image:
	@ docker buildx build \
		--push \
		-t mikaelsouza/pants:latest \
		-f dockerfiles/pants.Dockerfile \
		--platform linux/amd64,linux/arm64 .