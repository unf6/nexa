import requests
from urllib.parse import urlparse
import io
from modules.funcs.console import *

def is_binary_file(file):
    try:
        return isinstance(file.read(0), bytes)
    except io.UnsupportedOperation:
        return True
    
def is_valid_log_file(content_type, content):
    valid_types = {"text/plain"}
    return content_type in valid_types and not is_binary_file(content)

def f2(url):
    log_files = ["access.log", "error.log", "log.log"]
    parsed_url = urlparse(url)
   
    for log_file in log_files:
        log_url = f"{parsed_url.scheme}://{parsed_url.netloc}/{log_file}"
        response = requests.get(log_url)
        if response.status_code == 200 and is_valid_log_file(
            response.headers.get("Content-Type"), response.content
        ):
            print_success("Possible log file exposure.")

    print_error("[-] No log files found.")

def is_valid_backup(content_type, content):
    valid_types = {"application/octet-stream", "application/zip", "application/x-gzip"}

    if content_type in valid_types:
        return not is_binary_file(content)

    return False

def f(url):
    extensions = [".bak", ".zip", ".tgz", ".sql"]
    parsed_url = urlparse(url)

    for extension in extensions:
        backup_url = (
            f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}{extension}"
        )
        response = requests.get(backup_url)
        if response.status_code == 200 and is_valid_backup(
            response.headers.get("Content-Type"), response.content
        ):
            print_success("Possible backup file found.")

    print_error("[-] No backup files found.")
