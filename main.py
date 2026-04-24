import asyncio
import aiohttp
import os
import sys
import time
from colorama import Fore, Style, init
from prettytable import PrettyTable
from PIL import Image
from PIL.ExifTags import TAGS

# Inisialisasi warna terminal
init(autoreset=True)

# --- KONFIGURASI TARGET SITE ---
SITES = {
    "Instagram": "https://www.instagram.com/{}",
    "GitHub": "https://github.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "YouTube": "https://www.youtube.com/@{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Linktree": "https://linktr.ee/{}",
    "Telegram": "https://t.me/{}",
    "Chess.com": "https://www.chess.com/member/{}"
}

# --- FUNGSI UI & DISPLAY ---
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

# --- FUNGSI ENGINES (SOCIAL, BREACH, IMAGE) ---
async def check_site(session, site_name, url_template, username):
    url = url_template.format(username)
    try:
        async with session.get(url, timeout=5) as response:
            if response.status == 200:
                return site_name, url, "FOUND"
            return site_name, url, "NOT FOUND"
    except:
        return site_name, url, "ERROR"

async def check_breach(username):
    url = f"https://api.proxynova.com/comb?query={username}"
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=7) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("count", 0) > 0:
                        return "VULNERABLE", f"{data['count']} Leaks Found"
                    return "CLEAN", "No Leaks Found"
                return "UNKNOWN", "API Timeout"
        except:
            return "ERROR", "Connection failed"

async def download_and_audit(session, username):
    if not os.path.exists('intel_reports'):
        os.makedirs('intel_reports')
    
    avatar_url = f"https://github.com/{username}.png"
    path = f"intel_reports/{username}_avatar.jpg"
    
    try:
        async with session.get(avatar_url) as resp:
            if resp.status == 200:
                content = await resp.read()
                with open(path, 'wb') as f:
                    f.write(content)
                
                with Image.open(path) as img:
                    info = img._getexif()
                    if info:
                        exif = {TAGS.get(tag): val for tag, val in info.items() if tag in TAGS}
                        return f"SUCCESS (Saved: {path})", exif
                return f"SUCCESS (No Metadata)", None
            return "FAILED (No Avatar Found)", None
    except:
        return "ERROR (Skip Image Scan)", None

# --- CORE EXECUTION ---
async def start_investigation(target_user):
    show_banner()
    async with aiohttp.ClientSession() as session:
        print(f"{Fore.YELLOW}[*] TARGET: {Fore.WHITE}{target_user}")
        print(f"{Fore.CYAN}[1/3] Scanning Social Media...")
        
        tasks = [check_site(session, name, url, target_user) for name, url in SITES.items()]
        social_results = await asyncio.gather(*tasks)
        
        print(f"{Fore.CYAN}[2/3] Checking Data Breaches...")
        breach_status, breach_info = await check_breach(target_user)
        
        print(f"{Fore.CYAN}[3/3] Auditing Profile Image...")
        img_status, exif = await download_and_audit(session, target_user)
        
        # TABEL HASIL
        print("\n" + "="*65)
        table = PrettyTable()
        table.field_names = [f"{Fore.CYAN}PLATFORM", f"{Fore.CYAN}STATUS", f"{Fore.CYAN}URL"]
        for site, url, status in social_results:
            color = Fore.GREEN if status == "FOUND" else Fore.WHITE
            table.add_row([f"{Fore.WHITE}{site}", f"{color}{status}", f"{Fore.BLUE}{url}"])
        print(table)
        
        # FINAL REPORT
        print("="*65)
        b_color = Fore.RED if breach_status == "VULNERABLE" else Fore.GREEN
        print(f"BREACH STATUS : {b_color}{breach_status} ({breach_info})")
        print(f"IMAGE INTEL   : {Fore.YELLOW}{img_status}")
        if exif:
            print(f"METADATA      : {Fore.MAGENTA}Detected (Check intel_reports/)")
        print("="*65)
        print(f"\n{Fore.GREEN}[+] INVESTIGASI SELESAI. DATA DISIMPAN DI MARKAS 123TOOL.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_banner()
        print(f"{Fore.RED}[!] Usage: python main.py <username>")
        sys.exit()
    
    try:
        asyncio.run(start_investigation(sys.argv[1]))
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Shutdown.")
