from flask import request, redirect, Flask, render_template

app = Flask(__name__)

# @app.route('/message', methods=['GET', 'POST'])
# def message():
#    if request.method == 'GET':
#        print("We received GET")
#        return render_template("first.html")
#    elif request.method == 'POST':
#        print("We received POST")
#        print(request.form)
#        return redirect("/")

# @app.route('/greetings', methods=['GET', 'POST'])
# def greetings():
#    if request.method == 'GET':
#        print("We received GET")
#        return render_template("greetings.html")
#    elif request.method == 'POST':
#        print("We received POST")
#        print(request.form)
#        return redirect("/")

# @app.route("/warehouse")
# def warehouse():
#     items = ["screwdriver", "hammer", "saw"]
#     errors = "Błędy"
#     return render_template("warehouse.html", items=items, errors=errors)

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


