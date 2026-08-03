from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1 style='text-align:center; font-family:Arial; color:#228B22; padding-top:50px;'>Welcome to Fundz Website! <br><a href='/books'>My Books</a> | <a href='/about'>About</a> | <a href='/project'>Projects</a></h1>"

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project')
def project():
    return render_template('project.html')

if __name__ == '__main__':
    app.run(debug=True)
