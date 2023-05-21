from github import Github
import os
from git import Repo
import datetime
import openai
from flask import Flask, request
import os

# You should store the token as an environment variable for security reasons
token = os.getenv('GITHUB_TOKEN')

# Create a Github instance:
gh = Github(token)

# Cloning the repo
def clone_repository(repo_fullname, path):
        repo = gh.get_repo(repo_fullname)
        git_url = repo.clone_url
        Repo.clone_from(git_url, path)

#generation of code
def generate_code(instructions):
        # You should also store your OpenAI API key as an environment variable
        openai.api_key = os.getenv('OPENAI_API_KEY')
                
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=instructions,
            temperature=0.5,
            max_tokens=100
        )

        return response.choices[0].text.strip()



def create_commit(repo_path, commit_message):
        repo = Repo(repo_path)
            
        repo.git.add(update=True)
        repo.index.commit(commit_message)

        origin = repo.remote(name='origin')
        origin.push()



app = Flask(__name__)

@app.route('/instructions', methods=['POST'])
def handle_instructions():
    data = request.get_json()

    instructions = data['instructions']
    repo_fullname = data['repo']
                    
    repo_path = f"/tmp/{repo_fullname.split('/')[-1]}"

    clone_repository(repo_fullname, repo_path)

    code = generate_code(instructions)
    with open(os.path.join(repo_path, 'generated_code.py'), 'w') as f:
         f.write(code)

    commit_message = f"GTP generated {datetime.datetime.now()}: {instructions}"
    create_commit(repo_path, commit_message)

    return {'status': 'success'}


