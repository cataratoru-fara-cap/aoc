import sys
import os
import requests


def main():
    if len(sys.argv) < 3:
        print("Usage: python auto_run.py  <day> <year>  --abs_path <abs_path>")
        sys.exit(1)

    day = int(sys.argv[1])
    year = int(sys.argv[2])
    url = f"https://adventofcode.com/{year}/day/{day}/input"

    path = os.getcwd()
    if len(sys.argv) > 4:
        path = sys.argv[4]
  
    path += f"/{day}"

    try:
        os.mkdir(path=path)
    except FileExistsError:
        print(f"Directory {path}/{day} exists")

    try:
        response = requests.get(url)
        response.raise_for_status()

        file = open(f"{path}/{day}/input.txt", 'w')
        file.write(response.text)
        print(f"Content downloaded and saved to {path}/{day}/input")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading content: {e}")


if __name__ == '__main__':
    main()
