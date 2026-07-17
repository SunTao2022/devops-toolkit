import argparse
from modules.shell_utils import run_command
from modules.git_check import check_git_status
from modules.docker_check import check_docker_ps
from modules.k8s_check import check_k8s_nodes , check_k8s_pods

def run_all_checks():
    print("===Devops Toolkit Check report === \n")

    print(check_git_status())
    print()
    print(check_docker_ps())
    print()
    print(check_k8s_nodes())
    print()
    print(check_k8s_pods())
    print()


if __name__ == "__main__":
    run_all_checks()