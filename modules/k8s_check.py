from modules.shell_utils import run_command

def check_k8s_nodes():
    result = run_command(["kubectl" , "get" , "nodes"])
    if result.startswith("Error"):
        return "[K8s] kubectl 未安装或集群未运行"
    
    lines = result.split('\n')

    if len(lines) <= 1:
        return "k8s no nodes"
    node_count = len(lines) - 1
    return f"[K8s] 集群正常，共 {node_count} 个节点:\n{result}"

def check_k8s_pods():
    result = run_command(["kubectl" , "get" , "pods" , "--all-namespaces"])

    if result.startswith("错误"):
        return f"pods check faild,cluter is not runing"
    
    lines = result.split('\n')
    if len(lines) <= 1:
        return "pod : did not find pod"
    
    pod_count = len(lines) - 1
    return f"pod total: {pod_count}"