from flask import Flask, jsonify
from flask import render_template

app = Flask(__name__)

JOBS = [
{
  'id': 1,
  'title': 'Data analyst',
  'location': 'Dublin, Ireland',
  'salary': ''
},
  {
  'id': 2,
  'title': 'Data scientist',
  'location': 'Dublin, Ireland',
  'salary': '€60k'
},
{
  'id': 3,
  'title': 'Front-End Engineer',
  'location': 'Hybrid',
  'salary': '€40k'
},
{
  'id': 4,
  'title': 'Back-End Engineer',
  'location': 'Remote',
  'salary': '€65k'
}
]

@app.route('/')
def index():
  return render_template('home.html', 
                         jobs=JOBS, 
                         company_name='MegaShackle')

@app.route('/api/jobs')
def jobs():
  return jsonify(JOBS)


@app.route('/learn')
def learn():
  return render_template('learn.html')


@app.route('/events')
def events():
  return render_template('events.html')


@app.route('/about')
def about():
  return render_template('about.html')


app.run(host='0.0.0.0',debug=True)