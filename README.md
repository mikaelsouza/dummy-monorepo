# Dummy Monorepo

This is a dummy Python monorepo managed with the **[Pants Build System](https://www.pantsbuild.org/)**. It demonstrates a structured approach to managing multiple related projects, shared libraries, and build/test pipelines within a single repository.

## Repository Structure

- `projects/`: Contains top-level executable projects and services.
  - `machine-learning/titanic/`: A complete machine learning workflow for the classic Titanic survival prediction task, including data exploration notebooks, training scripts, model serving code, and tests.
  - `web/`: Web services and applications.
- `libs/`: Contains shared utility libraries that can be imported across different projects.
  - `calculator/`: A shared library module providing basic operations.
- `scripts/`: Utility scripts for repository automation.
- `dockerfiles/`: Docker configurations for containerizing applications and build environments.

## Build System

This monorepo uses Pants to handle dependency management, linting, formatting, type checking, and testing across the codebase. Configuration can be found in `pants.toml`.

## Getting Started

A `Makefile` is provided to simplify common development tasks.

### Setting up the Environment

To generate virtual environments and lockfiles for local development:
```bash
make env
```

If you need to regenerate lockfiles and environments from scratch:
```bash
make regenerate-env
```

### Code Quality

Format all code using Pants:
```bash
make fmt
```

Run linting and type checks (MyPy, Black, etc.):
```bash
make check
```

### Additional Commands

Download the Titanic dataset for the machine learning project:
```bash
make titanic-download-dataset
```

## CI/CD

Continuous Integration is handled via [Woodpecker CI](https://woodpecker-ci.org/), configured in `.woodpecker.yaml`. On every push, the CI pipeline runs checks, linters, and tests across the monorepo, utilizing a remote Bazel-compatible cache to speed up builds.