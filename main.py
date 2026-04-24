import asyncio
import sys
from engines.social import scan_social
from engines.breach import check_breach
from utils.display import show_banner, print_result_table, Fore, Style

async def start_investigation(target_user):
    show_banner()
    print(f"{Fore.YELLOW}[*] MEMULAI INVESTIGASI PADA TARGET: {Fore.WHITE}{target_user}")
    print(f"{Fore.CYAN}[1/2] Scanning Social Media Platforms...")
    
    # Menjalankan mesin pemindai media sosial
    social_results = await scan_social(target_user)
    
    print(f"{Fore.CYAN}[2/2] Checking Data Breach Databases...")
    # Menjalankan mesin pemindai kebocoran data
    breach_status, breach_info = await check_breach(target_user)
    
    # Menampilkan Hasil Akhir
    print("\n" + "="*60)
    print_result_table(social_results)
    print("="*60)
    
    # Status Keamanan
    color = Fore.RED if breach_status == "VULNERABLE" else Fore.GREEN
    print(f"\n{Fore.WHITE}DATA BREACH STATUS: {color}{breach_status}")
    print(f"{Fore.WHITE}REPORT: {Fore.YELLOW}{breach_info}")
    print(f"{Fore.WHITE}{'='*60}\n")
    print(f"{Fore.GREEN}[+] INVESTIGASI SELESAI. LOG DISIMPAN KE MARKAS 123TOOL.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_banner()
        print(f"{Fore.RED}[!] Error: Masukkan username target!")
        print(f"{Fore.WHITE}Usage: python main.py <username>")
        sys.exit()
    
    username = sys.argv[1]
    try:
        asyncio.run(start_investigation(username))
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Operasi Dibatalkan.")
