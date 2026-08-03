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
<a href="/books" style="background:#228B22; color:white; padding:18px 35px; border-radius:12px; text-decoration:none; margin:15px; display:inline-block;">My Books</a>
<a href="/about" style="background:#228B22; color:white; padding:18px 35px; border-radius:12px; text-decoration:none; margin:15px; display:inline-block;">About Me</a>
<a href="/project" style="background:#228B22; color:white; padding:18px 35px; border-radius:12px; text-decoration:none; margin:15px; display:inline-block;">My Projects</a>
        </div>
        <h2 style="color:#228B22; text-align:center; margin-top:40px;">Work With Me</h2>
<form action="https://wa.me/2347048595463?text=Hi Peter, I'm interested in working with you" method="get" target="_blank" style="max-width:500px; margin:20px auto; padding:20px; background:white; border-radius:10px;">
    <input name="name" type="text" placeholder="Your Name" style="width:100%; padding:10px; margin:10px 0; border:1px solid #ccc; border-radius:5px;" required><br>
    <input name="email" type="email" placeholder="Your Email" style="width:100%; padding:10px; margin:10px 0; border:1px solid #ccc; border-radius:5px;" required><br>
    <textarea name="message" placeholder="Tell me about your project..." rows="4" style="width:100%; padding:10px; margin:10px 0; border:1px solid #ccc; border-radius:5px;" required></textarea><br>
    <button type="submit" style="width:100%; padding:12px; background:#228B22; color:white; border:none; border-radius:5px; font-size:16px; cursor:pointer;">Send Message via WhatsApp</button>
</form>
        <div style="margin-top:60px; padding:20px; background:#f5f5f5;">
            <p style="color:#666;">© 2026 Fundz. All rights reserved.</p>
        </div>
    </body>
    </html>
    '''
@app.route('/books')

def books():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Books - Fundz</title>
    </head>
    <body style="font-family:Arial; background:#f0fff0; margin:0; padding:20px;">
        <h1 style="color:#228B22; text-align:center;">My Books</h1>
        
        <div style="max-width:800px; margin:40px auto;">
            
            <div style="background:white; padding:20px; margin:20px 0; border-radius:10px; box-shadow:0 2px 5px rgba(0,0,0,0.1);">
                <h3 style="color:#228B22;">Book Title 1</h3>
                <p>Short description of your book. What will they learn?</p>
                <a href="https://your-gumroad-link.com" target="_blank" style="background:#228B22; color:white; padding:10px 20px; text-decoration:none; border-radius:5px; display:inline-block;">Buy Now - ₦2000</a>
            </div>

            <div style="background:white; padding:20px; margin:20px 0; border-radius:10px; box-shadow:0 2px 5px rgba(0,0,0,0.1);">
                <h3 style="color:#228B22;">Book Title 2</h3>
                <p>Short description of your book.</p>
                <a href="https://your-amazon-link.com" target="_blank" style="background:#228B22; color:white; padding:10px 20px; text-decoration:none; border-radius:5px; display:inline-block;">Buy Now - ₦3500</a>
            </div>

        </div>

        <div style="text-align:center; margin-top:40px;">
            <a href="/" style="color:#228B22;">← Back to Home</a>
        </div>

    </body>
    </html>
    '''
    return html
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
