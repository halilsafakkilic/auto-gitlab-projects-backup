import time
import requests


def get_time() -> str:
    return str(int(time.time()))


def write_log(message: str, timePrint: bool = True):
    if timePrint:
        print(get_time() + ': ' + message)
    else:
        print(message)


def fetch_projects(private_token: str, page: int):
    write_log('Projects fetching... (Page: ' + str(page) + ')')

    response = requests.get('https://gitlab.com/api/v4/projects?private_token=' + private_token + '&simple=true&sort=asc&membership=true&page=' + str(page) + '&per_page=100')
    if response.status_code != 200:
        write_log('ERROR: #' + str(response.status_code) + ' ' + response.text)
        exit(1)

    write_log('Projects fetched. (Page: ' + str(page) + ')')

    return response.json()


def load_projects(private_token: str):
    page = 1

    output = []
    while True:
        response = fetch_projects(private_token, page)
        if len(response) == 0:
            break

        output += response
        page += 1

    return output
