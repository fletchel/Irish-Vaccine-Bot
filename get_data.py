from bs4 import BeautifulSoup as bs

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time

opts = Options()
opts.headless = True


# getting weird issues with networking so use following boilerplate to make it work
# not sure if this is potentially a security issue lol

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


def scrape_data():

    browser = Chrome('/Users/luanfletcher/Downloads/chromedriver', options=opts)
    browser.get("https://covid-19.geohive.ie/")
    time.sleep(5)

    elems = browser.find_elements_by_xpath('//*[@class="ss-value" or @class="ss-title"]')

    text = [e.text for e in elems]

    browser.close()

    return text


def check_new(prev_v, prev_v2):

    text = scrape_data()

    cur_v = 0
    cur_v2 = 0
    cur_date = 0

    for i, t in enumerate(text):

        if t == 'Vaccine Data Last Updated':

            cur_date = text[i+1]

        if t == 'Total 1st Dose Vaccines Administered':

            cur_v = text[i+1]

        if t == "Total 2nd Dose Vaccines Administered":

            cur_v2 = text[i+1]
            break

    if cur_v != 0 and cur_date != 0 and cur_v2 != 0:

        cur_v = cur_v.replace(',', '')
        cur_v2 = cur_v2.replace(',', '')
        cur_v = int(cur_v)
        cur_v2 = int(cur_v2)

        if cur_v != prev_v and cur_v2 != prev_v2:

            return cur_v, cur_date, cur_v2

    return 0, 0, 0

