import os
from subprocess import run
from pathlib import Path

folder = Path("repos")

for repo in folder.glob("*"):
    os.chdir(repo)
    print(f"building slides for {repo.name}...")
    run(["make", "slides"], check=True)
    print("done")