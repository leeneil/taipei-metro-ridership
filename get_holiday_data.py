import os
import re
import requests


def download_file(url, output_path, filename):
    os.makedirs(output_path, exist_ok=True)
    r = requests.get(url)
    with open(os.path.join(output_path, filename), 'wb') as f:
        f.write(r.content)


def main():
    url = "https://data.ntpc.gov.tw/api/v1/rest/datastore/382000000A-000077-002"
    download_file(url, "data/", "holidays.json")


if __name__ == "__main__":
    main()
