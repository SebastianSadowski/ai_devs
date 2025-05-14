from bs4 import BeautifulSoup

def extract_protection_phrase(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    return soup.find(id="human-question").contents[2].strip()