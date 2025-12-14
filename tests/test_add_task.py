"""
tests/test_add_task.py

Standalone Selenium test to add a regular task to the To-Do List App.

Features:
- Uses webdriver-manager to install a compatible ChromeDriver automatically.
- Clears localStorage before the test to avoid state leakage.
- Targets the task text span (ignores the Delete button text).
- Uses explicit waits and robust locators.
- Saves a screenshot on failure and logs useful information.
- Configurable via environment variables:
    TODO_APP_URL  - URL to the app (default: file:///C:/Users/jonas/Github/ToDoListApp/index.html)
    HEADLESS      - "true"/"1"/"yes" to run headless (default: true)
"""

import logging
import os
import sys
from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException

from webdriver_manager.chrome import ChromeDriverManager

# ---------- Configuration ----------
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

DEFAULT_LOCAL_PATH = Path(r"C:\Users\jonas\Github\ToDoListApp\index.html").resolve()
DEFAULT_APP_URL = f"file:///{DEFAULT_LOCAL_PATH.as_posix()}"
APP_URL = os.environ.get("TODO_APP_URL", DEFAULT_APP_URL)

TASK_TEXT = "Buy groceries"
ARTIFACTS_DIR = Path("artifacts/screenshots")
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

HEADLESS = os.environ.get("HEADLESS", "true").lower() in ("1", "true", "yes")
WAIT_TIMEOUT = int(os.environ.get("WAIT_TIMEOUT", "10"))

# ---------- Helpers ----------
def create_driver(headless: bool = True) -> webdriver.Chrome:
    opts = Options()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1200,900")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--log-level=3")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=opts)
    return driver

def save_screenshot(driver, name_prefix="failure"):
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    path = ARTIFACTS_DIR / f"{name_prefix}_{ts}.png"
    try:
        driver.save_screenshot(str(path))
        logger.info("Saved screenshot: %s", path)
    except Exception:
        logger.exception("Failed to save screenshot")

# ---------- Test ----------
def test_add_task():
    logger.info("Starting test_add_task")
    logger.info("APP_URL = %s", APP_URL)
    driver = create_driver(headless=HEADLESS)
    wait = WebDriverWait(driver, WAIT_TIMEOUT)

    try:
        driver.get(APP_URL)
        logger.info("Opened app")

        try:
            driver.execute_script("window.localStorage.clear();")
            logger.info("Cleared localStorage")
            driver.refresh()
        except Exception:
            logger.warning("Could not clear localStorage; continuing")

        input_el = wait.until(EC.presence_of_element_located((By.ID, "taskInput")))
        logger.info("Found task input element")

        add_btn = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addTask()"]')
        logger.info("Found Add Task button")

        input_el.clear()
        input_el.send_keys(TASK_TEXT)
        add_btn.click()
        logger.info("Clicked Add Task with text: %s", TASK_TEXT)

        locator = (By.CSS_SELECTOR, "ul#taskList li:last-child span")
        wait.until(EC.text_to_be_present_in_element(locator, TASK_TEXT))
        span = driver.find_element(*locator)
        assert span.text == TASK_TEXT, f"Expected task text '{TASK_TEXT}', got '{span.text}'"
        logger.info("Task added and verified: %s", span.text)

    except (TimeoutException, AssertionError, NoSuchElementException, WebDriverException) as exc:
        logger.exception("Test failed: %s", exc)
        save_screenshot(driver, "test_add_task_failure")
        raise
    finally:
        driver.quit()
        logger.info("Driver quit")

if __name__ == "__main__":
    try:
        test_add_task()
        logger.info("Test completed successfully")
        sys.exit(0)
    except Exception:
        logger.error("Test failed")
        sys.exit(1)
