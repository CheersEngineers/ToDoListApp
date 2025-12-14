import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

APP_URL = os.environ.get("TODO_APP_URL", "http://localhost:8000/index.html")

@pytest.fixture(scope="function")
def driver():
    opts = Options()
    if os.environ.get("HEADLESS", "true").lower() in ("1","true","yes"):
        opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1200,900")
    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=opts)
    yield drv
    drv.quit()

@pytest.fixture(autouse=True)
def open_app_and_clear(driver):
    driver.get(APP_URL)
    driver.execute_script("window.localStorage.clear();")
    driver.refresh()
    return driver
