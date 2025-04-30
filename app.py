from flask import Flask, render_template

app = Flask(__name__)

# Example static board (0 = empty)
example_board = [
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
    indexed_board = [
        [{'row': r, 'col': c, 'value': val} for c, val in enumerate(row)]
        for r, row in enumerate(example_board)
    ]
    return render_template('index.html', board=indexed_board)
 
if __name__ == '__main__':
    app.run(debug=True)