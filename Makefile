.PHONY: env
env:
	if [ ! -f deps/lockfiles/monorepo.lock ]; then \
		pants generate-lockfiles; \
	fi
	pants export --resolve=monorepo

.PHONY: regenerate-env
regenerate-env:
	pants generate-lockfiles
	pants export --resolve=monorepo

.PHONY: check
check: 
	pants lint check ::

.PHONY: fmt
fmt:
	pants fmt ::
