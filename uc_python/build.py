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
    slides_dir = folder / repo / "slides"
    if not (slides_dir / "index.html").exists():
        print("generating index.html")
        index = slides_dir / "index.html"
        with open(index, "at") as f:
            f.write("<h1>Slides</h1>\n")
            f.write("<ul>\n")
            slide_files = sorted(slides_dir.glob("*.slides.html"))
            for slide_file in slide_files:
                f.write(f'<li><a href="{slide_file.name}">{slide_file.name}</a></li>\n')
            f.write("</ul>\n")