# Selenium end-to-end test for Todo List App
Below is an outline of the detailed steps you and your group should follow to create and execute an automated end-to-end test with Selenium. The goal is to practice writing, running, and debugging a practical Selenium test for our Todo List App. By the end of this assignment, you will be able to:

- Set up your local environment for Selenium testing (Python, Selenium library, and ChromeDriver).

- Write a basic Selenium test that automates adding a new regular task to the Todo List App.

- Integrate best practices for debugging, error handling, and test design.

- (Optional) Prepare your test script for potential integration into a CI/CD pipeline.

- (Optional) Try to use the other tools (Cypress and Playwright) and compare them in effeciency and ease of use.

# Learning Path
***1. Environment Preparation***
  - Make sure you have Python installed on your machine.

  - Install the Selenium package via: pip install selenium

  - Download and place ChromeDriver (or another browser driver) in your system PATH. Refer to the Selenium documentation for driver requirements.


***2. Exploring the Todo List App***
  - Review the provided Todo List App files (index.html, script.js, and styles.css).

  - Understand the structure of the HTML elements—particularly the input field (ID: taskInput) and the “Add Task” button.

  - Serve your files locally (e.g., using a simple HTTP server or just simply opening the page via file:// URL).


***3. Creating a Basic Selenium Test***
  - Write a Python script that initializes a ChromeDriver instance and navigates to the Todo List App’s index.html.

  - Locate the task input field and the “Add Task” button using Selenium locators (ID, XPath, CSS selectors, etc.).

  - Simulate adding a task by sending text (e.g., “Buy groceries”) to the input field and clicking the “Add Task” button.

***4. Implementing Waits and Assertions***
  - Incorporate explicit waits so your test script patiently waits for the new task to appear in the DOM.

  - Use assertions (e.g., assert) to verify the newly added task actually appears in the list.

  - Example: Check that “Buy groceries” is contained in the newly rendered li element.

***5. Debugging Strategies***
  - Configure logging in Python (logging module) and capture screenshots on errors.

  - Familiarize yourself with techniques such as headless mode for non-GUI testing and capturing console or network logs for deeper debugging.

  - Explore advanced debugging tools in conjunction with your browser’s developer tools.

***6. Error Handling and Dynamic Elements***
  - Learn how to gracefully handle test failures, potential off-by-one bugs, or references to dynamically created DOM elements.

  - For the Todo List App, dynamic content is added when new tasks appear in the ul#taskList.

  - Use robust locators (e.g., partial text matching) and explicit waits for unpredictably loading elements.

***7. Optional: Integrating with CI/CD***
  - Optionally, but recommended, adapt your script so it can be triggered automatically via a continuous integration tool like GitHub Actions or Jenkins.

  - Running your Selenium tests in headless mode is particularly useful for pipeline automation.

***8. Optional: Try other tools***
  - Try to use the other tools (Cypress and Playwright) and compare them in efficiency and ease of use.

***9. Documentation and Reflection***
  - Keep track of your test steps, any issues encountered, and screenshots/logs if failures occur.

  - Share your experiences, discussing what worked smoothly and where you encountered obstacles.

# Step-by-Step Instructions
***1. Assign Roles***
  - Decide who will focus on environment setup, test writing, debugging, and optional CI/CD integration.

  - Collaborate on code and share updated scripts frequently.

***2. Clone or Copy the Todo List App***
  - Place the index.html, script.js, and styles.css files in a folder served locally or opened via file://.

***3. Create a Python Script***
  - Import Selenium libraries.

  - Initialize the webdriver.Chrome() driver.

  - Navigate to your index.html file (e.g., driver.get("file:///path/to/index.html")).

***4. Locate Elements and Send Interactions***
  - Use find_element methods with IDs or XPath queries for the input field (taskInput) and the “Add Task” button.

  - Send a sample task name via send_keys("Buy groceries") and click the add button.

***5. Add Waits and Assertions***
  - Implement an explicit wait (WebDriverWait + ExpectedConditions) to confirm the new li item is added to the list.

  - Use assert "Buy groceries" in new_task.text to ensure the text is indeed in the DOM.

***6. Incorporate Debugging Tools***
Set up Python logging to capture info and errors.

On exception, save a screenshot with driver.save_screenshot("debug.png").

***7. Try Headless Mode (Optional)***
Configure ChromeOptions to run in headless mode for a more CI/CD-friendly environment.

***8. Optional CI/CD Integration***
Explore how to commit your test script to a GitHub repository and set up GitHub Actions to run the test automatically.

***9. Optional: Try to use the other tools (Cypress and Playwright) and compare them in effeciency and ease of use.***

***10. Document and Submit***
Record steps, highlight issues encountered and solutions, and gather screenshots/logs demonstrating your test’s success or failure.

Summarize your learning and provide suggestions for future improvements or expansions.

Include screenshots.

Include short individual reflections.

# Expected Outcomes
1. Working Test Script: A Python file that runs a Selenium test to add a new task in the Todo List App.

2. Demonstrated Debugging: Screenshots or logs showing how you handled a test error.

3. Solid Understanding: Familiarity with Selenium locators, waits, and best practices in test design.

4. Group Collaboration: Clear division of roles and efficient communication throughout the assignment.

***Bonus:*** If your group integrates the script into a CI/CD tool and shows automated test runs on every commit, you’ll gain additional experience that ties in neatly with real-world DevOps workflows.
