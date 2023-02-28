import requests
import urllib3
from time import sleep

urllib3.disable_warnings()


def load_counters(date: str) -> list:
    response = requests.get(f"https://www.fgis.gost.ru/fundmetrology/eapi/vri?"
                            f"verification_date={date}&org_title=*дьяченко*"
                            f"&start=0&rows=100", verify=False).json()
    sleep(1)
    counters = []
    count = 0
    start = 0
    total_count = response['result']['count']

    while count < total_count:
        response = requests.get(f"https://www.fgis.gost.ru/fundmetrology/eapi/vri?"
                                f"verification_date={date}&org_title=*дьяченко*"
                                f"&start={start}&rows=100", verify=False).json()

        if len(response['result']['items']):
            for i in response['result']['items']:
                counters.append(i)
        else:
            break
        start += 100
        count += 100
        sleep(1)

    return counters



