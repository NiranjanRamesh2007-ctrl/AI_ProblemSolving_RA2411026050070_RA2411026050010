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
