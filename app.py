from flask import Flask, redirect, url_for, request, render_template

# WSGI application
app = Flask(__name__)


@app.route('/')
def form():
    return render_template('index.html')


@app.route('/results/<int:marks>')
def results(marks):
    if marks < 50:
        result = 'FAIL'
    else:
        result = 'SUCCESS'
    return render_template('result.html', marks=marks, result=result)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        total_score = 0
        for key in request.form:
            total_score += float(request.form[key])
        average_score = total_score / len(request.form)
        return redirect(url_for('results', marks=average_score))


if __name__ == '__main__':
    app.run(debug=True)
