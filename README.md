# Python Infrastructure Diagnostics Toolkit

A small personal IT operations lab written in Python. It runs simple, **read-only** checks against a local Git repository, Docker engine, and Kubernetes context.

## Requirements

- Python 3.11 or later
- `git`, `docker`, and/or `kubectl` installed to run the corresponding checks
- `pytest` for unit tests

No real cloud connection or credentials are needed for the Python test suite.

## Run

```bash
python main.py
python -m pip install pytest
python -m pytest tests/ -v
```

Each check runs with a 10-second subprocess timeout and prints a readable error if the command is missing, fails, or times out.

## What it checks

| Check | CLI operation | Purpose |
| --- | --- | --- |
| Git | `git status --short`, `git log --oneline -1` | Working tree status and last commit |
| Docker | `docker ps --format ...` | Running container names, status, ports |
| Kubernetes nodes | `kubectl get nodes` | List/count visible nodes |
| Kubernetes pods | `kubectl get pods --all-namespaces` | List/count visible pods |

The toolkit uses your currently selected Docker endpoint and Kubernetes context. If an active context points to a real cluster, the commands still only **read** resources, but require appropriate credentials.

## Structure

```text
main.py
modules/
  shell_utils.py
  git_check.py
  docker_check.py
  k8s_check.py
tests/
  test_diagnostics.py
.github/workflows/
  ci.yml
  azure-sp-auth.yml
```

## CI

GitHub Actions runs the Python unit tests on pushes and pull requests. A separate, manually triggered workflow keeps the previous Azure service-principal connectivity experiment available without logging into Azure on every code push.

## Limitations

- The command output is meant for quick manual diagnostics, not comprehensive health checks.
- Output parsing assumes the default tabular `kubectl` response.
- This is a personal learning project, not an enterprise monitoring solution.

## Author

[Tao Sun](https://www.linkedin.com/in/tao-sun-3437462b6/)
