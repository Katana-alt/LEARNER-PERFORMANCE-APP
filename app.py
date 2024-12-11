from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated database
learners = []

@app.route('/')
def index():
    # Rank learners by total marks
    ranked_learners = sorted(learners, key=lambda x: x['total'], reverse=True)
    for i, learner in enumerate(ranked_learners):
        learner['rank'] = i + 1
    return render_template('index.html', learners=ranked_learners)

@app.route('/add_marks', methods=['GET', 'POST'])
def add_marks():
    if request.method == 'POST':
        name = request.form['name']
        marks = {
            'ENG': int(request.form['ENG']),
            'MATH': int(request.form['MATH']),
            'KISW': int(request.form['KISW']),
            'SCIE': int(request.form['SCIE']),
            'SST': int(request.form['SST']),
        }
        total = sum(marks.values())

        learners.append({
            'name': name,
            'marks': marks,
            'total': total
        })
        return redirect(url_for('index'))
    return render_template('add_marks.html')

if __name__ == '__main__':
    app.run(debug=False)
