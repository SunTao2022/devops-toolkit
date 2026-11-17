"""Small subprocess wrapper used by the diagnostics commands."""

import subprocess


def run_command(command: list[str]) -> str:
    try:
        result = subprocess.run(
            command, capture_output=True, text=True, timeout=10, check=False
        )
    except FileNotFoundError:
        return f"Error: command not found: {command[0]}"
    except subprocess.TimeoutExpired:
        return f"Error: command timed out: {command[0]}"

    if result.returncode != 0:
        message = result.stderr.strip() or f"exit code {result.returncode}"
        return f"Error: {message}"
    return result.stdout.strip()
