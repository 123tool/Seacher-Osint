from colorama import Fore, Style, init
from prettytable import PrettyTable

init(autoreset=True)

def show_banner():
    print(f"{Fore.RED}{Style.BRIGHT}")
    print(r"""
  ██████  ██████  ██    ██      ███████ 
 ██      ██    ██  ██  ██       ██      
  █████  ██    ██   ████        █████   
      ██ ██    ██    ██         ██      
 ██████   ██████     ██         ███████ 
    PERSONA-SCRAPER v1.0 | BY: 123TOOL
    """)

def print_result_table(results):
    table = PrettyTable()
    table.field_names = [f"{Fore.CYAN}PLATFORM", f"{Fore.CYAN}STATUS", f"{Fore.CYAN}URL"]
    
    for site, url, status in results:
        if status == "FOUND":
            stat_text = f"{Fore.GREEN}{status}"
        elif status == "NOT FOUND":
            stat_text = f"{Fore.WHITE}{status}"
        else:
            stat_text = f"{Fore.YELLOW}{status}"
            
        table.add_row([f"{Fore.WHITE}{site}", stat_text, f"{Fore.BLUE}{url}"])
    
    print(table)
