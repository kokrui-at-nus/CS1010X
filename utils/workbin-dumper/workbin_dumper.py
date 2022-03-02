import requests
from bs4 import BeautifulSoup

from collections import deque
from pathlib import Path
import csv

##########################################
# COPY-PASTE CURLCONVERTER.COM OUTPUT HERE
# SEE: README.md USAGE SECTION
##########################################


##########################################

seen = set()
if Path("downloaded.csv").is_file():
    with open("downloaded.csv", "r") as downloaded:
        c = csv.reader(downloaded)
        seen = set(map(lambda x: Path(x[0]), filter(lambda y: len(y), list(c))))

with open("downloaded.csv", "a") as downloaded:
    c = csv.writer(downloaded)
    soup = BeautifulSoup(response.text, "html.parser")
    folders = deque(
        map(
            lambda x: (
                x["href"],
                Path("workbin") / Path("".join(x.get_text().split("(")[:-1])[1:-1]),
            ),
            soup.select("tr.material_folder a"),
        )
    )
    while len(folders) > 0:
        cur = folders.popleft()
        cur[1].mkdir(parents=True, exist_ok=True)
        r = requests.get(f"https://coursemology.org{cur[0]}", headers=headers)
        s = BeautifulSoup(r.text, "html.parser")
        for link in s.select("tr.material_folder a"):
            print(
                f"Found Folder: {cur[1]/Path(''.join(link.get_text().split('(')[:-1])[1:-1])}"
            )
            folders.append(
                (
                    link["href"],
                    cur[1] / Path("".join(link.get_text().split("(")[:-1])[1:-1]),
                )
            )
        for file in s.select("tr.material td > a"):
            fpath = cur[1] / file.get_text()
            if fpath not in seen:
                print(f"Downloading: {fpath}")
                r2 = requests.get(
                    f"https://coursemology.org{file['href']}",
                    allow_redirects=True,
                    headers=headers,
                )
                fpath.write_bytes(r2.content)
                seen.add(fpath)
                c.writerow([f"{fpath}"])
