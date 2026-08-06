from helpers import get_github_user, create_report


usernames = ["github", "octocat", "AnusyaYurchenko", "fake-user-123456789"]
output_file = "github_users_report.txt"


create_report(usernames, output_file)

print(f"Report generated: {output_file}")
