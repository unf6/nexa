import requests
from modules.funcs.console import *

def f(url, payloads):
    try:
        for payload in payloads:
            payload = payload.strip()  # Remove leading/trailing whitespaces and newlines
            try:
                data = {'template': payload}  # Adjust the data field name as per the target application
                response = requests.post(url, data=data)

                if 'SSTI_SUCCESS' in response.text:
                    print_success(f"Payload: {payload} - Server-Side Template Injection FOUND!")
                else:
                    print_warning(f"Payload: {payload} - Not Vulnerable")

            except requests.exceptions.RequestException as e:
                print_error(f"Error (requests): {e}")

    except Exception as e:
        print_error(f"Error: {e}")