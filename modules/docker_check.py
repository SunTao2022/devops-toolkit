from modules.shell_utils import run_command

def check_docker_ps():
    result = run_command(["docker" , "ps" , "--format" , "table{{.Names}}\t{{.Status}}\t{{.Port}}"])

    if result.startswith('Error'):
        return "[Docker] Docker 未安装或未启动"
    
    if result.count('\n') <= 1:
        return "[Docker] 没有运行中的容器"
    
    
    return f"[Docker] 运行中的容器:\n{result}"

