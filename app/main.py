from flask import Flask, render_template, request, redirect, url_for
from database import init_db, add_person, get_all_data, add_sample_data, reset_database
from analysis import perform_linear_regression

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'reset' in request.form:
            reset_database()
            return redirect(url_for('index'))
        else:
            name = request.form['name']
            height = float(request.form['height'])
            weight = float(request.form['weight'])
            add_person(name, height, weight)
        return redirect(url_for('results'))
    return render_template('index.html')

@app.route('/results')
def results():
    data = get_all_data()
    slope, intercept, r_squared = perform_linear_regression(data)
    return render_template('results.html', slope=slope, intercept=intercept, r_squared=r_squared, data=data)

if __name__ == '__main__':
    init_db()
    add_sample_data()
    app.run(host='0.0.0.0', port=5000, debug=True)