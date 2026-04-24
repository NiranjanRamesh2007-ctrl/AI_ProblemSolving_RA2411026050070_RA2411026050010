from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
import PyPDF2  
import re      

# Initialize the Flask application (This is the line that went missing!)
app = Flask(__name__)

# ==========================================
# 1. Train the Model on Startup
# ==========================================
np.random.seed(42)
n_samples = 1000

data = {
    'Income': np.random.randint(30000, 150000, n_samples),
    'Credit_Score': np.random.randint(300, 850, n_samples),
    'Loan_Amount': np.random.randint(5000, 80000, n_samples),
    'Employment_Status': np.random.choice(['Employed', 'Unemployed', 'Self-Employed'], n_samples)
}
train_df = pd.DataFrame(data)

loan_status = []
for index, row in train_df.iterrows():
    if row['Credit_Score'] > 620 and row['Income'] > 40000 and row['Employment_Status'] != 'Unemployed':
        loan_status.append('Approved')
    else:
        loan_status.append('Rejected')
train_df['Loan_Status'] = loan_status

encoder = LabelEncoder()
train_df['Employment_Status'] = encoder.fit_transform(train_df['Employment_Status'])

X_train = train_df.drop('Loan_Status', axis=1)
y_train = train_df['Loan_Status']

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# ==========================================
# 2. Website Routes
# ==========================================
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No file selected", 400

    if file and file.filename.endswith('.pdf'):
        try:
            # Read the PDF File
            reader = PyPDF2.PdfReader(file)
            extracted_text = ""
            for page in reader.pages:
                extracted_text += page.extract_text()
            
            # Extract data using Regular Expressions
            try:
                income = int(re.search(r'Income:\s*\$?(\d+)', extracted_text, re.IGNORECASE).group(1))
                credit = int(re.search(r'Credit(?:_|\s)Score:\s*(\d+)', extracted_text, re.IGNORECASE).group(1))
                loan = int(re.search(r'Loan(?:_|\s)Amount:\s*\$?(\d+)', extracted_text, re.IGNORECASE).group(1))
                employment = re.search(r'Employment(?:_|\s)Status:\s*([A-Za-z\-]+)', extracted_text, re.IGNORECASE).group(1)
            except AttributeError:
                return "Could not find all required fields in the PDF. Please ensure the PDF explicitly states: Income: [number], Credit Score: [number], Loan Amount: [number], Employment Status: [status]."

            # Package data
            applicant_data = pd.DataFrame({
                'Income': [income],
                'Credit_Score': [credit],
                'Loan_Amount': [loan],
                'Employment_Status': [employment]
            })

            display_df = applicant_data.copy()

            # Preprocess and Predict
            applicant_data['Employment_Status'] = encoder.transform(applicant_data['Employment_Status'])
            test_scaled = scaler.transform(applicant_data)
            
            prediction = model.predict(test_scaled)
            display_df['Prediction'] = prediction
            
            result_html = display_df.to_html(classes="result-table", index=False)
            
            return render_template('index.html', tables=[result_html])
            
        except Exception as e:
            return f"An unexpected error occurred processing the PDF: {e}"
    else:
        return "Please upload a valid .pdf file."

if __name__ == '__main__':
    app.run(debug=True)