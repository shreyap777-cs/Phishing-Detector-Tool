import re
from urllib.parse import urlparse


# -------------------------------
# 1. Extract links from text
# -------------------------------
def extract_links(text):
    return re.findall(r'http\S+', text)


# -------------------------------
# 2. URL Analysis Function
# -------------------------------
def check_url(url):
    score = 0
    reasons = []

    parsed = urlparse(url)
    domain = parsed.netloc

    if "@" in url:
        score += 2
        reasons.append("Contains '@' symbol")

    if len(url) > 75:
        score += 1
        reasons.append("URL is too long")

    if not url.startswith("https"):
        score += 2
        reasons.append("Not using HTTPS")

    if "-" in domain:
        score += 1
        reasons.append("Hyphen in domain")

    if domain.count('.') > 3:
        score += 1
        reasons.append("Too many subdomains")

    suspicious_words = ["login", "verify", "bank", "secure", "account"]
    for word in suspicious_words:
        if word in url.lower():
            score += 1
            reasons.append(f"Contains '{word}'")

    if score >= 4:
        status = "Highly Suspicious 🚨"
    elif score >= 2:
        status = "Possibly Suspicious ⚠️"
    else:
        status = "Safe URL ✅"

    return status, reasons