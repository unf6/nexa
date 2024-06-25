import requests
from pystyle import *
from modules.funcs.console import *

def f(url):
    headers = {
        'Origin': 'example.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.options(url, headers=headers, timeout=5)
        response_text = response.text

        if 'example' in response_text:
            print_success(f"[-] URL: {url}  [Vulnerable]\n")
        else:
            print_error(f"URL: {url}  [Not Vulnerable]\n")

    except requests.exceptions.RequestException as e:
        print_error(Colors.red + f"[-] An error occurred for URL: {url}\n{e}")


