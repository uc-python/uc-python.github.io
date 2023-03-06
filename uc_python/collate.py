import shutil
from pathlib import Path

folder = Path("repos")
site = Path("site").absolute()
site.mkdir(exist_ok=True)
subfolders = [f for f in site.glob("*") if f.is_dir()]
for s in subfolders:
    print(f"deleting {s}")
    shutil.rmtree(s)

# Build an index as we go
index = site / "index.html"
index.write_text("<h1>UC Python Slides</h1>")
for repo in folder.glob("*"):
    slides_dir = (repo / "slides")
    if not slides_dir.exists():
        print(f"no slides in {slides_dir}, skipping")
        continue
    slides_dir.rename(site / repo.name)
    index.write_text(f'<a href="/{repo.name}">{repo.name}</a>\n')