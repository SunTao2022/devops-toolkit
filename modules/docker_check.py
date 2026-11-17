"""Docker container diagnostics."""

from modules.shell_utils import run_command


def check_docker_ps() -> str:
    result = run_command(
        ["docker", "ps", "--format", "table {{.Names}}\t{{.Status}}\t{{.Ports}}"]
    )
    if result.startswith("Error:"):
        return f"[Docker] Unable to list containers: {result}"

    lines = result.splitlines()
    if len(lines) <= 1:
        return "[Docker] No running containers"

    return f"[Docker] Running containers:\n{result}"
