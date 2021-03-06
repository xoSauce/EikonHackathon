import dfdb
import json
from flask import Flask, render_template
from flask import  request
app = Flask(__name__)

@app.route('/countryPage.html')
def countryPage():
    return render_template('countryPage.html')

@app.route('/')
def startPage():
    return render_template('startPage.html')


@app.route('/map')
def index():
    dfdb.db_connect()
    values = dfdb.selectAll(''' SELECT * FROM countries ''')
    json_dict_list = []
    for entry in values:
        json_dict = {}
        json_dict['id'] = entry[0]
        json_dict['name'] = entry[1]
        json_dict['crime_index']   = entry[2]
        json_dict['pollution_index'] = entry[3]
        json_dict['natural_disaster_txt'] = entry[4]
        json_dict['natural_disaster_index'] = entry[5]
        json_dict['gdp'] = entry[6]
        json_dict['import'] = entry[7]
        json_dict['export'] = entry[8]
        json_dict['debt'] = entry[9]
        json_dict['overall_index'] = entry[10]
        json_dict_list.append(json_dict)
    dfdb.db_close()
    return render_template('index.html',jsondict=json.dumps(json_dict_list))


if __name__ == '__main__':
  app.run(debug=True)
