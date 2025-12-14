"""
Minimal Selenium script that performs the UI steps to add a task.
This version intentionally omits explicit waits and assertions so you can
capture a simple run for documentation purposes.
"""

import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

DEFAULT_LOCAL_PATH = Path(r"C:\Users\jonas\Github\ToDoListApp\index.html").resolve()
APP_URL = os.environ.get("TODO_APP_URL", f"file:///{DEFAULT_LOCAL_PATH.as_posix()}")
TASK_TEXT = "Buy groceries"
HEADLESS = os.environ.get("HEADLESS", "true").lower() in ("1", "true", "yes")

def create_driver(headless: bool = True) -> webdriver.Chrome:
    opts = Options()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1200,900")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=opts)

def main():
    driver = create_driver(headless=HEADLESS)
    try:
        print("Opening", APP_URL)
        driver.get(APP_URL)
        try:
            driver.execute_script("window.localStorage.clear();")
            driver.refresh()
        except Exception:
            pass
        input_el = driver.find_element(By.ID, "taskInput")
        add_btn = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addTask()"]')
        input_el.clear()
        input_el.send_keys(TASK_TEXT)
        add_btn.click()
        out_dir = Path("artifacts/screenshots")
        out_dir.mkdir(parents=True, exist_ok=True)
        screenshot_path = out_dir / "simple_add_task_run.png"
        driver.save_screenshot(str(screenshot_path))
        print("Screenshot saved to", screenshot_path)
        try:
            last_li = driver.find_element(By.CSS_SELECTOR, "ul#taskList li:last-child")
            print("Last list item text:", last_li.text)
        except Exception:
            print("Could not read last list item (no waits used).")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
