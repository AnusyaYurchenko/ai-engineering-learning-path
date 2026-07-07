import requests


def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def create_report(usernames, output_file):
    with open(output_file, "w") as file:
        file.write("GitHub Users Report\n\n")
        for username in usernames:
            user_data = get_github_user(username)

            if user_data:
                file.write(f"Username: {user_data['login']}\n")
                file.write(f"Public repos: {user_data['public_repos']}\n")
                file.write(f"Profile URL: {user_data['html_url']}\n")
                file.write("\n")
            else:
                file.write(f"Could not get data for {username}.\n")


if __name__ == "__main__":
    usernames = ["github", "octocat", "fake-user-123456789"]
    output_file = "test_report.txt"

    print(get_github_user("github"))
    create_report(usernames, output_file)
    print("Test report created.")
