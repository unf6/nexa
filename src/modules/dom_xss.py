from modules.funcs.console import *
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
def f(url, payloads, browser):
    try:
        driver = None
        if browser.lower() == 'chrome':
            driver = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            driver = webdriver.Firefox()
        elif browser.lower() == 'edge':    
            driver = webdriver.Edge()
        elif browser.lower() =='safari':
            driver = webdriver.Safari()

        # Add other supported browsers here

        if driver:
            for payload in payloads:
                payload = payload.strip()  # Remove leading/trailing whitespaces and newlines
                try:
                    driver.get(url)
                    wait = WebDriverWait(driver, 10)  # Set a timeout of 10 seconds

                    # Try locating the element using different methods
                    element_methods = [
                        ("ID", By.ID),
                        ("Name", By.NAME),
                        ("Class Name", By.CLASS_NAME),
                        ("XPath", By.XPATH)
                    ]

                    element_found = False
                    for method_name, method in element_methods:
                        try:
                            element = wait.until(EC.presence_of_element_located((method, 'message')))
                            element_found = True
                            break
                        except NoSuchElementException:
                            continue

                    if not element_found:
                        print_warning(f"Payload: {payload} - Element not found (via {browser})")
                        continue

                    submit_button = driver.find_element(By.NAME, 'submitbutton')
                    driver.execute_script("arguments[0].value = arguments[1]", element, payload)
                    driver.execute_script("arguments[0].click()", submit_button)

                    driver.implicitly_wait(5)

                    try:
                        if 'XSS' in driver.page_source:
                            print_success(f"Payload: {payload} - DOM-based XSS FOUND! (via {browser})")
                        else:
                            print_warning(f"Payload: {payload} - No XSS (via {browser})")
                    except NoSuchElementException:
                        print_warning(f"Payload: {payload} - Element not found (via {browser})")

                    # Print the page source to analyze the page structure
                    print(driver.page_source)

                except WebDriverException as e:
                    print_error(f"Error ({browser}): {e}")
                    break  # Exit the loop if any error occurs

        else:
            print_error("Unsupported browser. Please select a supported browser.")

    except Exception as e:
        print_error(f"Error: {e}")

    finally:
        if driver:
            driver.quit()