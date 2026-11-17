"""Simple Git repository status check."""

from modules.shell_utils import run_command


def check_git_status() -> str:
    status = run_command(["git", "status", "--short"])
    if status.startswith("Error:"):
        return f"[Git] Could not read Git working tree: {status}"

    latest = run_command(["git", "log", "--oneline", "-1"])
    if latest.startswith("Error:"):
        return f"[Git] Could not read latest commit: {latest}"

    if status:
        return f"[Git] Uncommitted changes:\n{status}\nLatest commit: {latest}"
    return f"[Git] Working tree clean\nLatest commit: {latest}"
