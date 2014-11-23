import dfdb
import json
from flask import Flask, render_template
from flask import  request
app = Flask(__name__)

@app.route('/countryPage.html')
def countryPage():
    return render_template('countryPage.html')

@app.route('/')
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
        json_dict_list.append(json_dict)
    dfdb.db_close()
    return render_template('index.html',jsondict=json.dumps(json_dict_list))


if __name__ == '__main__':
  app.run(debug=True)
