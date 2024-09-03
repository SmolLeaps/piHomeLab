import requests

def create_github_repo(repo_name, token):
    url = f"https://api.github.com/user/repos"
    headers = {"Authorization": f"token {token}"}
    data = {"name": repo_name}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print("Error:", response.json())

token = ""
repo_name = "example-repo"
create_github_repo(repo_name, token)

