import subprocess

def run_command(cmd_list):
    try:
        result = subprocess.run(cmd_list,capture_output=True , text=True , timeout= 10)
        if result.returncode == 0 :
            return result.stdout.strip()
        else:
            return f"Error: {result.stderr.strip()}"
    except FileNotFoundError:
        return f"Error , command {cmd_list[0]} did not install or not in the path"
    except subprocess.TimeoutExpired:
        return "Error : command excute timeout"