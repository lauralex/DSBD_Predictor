import random
import time

import requests

if __name__ == '__main__':
    while True:
        resp = requests.get('http://localhost:30433/searches/')
        if resp.ok:
            print(resp.text)
        time.sleep(random.uniform(0.2, 5))