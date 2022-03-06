from flask import Flask, render_template
from _datetime import datetime
import requests

GENDERIZE_IO = 'https://api.genderize.io?name='
AGIFY_IO = 'https://api.agify.io?name='
app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.now().strftime('%Y')
    return render_template('index.html', year=current_year)

@app.route('/guess/<string:name>')
def guess(name: str):
    # Gender API
    gender_response = requests.get(url=f'{GENDERIZE_IO}{name}')
    gender_data = gender_response.json()
    gender = gender_data['gender']

    # Age API
    age_response = requests.get(url=f'{AGIFY_IO}{name}')
    age_data = age_response.json()
    age = age_data['age']
    return render_template('guess.html', name=name, gender=gender, age=age)

if __name__ == '__main__':
    app.run()

