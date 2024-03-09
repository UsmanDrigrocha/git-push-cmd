import os
import click
from getpass import getpass

BASE_URL = 'https://api.github.com'



@click.command()
@click.option('--repo-url', help='GitHub repository URL')
def main(repo_url):
    click.echo("Welcome to Basic GitHub CLI")

    if repo_url:
        init()
        add()
        commit()
        branch()
        remote_origin(repo_url)
        push()


def init():
    click.echo("Initializing a new Git repository.")
    os.system('git init')


def add():
    click.echo("Adding files to the staging area.")
    os.system('git add .')


def commit():
    message = "Initial commit"
    click.echo("Committing changes.")
    os.system(f'git commit -m "{message}"')


def branch():
    branch_name = "main"
    click.echo(f"Creating a new branch: {branch_name}")
    os.system(f'git branch {branch_name}')


def remote_origin(repo_url):
    click.echo(f"Adding remote origin: {repo_url}")
    os.system(f'git remote add origin {repo_url}')


def push():
    choice = input("Do you want to push changes to GitHub repository? (y/n): ").lower()
    if choice == 'y':
        click.echo("Pushing changes to GitHub repository.")
        os.system('git push -u origin main')
    else:
        click.echo("Changes were not pushed to GitHub repository.")


if __name__ == '__main__':
    main()
