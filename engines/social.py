import aiohttp
import asyncio

# Daftar platform target (Bisa kamu tambah sampai ratusan)
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

async def check_site(session, site_name, url_template, username):
    url = url_template.format(username)
    try:
        async with session.get(url, timeout=5) as response:
            if response.status == 200:
                return site_name, url, "FOUND"
            elif response.status == 404:
                return site_name, url, "NOT FOUND"
            else:
                return site_name, url, "PROTECTED/UNKNOWN"
    except:
        return site_name, url, "ERROR"

async def scan_social(username):
    results = []
    async with aiohttp.ClientSession() as session:
        tasks = []
        for name, url in SITES.items():
            tasks.append(check_site(session, name, url, username))
        
        results = await asyncio.gather(*tasks)
    return results
