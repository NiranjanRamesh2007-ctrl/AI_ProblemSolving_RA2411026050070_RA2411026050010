# PROBLEM 1
# Sudoku Puzzle Solver Using CSP

An interactive, full-stack web application that solves Sudoku puzzles using **Constraint Satisfaction Problem (CSP)** techniques. This project features a modern "Glassmorphism" dark-themed UI and a recursive backtracking engine built with Python and Flask.

## 🚀 Innovative Features
- **CSP Backtracking Engine:** Uses intelligent recursive searching with constraint checking to find solutions efficiently.
- **Hybrid Interaction:** Users can play manually and "Verify Logic" to see if their current progress follows Sudoku constraints, or deploy the "AI Solver" to complete the grid instantly.
- **Glassmorphism Design:** A modern, dark-themed interface featuring neon accents, responsive input fields, and smooth CSS transitions.
- **Dynamic Feedback:** Real-time status updates (e.g., "AI is thinking...") and color-coded results (green for success, red for errors).

## 🛠️ Technology Stack
- **Frontend:** HTML5, CSS3 (Glassmorphism), JavaScript (ES6 Fetch API)
- **Backend:** Python 3.13, Flask (Web Framework)
- **AI Logic:** Constraint Satisfaction Problem (CSP) / Recursive Backtracking Algorithm

## 📂 Project Structure
```text
sudoku-ai/
├── app.py           # Main Flask application & routing
├── solver.py        # Core CSP logic (Backtracking & Validation)
├── templates/
│   └── index.html   # Modern dark-themed frontend
└── README.md        # Documentation
```

## ⚙️ Logic and CSP Approach
This project treats Sudoku as a classic **Constraint Satisfaction Problem**:
1.  **Variables:** Each empty cell ($0$) is a variable to be assigned a value.
2.  **Domains:** Each cell has a domain of integers from $\{1, \dots, 9\}$.
3.  **Constraints:**
    * **Row Constraint:** No repeating numbers in a row.
    * **Column Constraint:** No repeating numbers in a column.
    * **Subgrid Constraint:** No repeating numbers in a $3 \times 3$ grid.
4.  **Backtracking:** The algorithm picks an unassigned cell, tries a value from the domain that satisfies all constraints, and recurses. If no valid value exists, it backtracks to the previous state.

## 🏁 How to Run

### Prerequisites
- Python 3.x installed.
- Flask library installed.

### Installation & Execution
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/sudoku-ai.git
   cd sudoku-ai
   ```

2. **Install Flask:**
   ```bash
   pip install flask
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Access the Website:**
   Open your browser and navigate to `http://127.0.0.1:5000`.

## 🖥️ Preview
The interface is designed for high visibility in dark mode:
- **Neon Blue:** Indicates pre-filled numbers and grid borders.
- **Neon Green:** Indicates numbers successfully placed by the AI Solver.
- **Rose Red:** Alerts the user to invalid logic during manual play.

---
# PROBLEM 2
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

## 📝 How to Test the System
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

## 🧠 How the Model Works
The application currently uses a Logistic Regression model. Upon starting app.py, the system generates 1,000 realistic data points with the following logic:

Approved if: Credit Score > 620 AND Income > $40,000 AND Status != 'Unemployed'.

Rejected: All other conditions.

The model is then trained on this data. When a user uploads a PDF, the extracted variables are scaled using StandardScaler and encoded using LabelEncoder before being passed to the model for the final prediction.
