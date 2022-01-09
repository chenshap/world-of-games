import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import os

def test_scores_service(app_url):
    chrome_driver_path = Service(os.environ['CHROME_DRIVER_PATH'])
    # print(chrome_driver_path)
    driver = webdriver.Chrome(service=chrome_driver_path)
    driver.get(app_url)
    driver.implicitly_wait(20)
    q = int((driver.find_element(By.ID, "score")).text)
    if 1 < q < 1000:
        return True
    else:
        return False


def main():
    score = test_scores_service(os.environ['URL'])
    if score:
        sys.exit(0)
    else:
        sys.exit(-1)
