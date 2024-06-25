from colorama import Fore, Style
def print_success(message):
    print(Fore.GREEN + message + Style.RESET_ALL)

def print_warning(message):
    print(Fore.YELLOW + message + Style.RESET_ALL)

def print_error(message):
    print(Fore.RED + message + Style.RESET_ALL)