from flask import request, redirect, Flask, render_template

app = Flask(__name__)


@app.route('/mypage/me')
def information_about_me():
    if request.method == 'GET':
        print("We received GET")
        return render_template("about_me.html")

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact_me():
    if request.method == 'POST':
        message = request.form.get('message')
        print("We received POST")
        print({message})
    return render_template('contact.html')