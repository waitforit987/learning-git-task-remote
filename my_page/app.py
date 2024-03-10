import csv
import requests
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

def get_currency_codes_data():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()
    currency_codes = []
    for currency in data[0]['rates']:
        currency_codes.append(currency['code'])
    print(currency_codes)
    return currency_codes



def export_items_to_csv():
    with open("currency.csv", "w", newline='', encoding='utf-8') as csvfile:
        field_names = ["currency", "code", "bid", "ask"]
        csv_writer = csv.DictWriter(csvfile, fieldnames=field_names)
        csv_writer.writeheader()
        for item in get_currency_codes_data():
            csv_writer.writerow(item)
    print("Successfully exported data to currency.csv")

# export_items_to_csv()

@app.route('/currency_calculator', methods=['GET', 'POST'])
def calculate():
    currencies = get_currency_codes_data()
    selected_currency = None
    result = None

    if request.method == 'POST':
        data = request.form
        selected_currency = data.get('currency_code')
        # selected_currency = {'code': selected_currency_code}
        print(selected_currency)
        value = data.get('value')
        new_value = int(value) * 2
        print(new_value)

        result = new_value
    # currencies = get_json_data()
    # print(currencies)  # Dodane print statement
    return render_template('currency_calculator.html', currencies=currencies, selected_currency=selected_currency, result=result)

# def get_currency_codes_data():
# response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
# data = response.json()
# for currency in data[0]['rates']:
#     print(currency["code"])
#     if "JPY" == currency["code"]:
#         print(currency["bid"])
# print(data[0]['rates'])

    # print(data[0]['rates'][0]["bid"])










































































































































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

# @app.route('/mypage/me')
# def information_about_me():
#     if request.method == 'GET':
#         print("We received GET")
#         return render_template("about_me.html")

# @app.route('/mypage/contact', methods=['GET', 'POST'])
# def contact_me():
#     if request.method == 'POST':
#         message = request.form.get('message')
#         print("We received POST")
#         print({message})
#     return render_template('contact.html')



# UPLOAD_FOLDER = 'uploads'

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route("/images/", methods=["GET", "POST"])
# def form_view():
#     if request.method == "POST":
#         file = request.files['file']
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
#         return "File is uploaded"
#     return render_template('form.html')

# if __name__ == '__main__':
#     app.run(debug=True)