from github import Github
import os

class GithubInterface:

        def __init__(self):
            github_token = os.getenv("GITHUB_TOKEN")
            self.github = Github(github_token)

        def commit_code(self, repo_name, file_path, commit_message, code):
            repo = self.github.get_repo(repo_name)
            repo.create_file(file_path, commit_message, code)

