from flask import Flask, render_template

app = Flask(__name__)

inventors = [{
    'inventor': 'Lawrence Patrick',
    'invention': 'Crash Test Dummy',
    'invented': '1940'
    },
    {'inventor': 'Torald Sollmann',
     'invention': 'antidote for mustard gas',
     'invented': '1919'
     },
    {'inventor': 'Dr. Gordon Giesbrecht, Mr. Freeze',
     'invention': ' effective scure for hypothermia',
     'invented': '1990'
     },
    {'inventor': 'Elisha Graves',
     'invention': 'automatic braking system',
     'invented': '1853'
     },
    {'inventor': 'Louis Sebastien Lenormand}',
     'invention': 'parachute',
     'invented': '1783'
     },
    {'inventor': 'Jonas Salk',
     'invention': 'polio vaccine',
     'invented': '1952'}]


genres = ['medicine', 'engineering', 'physics', 'biology']


@app.route('/inventors')
def list_inventors():
    return render_template('flasktest.html', inventors=inventors, genres=genres)


if __name__ == '__main__':
    app.run()
