from flask import Flask, render_template 

# create Flask creating 
app = Flask(__name__)

# create Flask route 
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)



# create custom Error pages 
# Invalid URL 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=404)

# Internal Server Error
@app.errorhandler(500)
def internal_server(e):
    return render_template('500.html', error=500)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)