import ssl
import socket
from modules.funcs.console import *

def f(url):
    try:
        context = ssl.create_default_context()
        connection = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=url)

        connection.connect((url, 443))
        certificate = connection.getpeercert()

        # Check for outdated protocols
        if 'SSL 2.0' in certificate['protocol']:
            print_warning(f"SSL/TLS Security Check - Outdated Protocol: SSL 2.0 detected.")
        if 'SSL 3.0' in certificate['protocol']:
            print_warning(f"SSL/TLS Security Check - Outdated Protocol: SSL 3.0 detected.")

        # Check for weak cipher suites
        cipher_suite = certificate['cipher']
        if 'RC4' in cipher_suite or 'MD5' in cipher_suite:
            print_warning(f"SSL/TLS Security Check - Weak Cipher Suite detected: {cipher_suite}")

        # Additional checks can be added as needed

        print_success(f"SSL/TLS Security Check passed. No critical issues detected.")

    except socket.error as e:
        print_error(f"Error (socket): {e}")
    except ssl.SSLError as e:
        print_error(f"Error (SSL): {e}")
    except Exception as e:
        print_error(f"Error: {e}")