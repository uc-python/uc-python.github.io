import os
import shutil
from subprocess import run, PIPE
from pathlib import Path

from .repos import repos

folder = Path("repos")
folder.mkdir(exist_ok=True)
subfolders = [f for f in folder.glob("*") if f.is_dir()]
for s in subfolders:
    print(f"deleting {s}")
    shutil.rmtree(s)

os.chdir(folder)
for repo in repos:
    print(f"cloning {repo.name}...")
    run(["git", "clone", repo.url], check=True, stdout=PIPE, stderr=PIPE)
    print("done")