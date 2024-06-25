from modules.funcs.console import *
import requests

def f(url, payloads, method):
    
    try:
        if method == '1':
            # Method 1: Injecting into URL parameters
            for payload in payloads:
                payload = payload.strip()  # Remove leading/trailing whitespaces and newlines
                try:
                    response = requests.get(f"{url}?cmd={payload}")

                    if 'RCE_SUCCESS' in response.text:
                        print_success(f"Payload: {payload} - Remote Code Execution FOUND! (Method 1)")
                    else:
                        print_warning(f"Payload: {payload} - Not Vulnerable (Method 1)")

                except requests.exceptions.RequestException as e:
                    print_error(f"Error (requests): {e}")

        elif method == '2':
            # Method 2: Injecting into POST form data
            for payload in payloads:
                payload = payload.strip()  # Remove leading/trailing whitespaces and newlines
                try:
                    data = {'cmd': payload}  # Adjust data fields as per the form
                    response = requests.post(url, data=data)

                    if 'RCE_SUCCESS' in response.text:
                        print_success(f"Payload: {payload} - Remote Code Execution FOUND! (Method 2)")
                    else:
                        print_warning(f"Payload: {payload} - Not Vulnerable (Method 2)")

                except requests.exceptions.RequestException as e:
                    print_error(f"Error (requests): {e}")

        else:
            print_error("Invalid RCE method. Please enter either '1' or '2'.")

    except Exception as e:
        print_error(f"Error: {e}")