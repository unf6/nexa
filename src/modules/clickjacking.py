import requests
from modules.funcs.console import *
def f(url):
    try:
        headers = {
            'Content-Security-Policy': 'frame-ancestors \'none\'',
            'X-Frame-Options': 'deny',
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            if 'X-Frame-Options' in response.headers:
                print_warning(f"URL: {url} - X-Frame-Options is set to {response.headers['X-Frame-Options']}. Clickjacking may be mitigated.")
            elif 'Content-Security-Policy' in response.headers:
                print_warning(f"URL: {url} - Content-Security-Policy is set. Clickjacking may be mitigated.")
            else:
                print_success(f"URL: {url} - No Clickjacking vulnerability detected.")
        else:
            print_warning(f"URL: {url} - Unexpected response status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print_error(f"Error (requests): {e}")