from pathlib import Path

folder = Path("repos")
site = Path("site")
site.mkdir(exist_ok=True)

for repo in folder.glob("*"):
    (repo / "slides").rename(site / repo.name)