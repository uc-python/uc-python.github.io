from pathlib import Path

folder = Path("repos")
site = Path("site")
site.mkdir(exist_ok=True)

# Build an index as we go
index = site / "index.html"
index.touch()
for repo in folder.glob("*"):
    (repo / "slides").rename(site / repo.name)
    index.write_text(f'<a href="/{repo.name}">{repo.name}</a>')