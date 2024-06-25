import requests
import socket
import selenium
from sys import *
from modules.funcs.console import *
from modules.funcs.menus import *
from modules import files, license, cors, rfi, rce, clickjacking, open_r, dom_xss, re_xss, sqli, ssrf, ssltls, xxe, tech, subfinder
from colorama import Fore, Style
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pystyle import *

def get_links_from_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [urljoin(url, link.get('href')) for link in soup.find_all('a', href=True)]
            return links
        else:
            print_error(f"Failed to get links from page {url}. Status code: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        print_error(f"Error (requests) while getting links from page {url}: {e}")
        return []
    
def crawl_and_test_links(base_url, xss_payloads, sql_payloads, rce_payloads, ssti_payloads, open_redirection_payloads, rfi_payloads, max_depth=3):
    visited_urls = set()

    def crawl(url, depth):
        try:
            if depth > max_depth or url in visited_urls:
                return

            visited_urls.add(url)
            print(f"Crawling: {url}")
            links = get_links_from_page(url)

            for link in links:
                re_xss.f(link, xss_payloads)
                dom_xss.f(link, xss_payloads, browser='chrome')
                sqli.f(link, sql_payloads, method='1')
                rce.f(link, rce_payloads, method='1')
                open_r.f(link, open_redirection_payloads)
                ssrf.f(link, ssti_payloads)
                rfi.f(link, rfi_payloads, method='1')
                cors.f(link)
                files.f(link)
                files.f2(link)
                subfinder.f(link)
                clickjacking.f(link)

                crawl(link, depth + 1)

        except Exception as e:
            print_error(f"Error in crawl function: {e}")

    crawl(base_url, 1)

def main():
    try:
        
        with open('payloads/xss.txt', 'r', encoding='utf-8') as f:
            xss_payloads = f.readlines()

        with open('payloads/sqli.txt', 'r', encoding='utf-8') as f:
            sql_payloads = f.readlines()

        with open('payloads/rce.txt', 'r', encoding='utf-8') as f:
            rce_payloads = f.readlines()

        with open('payloads/ssti.txt', 'r', encoding='utf-8') as f:
            ssti_payloads = f.readlines()

        with open('payloads/xxe.txt', 'r', encoding='utf-8') as f:
            xxe_payloads = f.readlines()

        with open('payloads/openred.txt', 'r', encoding='utf-8') as f:
            open_redirection_payloads = f.readlines()

        with open('payloads/rfi.txt', 'r', encoding='utf-8') as f:
            rfi_payloads = f.readlines()
    
        clear()
        banner()

        while True:
            prompt = """
╔═══[root@Nexa]
╚══>"""
            blue_to_purple_prompt = Colorate.Horizontal(Colors.blue_to_purple, prompt)
            stdout.write(blue_to_purple_prompt + "\033[37m")
            choice = input("")
            
            if choice == 'help' or choice == 'h' or choice == '?':
                help()
            elif choice == 'scanners' or choice =='s':
                scanners()
            elif choice == 'tools' or choice == 't':
                tools()
            elif choice == 'license' or choice == 'l':
                license()
            elif choice == 'rexss' or choice == 'REXSS':
                url = input("Enter the URL where XSS payload will be submitted: ")
                re_xss.f(url, xss_payloads)
            elif choice == 'dxss' or choice == 'DXSS':
                url = input("Enter the URL where DOM-based XSS payload will be submitted: ")
                browser = input("Enter the browser you want to use (chrome / firefox / safari / edge): ")
                dom_xss.f(url, xss_payloads, browser)
            elif choice == 'sqli' or choice =='sq' or choice =='sql' or choice == 'SQLI':
                url = input("Enter the URL where SQL Injection payload will be submitted: ")
                print("Choose SQL injection method:")
                print("1. Injecting into URL parameters")
                print("2. Injecting into POST form data")
                print("3. Injecting into cookies")
                method = input("Enter your choice (1, 2, or 3): ")
                sqli.f(url, sql_payloads, method)
            elif choice == 'rce' or choice == 'RCE':
                url = input("Enter the URL where Remote Code Execution payload will be submitted: ")
                print("Choose RCE method:")
                print("1. Injecting into URL parameters")
                print("2. Injecting into POST form data")
                method = input("Enter your choice (1 or 2): ")
                rce.f(url, rce_payloads, method)
            elif choice == 'ssrf' or choice == 'SSRF':
                url = input("Enter the URL where SSRF payload will be submitted: ")
                ssrf.f(url, ssti_payloads)
            elif choice == 'or' or choice == 'OR':
                url = input("Enter the URL where Open Redirection payload will be tested: ")
                open_r.f(url, open_redirection_payloads)
            elif choice == 'all' or choice == 'ALL':
                url = input("Enter the base URL to start crawling and testing: ")
                crawl_and_test_links(url, xss_payloads, sql_payloads, rce_payloads, ssti_payloads, open_redirection_payloads, rfi_payloads)
            elif choice == 'ssltls' or choice == 'SSLTLS':
                url = input("Enter the URL to test: ")
                ssltls.f(url)
            elif choice == 'cj' or choice == 'CJ':
                url = input("Enter the URL to test: ")
                clickjacking.f(url)
            elif choice == 'xxe' or choice == 'XXE':
                url = input("Enter the URL where XXE payload will be submitted: ")
                print("Choose RCE method:")
                print("1. Injecting into URL parameters")
                print("2. Injecting into POST form data")
                print("3. Injecting into headers")
                method = input("Enter your choice (1 or 2, 3): ")
                xxe.f(url, xxe_payloads, method)
            elif choice == 'rfi' or choice == 'RFI':
                url = input("Enter the URL where RFI payload will be submitted: ")
                print("Choose RFI method: ")
                print("1. Injecting into URL parameters")
                print("2. Injecting into POST form data")
                method = input("Enter your choice (1 or 2): ")
                rfi.f(url, rfi_payloads, method)
            elif choice == 'cors' or choice == 'CORS':
                url = input("Enter the URL where CORS payload will be submitted: ")
                cors.f(url)
            elif choice == 'server' or choice == 'SERVER':
                url = input("Enter the URL to check: ")   
                checking = url.replace('http://', '').replace('https://', '')
                domain_to_ip = socket.gethostbyname(checking)
                protocol = tech.detect_http_or_https(url)
                url = protocol
                print(Colorate.Horizontal(Colors.blue_to_purple, f'[-] Target Domain: {checking}'))
                print(Colorate.Horizontal(Colors.blue_to_purple, f'[-] Target IP: {domain_to_ip}'))
                print(Colorate.Horizontal(Colors.blue_to_purple, f'[-] PROTOCOL: {url}'))
                server = tech.detect_server(url)
                print(Colorate.Horizontal(Colors.blue_to_purple, f"[-] SERVER: {server}"))
                tech.port_etc(domain_to_ip)
            elif choice == 'subfinder' or choice == 'SUBFINDER':
                url = input("Enter the URL to find subdomains: ")
                print(url)
                subfinder.f(url)
            elif choice == 'log' or choice == 'LOG':
                url = input("Enter the URL to find log files in: ")
                files.f2(url)
            elif choice == 'backup' or choice == 'BACKUP':
                url = input("Enter the URL to find backup files in: ")
                files.f(url)
            elif choice == 'clear' or choice == 'cls':
                clear()
                banner()
            elif choice == 'exit' or choice == 'q' or choice == 'quit' or choice == 'e':
                print("Exiting Nexa. Goodbye!")
                exit(0)
            else:
                print_error(f"Invalid choice {choice}. Try again.")

    except FileNotFoundError:
        print_error("One or more payload files not found.")
    except KeyboardInterrupt:
        print("\nNexa terminated by user. Goodbye!")
    except Exception as e:
        print_error(f"Error: {e}")

if __name__ == "__main__":
    main()
    
