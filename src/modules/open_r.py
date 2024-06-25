from modules.funcs.console import *
import requests

def f(url, payloads):
    try:
        for payload in payloads:
            payload = payload.strip()  # Remove leading/trailing whitespaces and newlines
            try:
                response = requests.get(f"{url}?redirect={payload}", allow_redirects=False)

                if response.status_code == 302 and 'Location' in response.headers:
                    print_success(f"Payload: {payload} - Open Redirection FOUND!")
                    print_warning(f"Redirect URL: {response.headers['Location']}")
                else:
                    print_warning(f"Payload: {payload} - Not Vulnerable")

            except requests.exceptions.RequestException as e:
                print_error(f"Error (requests): {e}")

    except Exception as e:
        print_error(f"Error: {e}")