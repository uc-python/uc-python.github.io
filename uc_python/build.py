import os
from subprocess import run
from pathlib import Path

folder = Path("repos").absolute()
repo_paths = [f for f in folder.glob("*") if f.is_dir()]

for repo in repo_paths:
    os.chdir(folder / repo)
    if not (repo / "Makefile").exists():
        print("no Makefile, skipping")
        continue
    print(f"building slides for {repo.name}...")
    run(["make", "slides"], check=True)
    print("done")
    print(os.getcwd())