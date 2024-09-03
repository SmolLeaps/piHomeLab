import re

def parse_command(command):
    if re.search(r"create repo", command, re.I):
        repo_name = re.search(r"repo called '(.+?)'", command).group(1)
        return {"action": "create_repo", "repo_name": repo_name}
    elif re.search(r"run the C code", command, re.I):
        file_name = re.search(r"code in '(.+?)'", command).group(1)
        return {"action": "run_c_code", "file_name": file_name}
    return {"action": "unknown"}

command = input("Enter your command: ")
print(parse_command(command))

