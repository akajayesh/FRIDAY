import os

def open_website(url):
    sites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "linkedin": "https://www.linkedin.com",
        "instagram" : "https://www.instagram.com",
        "facebook": "https://www.facebook.com",
        "stackoverflow" : "https://stackoverflow.com",
        "chatgpt" : "https://chat.openai.com",
        "github" : "https://github.com",
        "gfg" : "https://geeksforgeeks.org",
        "whatsapp" : "https://web.whatsapp.com",
        "goclasses" : "https://goclasses.in" 
    }

    if url in sites:
        os.system(f'start {sites[url]}')
        return f"Opening {url.title()} 🌐"
    else:
        return "I don't know this website..."
