"""Kubernetes cluster diagnostics."""

from modules.shell_utils import run_command


def check_k8s_nodes() -> str:
    result = run_command(["kubectl", "get", "nodes"])
    if result.startswith("Error:"):
        return f"[Kubernetes] Unable to query nodes: {result}"

    node_count = max(0, len(result.splitlines()) - 1)
    if not node_count:
        return "[Kubernetes] No nodes found"
    return f"[Kubernetes] {node_count} nodes:\n{result}"


def check_k8s_pods() -> str:
    result = run_command(["kubectl", "get", "pods", "--all-namespaces"])
    if result.startswith("Error:"):
        return f"[Kubernetes] Unable to query pods: {result}"

    pod_count = max(0, len(result.splitlines()) - 1)
    if not pod_count:
        return "[Kubernetes] No pods found"
    return f"[Kubernetes] Total pods across namespaces: {pod_count}"
