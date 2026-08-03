from flask import Flask, request, render_template
import os

app = Flask(__name__)
name = "Fundz"  # YOUR NAME

# This makes messages save to a file
MESSAGES_FILE = "messages.txt"

@app.route('/')
def home():
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- 3. MOBILE FRIENDLY -->
        <title>{name}'s Website</title>
    </head>
    <body style="background: linear-gradient(to right, #ff9a9e, #fad0c4); font-family: Arial; margin:0;">
        
        <!-- HEADER -->
        <div style="background:white; padding:15px; box-shadow:0 2px 5px gray; position:sticky; top:0;">
            <h2 style="margin:0; color:#ff6b81; text-align:center;">{name}'s Website</h2>
        </div>
        
        <div style="text-align:center; padding:20px; max-width:800px; margin:auto;">
            <h1 style="color:blue;">Welcome to My Website!</h1>
            <p>Hello {name}! This is my first real webpage 🚀</p>
            
            <!-- BUTTON -->
            <a href="/about" style="background:white; padding:15px 30px; text-decoration:none; color:blue; border-radius:10px; font-weight:bold; display:inline-block;">
                Click Me - Go to About
            </a>
            
            <br><br>
            
            <!-- 2. YOUR PHOTO - REPLACE THIS LINK -->
            <img src="https://i.postimg.cc/qqNFcbPv/132e00e6-35d6-4786-bc1b-061bf86ae954.jpg" style="border-radius:20px; margin-top:20px; max-width:90%; height:auto;">
            <p><small>Tip: Upload your photo to imgur.com and paste the link here</small></p>
            
            <!-- CONTACT FORM -->
            <div style="background:white; max-width:400px; margin:30px auto; padding:20px; border-radius:15px; box-shadow:0 4px 10px gray;">
                <h3>Contact Me</h3>
                <form action="/submit" method="post">
                    <input name="user_name" placeholder="Your Name" style="width:90%; padding:10px; margin:8px; border-radius:5px; border:1px solid #ccc;"><br>
                    <textarea name="message" placeholder="Your Message" style="width:90%; padding:10px; margin:8px; border-radius:5px; border:1px solid #ccc; height:80px;"></textarea><br>
                    <button style="background:blue; color:white; border:none; padding:12px 25px; border-radius:8px; font-weight:bold;">Send</button>
                </form>
            </div>
        </div>
        
        <!-- FOOTER -->
        <div style="background:#333; color:white; text-align:center; padding:15px;">
            © 2026 {name}'s First Website
        </div>
    </body>
    </html>
    '''
    
@app.route('/about')
def about():
    return f'''
    <!DOCTYPE html>
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>About {name}</title>
        </head>
        <body style="background: linear-gradient(to right, #e8f5e9, #c8e6c9); font-family: Arial; margin:0;">
            
            <div style="background:white; padding:15px; box-shadow:0 2px 5px gray; text-align:center;">
                <h2 style="margin:0; color:#2e7d32;">About {name}</h2>
            </div>

            <div style="text-align:center; padding:40px; max-width:700px; margin:auto;">
                <h1 style="color:#2e7d32;">I'm Peter, also called Fundz</h1>
                <img src="fundz.jpeg" style="width:200px; height:200px; border-radius:50%; border:4px solid #2e7d32; margin:20px; object-fit:cover;">
                    I'm a web developer, writer and also a graphic designer from Lagos.
                    I build websites and love tech 💻✨
                </p>
                <br>
                <a href="/" style="background:white; padding:12px 25px; border-radius:8px; text-decoration:none; color:#2e7d32; font-weight:bold;">
                    ← Back to Home
                </a>
            </div>
        </body>
    </html>
    '''
    @app.route('/books')
def books():
    books = [
        {"title": "The Power of Mindset", "author": "Fundz", "price": "₦2,000"},
        {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "price": "₦3,500"},
        {"title": "Atomic Habits", "author": "James Clear", "price": "₦4,000"}
    ]
    return render_template('books.html', books=books)# 4. SAVE MESSAGES
@app.route('/submit', methods=['POST'])
def submit():
    user_name = request.form['user_name']
    message = request.form['message']
    
    # Save to messages.txt
    with open(MESSAGES_FILE, "a") as f:
        f.write(f"From: {user_name} | Message: {message}\n")
    
    return f'''
    <body style="background:#ffebcd; text-align:center; padding:50px;">
        <h1>Thanks {user_name}!</h1>
        <p>I got your message: "{message}"</p>
        <a href="/" style="color:blue;">← Back to Home</a>
    </body>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # host='0.0.0.0' lets phone on same wifi see it
