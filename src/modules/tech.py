import requests
import socket
from pystyle import *

def detect_http_or_https(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.url
        return 'Unknown'
    except requests.exceptions.RequestException:
        return 'Invalid'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def detect_cms(domain):
    try:
        # Send a GET request to the domain with custom User-Agent header
        response = requests.get(f"http://{domain}", headers=headers)

        # Extract the response content
        content = response.text

        # Detect CMS based on common patterns
        if "WordPress" in content:
            return "WordPress"
        elif "Joomla" in content:
            return "Joomla"
        elif "Drupal" in content:
            return "Drupal"
        elif "Magento" in content:
            return "Magento"
        else:
            return Colors.red+"NOT DETECTED"

    except requests.exceptions.RequestException as e:
        pass

def detect_server(url):
    try:
        response = requests.head(f"http://{url}", headers=headers)
        server = response.headers.get('Server')
        if server:
            return server
        else:
            return Colors.red+"NOT DETECTED"
    except requests.exceptions.RequestException as e:
        pass

    
def port_etc(url):
    checking = url.replace('http://', '').replace('https://', '')
    domain_to_ip = socket.gethostbyname(checking)
    dest = f"https://internetdb.shodan.io/{domain_to_ip}"
    response = requests.get(dest)
    data = response.json()
    ports = data.get('ports', [])
    vulns = data.get('vulns', [])
    cpes = data.get('cpes', [])
    tags = data.get('tags', [])
    print(Colorate.Horizontal(Colors.blue_to_purple, f'[-] Ports: {ports}'))
    print(Colorate.Horizontal(Colors.blue_to_purple, f'[-] Vulns: {vulns}'))
    print(Colorate.Horizontal(Colors.blue_to_purple, f'[-] Cpes:  {cpes}'))
    print(Colorate.Horizontal(Colors.blue_to_purple, f'[-] Tags:  {tags}'))