from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TASK = "Buy groceries"

def test_add_task(open_app_and_clear):
    driver = open_app_and_clear
    wait = WebDriverWait(driver, 8)
    driver.find_element(By.ID, "taskInput").send_keys(TASK)
    driver.find_element(By.CSS_SELECTOR, 'button[onclick="addTask()"]').click()
    locator = (By.CSS_SELECTOR, "ul#taskList li:last-child span")
    wait.until(EC.text_to_be_present_in_element(locator, TASK))
    assert driver.find_element(*locator).text == TASK
