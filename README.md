# Phishing-Detector-Tool
AI-Powered Phishing Detection System : 

An intelligent cybersecurity tool that detects phishing emails using Machine Learning and analyzes malicious URLs using rule-based techniques.<br>

Features : 

AI-based Email Classification , 
Uses TF-IDF and Naive Bayes to detect phishing emails , 
Provides prediction with confidence score , 
URL Security Analysis , 
Detects suspicious links inside emails , 
Checks for HTTPS, domain structure, and phishing patterns , 
Risk Scoring System , 
Combines AI prediction + URL analysis + keywords , 
Outputs overall risk level (Low / Medium / High) , 
Explainable Results , 
Shows suspicious keywords , 
Provides reasons for malicious URLs , 
Interactive Web App , 
Built using Streamlit , 
Real-time email analysis <br>

Tech Stack : 

Python , 
Machine Learning (Naive Bayes), 
TF-IDF Vectorization , 
Streamlit , 
Regex and URL Parsing <br>

Project Structure : 

email_model.py → ML model for email classification<br>
url_checker.py → URL analysis logic<br>
main.py → Integration and risk scoring<br>
app.py → Streamlit UI<br>
dataset.csv → Email dataset<br>

How to Run: <br>

Install dependencies<br>
pip install streamlit pandas scikit-learn<br>
Run the app<br>
python -m streamlit run app.py<br>
Open in browser<br>
http://localhost:8501<br>

How It Works:<br>

Email text is cleaned and processed<br>
TF-IDF converts text into numerical features<br>
Naive Bayes model predicts phishing probability<br>
URLs are extracted and analyzed using security rules<br>
Final risk score is calculated<br>

Use Cases:<br>

Email security analysis<br>
Phishing detection systems<br>
Cybersecurity learning projects<br>
Real-time threat analysis tools<br>

Future Improvements:<br>

Add deep learning models<br>
Real-time URL reputation APIs<br>
Deploy app online<br>
Browser extension integration<br>
