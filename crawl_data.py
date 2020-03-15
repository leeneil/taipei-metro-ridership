import os
import re
import requests


def get_list(url, pat):
    html = requests.get(url).content
    results = re.compile(pat).findall(html.decode("utf-8"))
    return results


def download_files(file_list, output_path):
    os.makedirs(output_path, exist_ok=True)
    for result in file_list:
        print(result[0])
        if len(result[1]) < 4:
            year = int(result[1]) + 1911
        else:
            year = int(result[1])
        month = result[2]
        ext = result[3]
        r = requests.get(result[0])
        with open(os.path.join(output_path, "{}{}.{}".format(year, month, ext)), 'wb') as f:
            f.write(r.content)


def main():
    url = "https://www.metro.taipei/cp.aspx?n=FF31501BEBDD0136"
    # get system-wide ridership data
    pat1 = '"(https:\/\/web.metro.taipei\/RidershipCounts\/c\/(\d{2,3})(\d{2})\.(htm))"'
    results1 = get_list(url, pat1)
    print("found {} targets".format(len(results1)))
    download_files(results1, "data/system/")
    pat2 = '"(https:\/\/web\.metro\.taipei\/RidershipPerStation\/(\d{4})(\d{2})_cht\.(ods))"'
    results2 = get_list(url, pat2)
    print("found {} targets".format(len(results2)))
    download_files(results2, "data/station/")


if __name__ == "__main__":
    main()
