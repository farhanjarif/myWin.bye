import requests

def check_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"User '{username}' exists on GitHub.")
        print("User Info:", response.json())
    elif response.status_code == 404:
        print(f"User '{username}' does not exist.")
    else:
        print(f"An error occurred: {response.status_code}")
        print(response.json())

username = "myWin.bye"
check_github_user(username)
