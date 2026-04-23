from flask import Flask, render_template, request, jsonify
from solver import solve_csp, is_valid
import copy

app = Flask(__name__)

# Initial "Easy" Puzzle
DEFAULT_BOARD = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

@app.route('/')
def index():
    return render_template('index.html', board=DEFAULT_BOARD)

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    board = data['board']
    solved_board = copy.deepcopy(board)
    if solve_csp(solved_board):
        return jsonify({"status": "success", "solution": solved_board})
    return jsonify({"status": "error", "message": "No solution exists"})

@app.route('/check', methods=['POST'])
def check_solution():
    data = request.json
    user_board = data['board']
    # Check if complete and valid
    for r in range(9):
        for c in range(9):
            val = user_board[r][c]
            if val == 0: return jsonify({"result": "Incomplete"})
            # Temporarily empty to check validity
            user_board[r][c] = 0
            if not is_valid(user_board, r, c, val):
                return jsonify({"result": "Try Again"})
            user_board[r][c] = val
    return jsonify({"result": "You Won!"})

if __name__ == '__main__':
    app.run(debug=True)