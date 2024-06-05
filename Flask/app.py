from flask import Flask,request

app=Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World'

# if __name__ == '__main__':
#     app.run()
@app.route('/submit', methods=['GET'])
def warn():
    return "<h1>Please fill up the form.</h1>"

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    choice = request.form['choice']
    return "<h1>The name of user is "+name+". And his/her choice is "+choice+".</h1>"

if __name__ == '__main__':
    app.run()