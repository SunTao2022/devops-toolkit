"""Unit tests that do not require real Docker, Kubernetes, Git, or Azure."""

from types import SimpleNamespace

import modules.docker_check as docker_check
import modules.git_check as git_check
import modules.k8s_check as k8s_check
import modules.shell_utils as shell_utils


def test_git_status_clean(monkeypatch):
    def fake_run(args):
        if args[1] == "status":
            return ""
        return "abc123 first commit"

    monkeypatch.setattr(git_check, "run_command", fake_run)
    output = git_check.check_git_status()
    assert "Working tree clean" in output
    assert "abc123" in output


def test_git_status_error(monkeypatch):
    monkeypatch.setattr(
        git_check, "run_command", lambda args: "Error: not a git repository"
    )
    assert "Could not read" in git_check.check_git_status()


def test_docker_uses_ports_and_handles_no_containers(monkeypatch):
    commands = []

    def fake_run(args):
        commands.append(args)
        return "NAMES\tSTATUS\tPORTS"

    monkeypatch.setattr(docker_check, "run_command", fake_run)
    assert "No running containers" in docker_check.check_docker_ps()
    assert "{{.Ports}}" in commands[0][-1]


def test_docker_shows_running_container(monkeypatch):
    monkeypatch.setattr(
        docker_check,
        "run_command",
        lambda args: "NAMES\tSTATUS\tPORTS\nweb\tUp 1 hour\t8080->80/tcp",
    )
    assert "web" in docker_check.check_docker_ps()


def test_kubernetes_error_is_not_counted_as_pods(monkeypatch):
    monkeypatch.setattr(
        k8s_check, "run_command", lambda args: "Error: cluster unavailable"
    )
    assert "Unable to query pods" in k8s_check.check_k8s_pods()
    assert "Unable to query nodes" in k8s_check.check_k8s_nodes()


def test_kubernetes_counts_rows(monkeypatch):
    monkeypatch.setattr(
        k8s_check, "run_command", lambda args: "NAME\tSTATUS\npod-a\tRunning\npod-b\tRunning"
    )
    assert "2" in k8s_check.check_k8s_pods()


def test_run_command_failure_is_consistent(monkeypatch):
    def fake_run(*args, **kwargs):
        return SimpleNamespace(returncode=1, stdout="", stderr="permission denied")

    monkeypatch.setattr(shell_utils.subprocess, "run", fake_run)
    assert shell_utils.run_command(["kubectl", "get", "nodes"]) == "Error: permission denied"


def test_run_command_missing_binary(monkeypatch):
    def fake_run(*args, **kwargs):
        raise FileNotFoundError("executable missing")

    monkeypatch.setattr(shell_utils.subprocess, "run", fake_run)
    assert shell_utils.run_command(["kubectl"]).startswith("Error:")
