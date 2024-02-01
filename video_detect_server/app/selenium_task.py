from celery import shared_task
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


def init__webdriver(url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    return driver


def search_on_youtube(driver, query):
    driver.get("https://www.youtube.com/")
    wait = WebDriverWait(driver, 10)


# apply filter

# get url

# output to video analysis

# pass result to django
