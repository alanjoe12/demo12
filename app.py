from flask import Flask, render_template, request,jsonify


app = Flask(__name__)



@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def Home():
    return render_template('index.html')


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()