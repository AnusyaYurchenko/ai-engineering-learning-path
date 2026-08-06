from helpers import create_report


usernames = ["github", "octocat", "AnusyaYurchenko", "fake-user-123456789"]
output_file = "github_users_report.txt"


def main():
    create_report(usernames, output_file)
    print(f"Report generated: {output_file}")


if __name__ == "__main__":
    main()
