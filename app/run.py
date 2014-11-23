from flask import Flask
app = Flask(__name__,static_url_path='', static_folder='/frontEnd/public_html/')

@app.route('/map')
def map():
    return app.send_static_file('index.html')

@app.route('/')
def hello_world():
    return 'HelloWorld'


if __name__ == '__main__':
    app.run(debug=True,port=8080,host="0.0.0.0")