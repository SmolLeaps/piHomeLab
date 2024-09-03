import re

def parse_command(command):
    # Adjust the regex to be more flexible with spaces and punctuation
    create_repo_match = re.search(r"create repo '(.+?)'", command, re.I)
    run_code_match = re.search(r"run\s+the\s+c\s+code\s+in\s+'(.+?)'", command, re.I)

    # Debug prints to check the matches
    print(f"Create Repo Match: {create_repo_match}")
    print(f"Run Code Match: {run_code_match}")
    
    if create_repo_match:
        repo_name = create_repo_match.group(1)
        return {"action": "create_repo", "repo_name": repo_name}
    elif run_code_match:
        file_name = run_code_match.group(1)
        return {"action": "run_c_code", "file_name": file_name}
    else:
        return {"action": "unknown"}

command = input("Enter your command: ")
parsed_command = parse_command(command)
print(parsed_command)

