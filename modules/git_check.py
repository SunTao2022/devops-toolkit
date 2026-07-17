from modules.shell_utils import run_command

def check_git_status():
    """
    检查当前 Git 仓库的状态：
    1. 是否有未提交的更改
    2. 最新一次提交的信息
    返回一段可读的文字描述。
    """
    # ① 运行 git status --short，查看是否有未提交的更改
    #    --short 参数输出精简格式：有变更的文件会列出来
    status = run_command(["git", "status", "--short"])
    
    # ② 运行 git log --oneline -1，查看最近一条提交
    #    --oneline 参数只显示 commit hash 和提交信息（一行）
    #    -1 参数只看最近一条
    log = run_command(["git", "log", "--oneline", "-1"])
    
    # ③ 判断并返回结果
    if status.startswith("错误"):
        return f"[Git] 当前目录不是 Git 仓库，或 Git 未安装"
    
    if status:
        return f"[Git] 有未提交的更改:\n{status}"
    else:
        return f"[Git] 工作区干净\n最新提交: {log}"
