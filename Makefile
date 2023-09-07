.PHONY: env
env:
	pants generate-lockfiles
	pants export --resolve=monorepo

.PHONY: check
check: 
	pants lint check ::

.PHONY: fmt
fmt:
	pants fmt ::
