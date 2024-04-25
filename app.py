from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
}, {
    'id': 5,
    'title': 'Python Developer',
    'location': 'Pune, India',
    'salary': 'Rs. 8,00,000'
}]

Cources = [{
    'course_name': 'Data Science',
    'course_code': 'DS',
    'course_fees': 'Rs. 40,000'
}, {
    'course_name': 'Python',
    'course_code': 'PY',
    'course_fees': 'Rs. 22,000'
}, {
    'course_name': 'Machine Learning',
    'course_code': 'ML',
    'course_fees': 'Rs. 30,000'
}]


@app.route("/")
def hello():
  return render_template('home.html', jobs=JOBS, company_name='SS')


# @app.route("/jobs")
# def list_jobs():
#   return jsonify(JOBS)


@app.route("/cources")
def cource():
  return render_template('cources.html', cources=Cources)


if __name__ == "__main__":
  app.run(debug=True)
