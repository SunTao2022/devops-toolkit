"""Run lightweight local Git, Docker and Kubernetes checks."""

from modules.docker_check import check_docker_ps
from modules.git_check import check_git_status
from modules.k8s_check import check_k8s_nodes, check_k8s_pods


def run_all_checks() -> None:
    print("=== Infrastructure Diagnostics ===\n")
    for check in (
        check_git_status,
        check_docker_ps,
        check_k8s_nodes,
        check_k8s_pods,
    ):
        print(check(), end="\n\n")


if __name__ == "__main__":
    run_all_checks()
