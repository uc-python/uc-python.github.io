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
with open(index, "wt") as f:
    f.write("<h1>UC Python Slides</h1>\n")
    f.write("<ul>\n")
    for repo in folder.glob("*"):
        slides_dir = (repo / "slides")
        if not slides_dir.exists():
            print(f"no slides in {slides_dir}, skipping")
            continue
        slides_dir.rename(site / repo.name)
        f.write(f'<li><a href="{repo.name}">{repo.name}</a>\n</li>\n')
    f.write("</ul>\n")