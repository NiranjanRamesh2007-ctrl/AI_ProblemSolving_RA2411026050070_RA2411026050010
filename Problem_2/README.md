# AI Loan Approval System 🏦🤖

A web-based machine learning application that predicts whether a user's loan application will be approved or rejected. Users can upload a PDF containing their financial details, and the system will extract the text, process the variables, and return an instant prediction.

## 🌟 Features
* **PDF Data Extraction:** Automatically reads and extracts specific applicant details from uploaded `.pdf` documents using `PyPDF2` and Regular Expressions.
* **Machine Learning Prediction:** Uses a Logistic Regression classification model (via `scikit-learn`) trained on 1,000 synthetic realistic data points.
* **Clean Web Interface:** A lightweight, user-friendly HTML/CSS frontend served by Flask.
* **Instant Processing:** Preprocesses the data (scaling and encoding) on the fly to match the training environment and displays the result instantly.

## 🛠️ Tech Stack
* **Backend:** Python, Flask
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Data Processing:** PyPDF2, Regex (re)
* **Frontend:** HTML5, CSS3

## 📂 Project Structure
```text
Loan_App/
│
├── app.py                # The main Python Flask server and ML logic
├── README.md             # Project documentation
└── templates/
    └── index.html        # The frontend user interface
```
## 🚀 Installation & Setup
1. Prerequisites
You must have Python installed on your system. You can download it from python.org.

2. Install Dependencies
Open your terminal, navigate to the project folder, and run the following command to install the required Python libraries:

Bash
python -m pip install flask pandas scikit-learn pypdf2
3. Run the Application
Start the Flask development server:

Bash
python app.py
Once the server is running, open your web browser and navigate to: http://127.0.0.1:5000

##📝 How to Test the System
Because the application uses Regular Expressions to scrape unstructured PDF data, the uploaded PDF must contain text in a specific format.

To test the application, create a Word Document, Google Doc, or Text File, copy the text below, and Save/Export it as a .pdf:

Plaintext
Loan Application Form

Applicant Name: John Doe
Income: 85000
Credit Score: 720
Loan Amount: 20000
Employment Status: Employed
(Note: Employment Status must be exactly Employed, Unemployed, or Self-Employed).

Upload this newly created PDF via the web interface to view the prediction!

##🧠 How the Model Works
The application currently uses a Logistic Regression model. Upon starting app.py, the system generates 1,000 realistic data points with the following logic:

Approved if: Credit Score > 620 AND Income > $40,000 AND Status != 'Unemployed'.

Rejected: All other conditions.

The model is then trained on this data. When a user uploads a PDF, the extracted variables are scaled using StandardScaler and encoded using LabelEncoder before being passed to the model for the final prediction.
