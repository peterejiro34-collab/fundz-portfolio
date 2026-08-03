from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head><title>Fundz Portfolio</title></head>
    <body style="font-family:Arial; text-align:center; background:linear-gradient(to bottom, #e8f5e9, #ffffff); padding:50px 20px;">
        
        <h1 style="color:#228B22; font-size:40px; margin-bottom:10px;">Welcome to Fundz Website!</h1>
        <p style="font-size:18px; color:#333;">Web Developer | Writer | Graphic Designer</p>
        
        <div style="margin-top:50px;">
            <a href="/books" style="background:#228B22; color:white; padding:18px 35px; border-radius:12px; text-decoration:none; margin:15px; display:inline-block; font-weight:bold; font-size:18px;">📚 My Books</a>
            
            <a href="/about" style="background:#228B22; color:white; padding:18px 35px; border-radius:12px; text-decoration:none; margin:15px; display:inline-block; font-weight:bold; font-size:18px;">👨‍💻 About Me</a>
            
            <a href="/project" style="background:#228B22; color:white; padding:18px 35px; border-radius:12px; text-decoration:none; margin:15px; display:inline-block; font-weight:bold; font-size:18px;">🚀 My Projects</a>
        </div>
        
        <div style="margin-top:60px; padding:20px; background:#f5f5f5;">
            <p style="color:#666;">© 2026 Fundz. All rights reserved.</p>
        </div>
    </body>
    </html>
    '''

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project')
def project():
    return render_template('project.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
