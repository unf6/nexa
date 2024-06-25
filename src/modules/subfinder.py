import requests
import re
from concurrent.futures import ThreadPoolExecutor

def f(domain):
    subdomains = set()

    # Use various sources to find subdomains
    sources = [
        f"https://crt.sh/?q=%.{domain}",
        f"https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={domain}",
        f"https://dns.bufferover.run/dns?q=.{domain}",
        f"https://api.seon.io/api/v1/domain/{domain}/subdomains",
        f"https://api.spyse.com/v2/subdomains?domain={domain}"
    ]

    with ThreadPoolExecutor() as executor:
        results = [executor.submit(make_request, source) for source in sources]
        for future in results:
            try:
                response = future.result()
                subdomains.update(re.findall(r"[\w\-]+\.{}".format(domain), response))
            except:
                pass
    
        if subdomains:
            for subdomain in subdomains:
                print(f"{subdomain}\n")
        else:
            print(f"No subdomains found for {domain}.")
            
def make_request(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text