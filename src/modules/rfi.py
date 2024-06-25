import requests
from modules.funcs.console import *

def f(url, payloads, method):
    try:
        if method == '1':
            for payload in payloads:
                payload = payload.strip()
                full_url = f"{url}{payload}"
                response = requests.get(full_url)
                if 'RFI_SUCCESS' in response.text:
                    print_success(f"Payload: {payload} - Remote File Inclusion FOUND!")
                else:
                    print_error(f"Payload: {payload} - Not Vulnerable")
        elif method == '2':
            for payload in payloads:
                payload = payload.strip()
                response = requests.get(url, data={'payload': payload})
                if 'RCE_SUCCESS' in response.text:
                    print_success(f"Payload: {payload} - Remote Code Execution FOUND!")
                else:
                    print_error(f"Payload: {payload} - Not Vulnerable")

    except requests.exceptions.RequestException as e:
        print_error(f"Error (requests): {e}")
