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