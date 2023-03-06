import csv
from dataclasses import dataclass

__all__ = ['repos', 'Repo']

@dataclass
class Repo:
    name: str
    url: str


with open('repos.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)
    repos = [Repo(r["name"], r["url"]) for r in reader]
