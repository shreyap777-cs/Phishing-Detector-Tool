from email_model import predict_email, find_suspicious_words
from url_checker import check_url, extract_links


# -------------------------------
# Main Analysis Function
# -------------------------------
def analyze_email(text):
    result = ""
    risk_score = 0

    # ---------------------------
    # 1. Email Prediction
    # ---------------------------
    email_result = predict_email(text)
    result += email_result + "\n\n"

    if "Phishing" in email_result:
        risk_score += 2

    # ---------------------------
    # 2. Suspicious Keywords
    # ---------------------------
    words = find_suspicious_words(text)
    if words:
        result += "Suspicious keywords: " + ", ".join(words) + "\n\n"
        risk_score += 1

    # ---------------------------
    # 3. URL Detection
    # ---------------------------
    links = extract_links(text)

    if links:
        result += "Detected Links:\n"

        for link in links:
            status, reasons = check_url(link)

            # URL status
            result += f"{link} → {status}\n"

            # Reasons for suspicion
            if reasons:
                result += "Reasons:\n"
                for r in reasons:
                    result += f"- {r}\n"

            result += "\n"

            # Risk scoring
            if "Highly Suspicious" in status:
                risk_score += 3
            elif "Possibly Suspicious" in status:
                risk_score += 2

    # ---------------------------
    # 4. Final Risk Level
    # ---------------------------
    if risk_score >= 4:
        result += "Overall Risk: HIGH 🚨"
    elif risk_score >= 2:
        result += "Overall Risk: MEDIUM ⚠️"
    else:
        result += "Overall Risk: LOW ✅"

    return result


# -------------------------------
# Run Test (only when running file directly)
# -------------------------------
if __name__ == "__main__":
    sample = "Win free money now!!! Click http://fake-login.com immediately"
    print(analyze_email(sample))