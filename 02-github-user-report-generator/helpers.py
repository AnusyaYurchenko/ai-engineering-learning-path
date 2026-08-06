import requests


def get_github_user(username):
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, timeout=10)
    except requests.RequestException:
        return None

    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            return None

    return None


def create_report(usernames, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
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
    test_usernames = ["github", "octocat", "fake-user-123456789"]
    create_report(test_usernames, "test_report.txt")
    print("Test report created.")
