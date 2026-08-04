from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return '''
    <html>
    <head><title>Fundz Portfolio</title></head>
    <body style="font-family:Arial; text-align:center; background:linear-gradient(to bottom, #e8f5e9, #ffffff); padding:50px 20px;">
     <nav style="background:#228B22; padding:15px; text-align:center; margin-bottom:30px;">
    <a href="/" style="color:white; text-decoration:none; margin:0 20px; font-weight:bold;">Home</a>
    <a href="/books" style="color:white; text-decoration:none; margin:0 20px; font-weight:bold;">Books</a>
    <a href="/about" style="color:white; text-decoration:none; margin:0 20px; font-weight:bold;">About Me</a>
</nav>   
        <h1 style="color:#228B22; font-size:40px; margin-bottom:10px;">Peter</h1>
<p style="font-size:18px; color:#333;">Bestselling Author & Mindset Coach</p>
        <div style="text-align:center; padding:60px 20px; background:#f1f8e9;">
<img src="/static/peter.jpg" alt="Peter - Author" style="width:180px; height:180px; border-radius:50%; object-fit:cover; border:4px solid #228B22; margin-bottom:20px;">
<h2 style="color:#228B22; font-size:28px;">Meet Peter</h2>
<div style="background:linear-gradient(135deg, #667eea 0%, #764ba2 100%); color:white; padding:40px; border-radius:12px; margin:30px auto; max-width:800px; text-align:center;">
    <h2 style="color:white; font-size:28px;">My Books Are Changing Lives</h2>
    <p style="color:white; font-size:16px;">Join thousands of readers who are transforming their mindset, healing their past, and building hope for the future.</p>
    <a href="/books" style="background:white; color:#667eea; padding:12px 24px; border-radius:6px; text-decoration:none; font-weight:bold; display:inline-block; margin-top:10px;">Browse All Books →</a>
</div>
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
    return html

@app.route('/books')
def books():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Books - Fundz</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {font-family: Arial; padding: 20px; background: #f5f5f5;}
            .book {background: white; padding: 20px; margin: 20px 0; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);}
            .book h3 {color: #228B22;}
            .book a {display: inline-block; padding: 12px 20px; background: #228B22; color: white; text-decoration: none; border-radius: 8px; margin-right: 10px;}
        </style>
    </head>
    <body>
<nav style="background:#228B22; padding:15px; text-align:center; margin-bottom:30px;">
    <a href="/" style="color:white; text-decoration:none; margin:0 20px; font-weight:bold;">Home</a>
    <a href="/books" style="color:white; text-decoration:none; margin:0 20px; font-weight:bold;">Books</a>
    <a href="/about" style="color:white; text-decoration:none; margin:0 20px; font-weight:bold;">About Me</a>
</nav>
        <h1 style="text-align:center; color:#228B22;">My Books</h1>
        
      <div class="book">
    <img src="https://i.imgur.com/I4b5EQb.jpg" style="width:150px; border-radius:8px; margin-bottom:15px; box-shadow:0 4px 8px rgba(0,0,0,0.1);">
    <h2>The Power Of Mindset & How Your Inner World Shapes Your Outer Reality</h2>
    <p>Discover how your thoughts, beliefs, and habits create your reality. Learn to reprogram negative patterns and build a mindset for growth, confidence, and success.</p>
    <a href="https://amazon.com" target="_blank" class="btn">Buy on Amazon - N13,639</a>
    <a href="https://wa.me/2347048595463?text=Hi! I want to order 'The Power Of Mindset' - N13,639" target="_blank" class="btn btn-whatsapp">Order on WhatsApp</a>
</div>

<div class="book">
    <img src="https://i.imgur.com/ef6d0sd.jpg" style="width:150px; border-radius:8px; margin-bottom:15px; box-shadow:0 4px 8px rgba(0,0,0,0.1);">
    <h2>Breaking Free From Your Past</h2>
    <p>A transformative guide to healing old wounds and reclaiming your life. Learn how childhood experiences shaped you and build a future rooted in self-worth and peace.</p>
    <a href="https://amazon.com" target="_blank" class="btn">Buy on Amazon - N81,836</a><a href="https://wa.me/2347048595463?text=Hi! I want to order 'Breaking Free From Your Past' - N81,836" target="_blank" class="btn btn-whatsapp">
</div>

<div class="book">
    <img src="https://i.imgur.com/p3QVRBI.jpg" style="width:150px; border-radius:8px; margin-bottom:15px; box-shadow:0 4px 8px rgba(0,0,0,0.1);">
    <h2>The Last Hope</h2>
    <p>In a dying world, one hero must find a legendary artifact to save humanity. A sci-fi adventure about teamwork, sacrifice, and hope shining brightest in dark times.</p>
    <a href="https://amazon.com" target="_blank" class="btn">Buy on Amazon - N10,912</a>
    <a href="https://wa.me/2347048595463?text=Hi! I want to order 'The Last Hope' - N10,912" target="_blank" class="btn btn-whatsapp">Order on WhatsApp</a>
</div>
        
        <div style="text-align:center; margin-top:30px;">
            <a href="/" style="background:#666;">← Back to Home</a>
        </div>
    </body>
    </html>
    '''
    return html
@app.route('/about')
def about():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>About Peter</title>
        <style>
            body { font-family: Arial; background: #f8f5e9; padding: 40px 20px; max-width: 800px; margin: 0 auto; line-height: 1.8; }
            h1 { color: #228B22; text-align: center; font-size: 36px; }
            .bio { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
            img { width: 200px; height: 200px; border-radius: 50%; display: block; margin: 0 auto 20px; border: 4px solid #228B22; }
            .btn { background: #228B22; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; display: inline-block; margin-top: 20px; }
        </style>
    </head>
    <body>
        <h1>About Peter</h1>
        <div class="bio">
            <img src="/static/peter.jpg" alt="Peter">
            <h2 style="text-align:center; color:#333;">Author | Web Developer | Mindset Coach</h2>
            
            <p>Hi, I'm Peter. I'm a writer from Lagos, Nigeria with a passion for helping people transform their lives through books, mindset, and technology.</p>
            
            <p>I wrote <b>The Power Of Mindset</b> to help people break limiting beliefs. 
            <b>Breaking Free From Your Past</b> to help people heal. 
            And <b>The Last Hope</b> to give people hope for the future.</p>
            
            <p>When I'm not writing, I'm building websites, designing graphics, and drinking way too much coffee ☕</p>
            
            <p><b>My Mission:</b> To inspire 1 million people to believe in themselves and take action.</p>
            
            <div style="text-align:center;">
                <a href="/books" class="btn">Read My Books</a>
            </div>
        </div>
    </body>
    </html>
    '''
    return html
@app.route('/projects')
def projects():
    html = '''
    <!DOCTYPE html>
    <html>
    <head><title>Projects - Peter</title></head>
    <body style="font-family:Arial; padding:40px; background:#f8f8f8;">
        <nav style="background:#228B22; padding:15px; text-align:center; margin-bottom:30px;">
            <a href="/" style="color:white; text-decoration:none; margin:0 20px; font-weight:bold;">Home</a>
            <a href="/books" style="color:white; text-decoration:none; margin:0 20px; font-weight:bold;">Books</a>
            <a href="/about" style="color:white; text-decoration:none; margin:0 20px; font-weight:bold;">About Me</a>
            <a href="/projects" style="color:white; text-decoration:none; margin:0 20px; font-weight:bold;">Projects</a>
        </nav>
        
        <h1 style="text-align:center; color:#228B22;">My Projects</h1>
        <div style="max-width:800px; margin:0 auto; text-align:center;">
            <p>Coming Soon! 🚀</p>
            <p>I'm building websites, designing graphics, and creating tools to help people.</p>
        </div>
    </body>
    </html>
    '''
    return html
