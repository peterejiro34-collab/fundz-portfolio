from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return '''
    <html>
    <head><title>Fundz Portfolio</title></head>
    <body style="font-family:Arial; text-align:center; background:linear-gradient(to bottom, #e8f5e9, #ffffff); padding:50px 20px;">
        
        <h1 style="color:#228B22; font-size:40px; margin-bottom:10px;">Welcome to Fundz Website!</h1>
        <p style="font-size:18px; color:#333;">Web Developer | Writer | Graphic Designer</p>
        <div style="text-align:center; padding:60px 20px; background:#f1f8e9;">
<img src="/static/peter.jpg" alt="Peter - Author" style="width:180px; height:180px; border-radius:50%; object-fit:cover; border:4px solid #228B22; margin-bottom:20px;">
<h2 style="color:#228B22; font-size:28px;">Meet Peter</h2>
<p style="max-width:600px; margin:0 auto; font-size:16px; line-height:1.6; color:#333;">
I'm a web developer, writer and also a graphic designer from Lagos. I build websites and love tech 💻✨
</p>
</div>
        
        <div style="margin-top:50px;">
            <a href="/books" style="background:#228B22; color:white; padding:18px 35px; border-radius:12px; text-decoration:none; margin:15px; display:inline-block; font-weight:bold; font-size:18px;">📚 My Books</a>
            
            <a href="/about" style="background:#228B22; color:white; padding:18px 35px; border-radius:12px; text-decoration:none; margin:15px; display:inline-block; font-weight:bold; font-size:18px;">👨‍💻 About Me</a>
            
            <a href="/project" style="background:#228B22; color:white; padding:18px 35px; border-radius:12px; text-decoration:none; margin:15px; display:inline-block; font-weight:bold; font-size:18px;">🚀 My Projects</a>
        </div>
        <h2 style="color:#228B22; text-align:center; margin-top:40px;">Work With Me</h2>
<form style="max-width:500px; margin:20px auto; padding:20px; background:white; border-radius:10px;">
    <input type="text" placeholder="Your Name" style="width:100%; padding:10px; margin:10px 0; border:1px solid #ccc; border-radius:5px;" required><br>
    <input type="email" placeholder="Your Email" style="width:100%; padding:10px; margin:10px 0; border:1px solid #ccc; border-radius:5px;" required><br>
    <textarea placeholder="Tell me about your project..." rows="4" style="width:100%; padding:10px; margin:10px 0; border:1px solid #ccc; border-radius:5px;" required></textarea><br>
    <button type="submit" style="width:100%; padding:12px; background:#228B22; color:white; border:none; border-radius:5px; font-size:16px; cursor:pointer;">Send Message</button>
</form>
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
