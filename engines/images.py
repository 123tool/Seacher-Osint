import aiohttp
import os
from PIL import Image
from PIL.ExifTags import TAGS

async def download_and_audit(session, url, username):
    """Mengunduh foto profil dan cek Metadata EXIF"""
    if not os.path.exists('intel_reports'):
        os.makedirs('intel_reports')
        
    path = f"intel_reports/{username}_avatar.jpg"
    
    try:
        async with session.get(url) as resp:
            if resp.status == 200:
                with open(path, 'wb') as f:
                    f.write(await resp.read())
                
                # Analisis Metadata Dasar
                with Image.open(path) as img:
                    info = img._getexif()
                    if info:
                        exif_data = {TAGS.get(tag): value for tag, value in info.items() if tag in TAGS}
                        return f"SUCCESS (Saved to {path})", exif_data
                return f"SUCCESS (No Metadata Found)", None
    except Exception as e:
        return f"FAILED: {str(e)}", None
