import os
import subprocess

from .repos import repos

for repo in repos:
    os.mkdir("repos")
    os.chdir("repos")
    subprocess.run(["git", "clone", repo.url], check=True)
    os.chdir("..")