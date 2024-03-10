import csv
import pickle

import requests
from flask import request, Flask, render_template

app = Flask(__name__)

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()


def save_currency_rates_to_file():
    tasks = data[0]['rates']

    with open("currencies.pickle", 'wb') as f:
        pickle.dump(tasks, f)

    with open("currencies.pickle", "rb") as f:
        tasks = pickle.load(f)
    return tasks


def get_currency_codes_data():
    currency_codes = []
    for currency in data[0]['rates']:
        currency_codes.append(currency['code'])
    return currency_codes


def get_currency_bid(selected_currency_code):
    for currency in data[0]['rates']:
        if selected_currency_code == currency['code']:
            return currency['bid']


def export_items_to_csv():
    with open("currency.csv", "w", newline='', encoding='utf-8') as csvfile:
        field_names = ["currency", "code", "bid", "ask"]
        csv_writer = csv.DictWriter(csvfile, fieldnames=field_names, delimiter=';')
        csv_writer.writeheader()
        for item in save_currency_rates_to_file():
            csv_writer.writerow(item)
    print("Successfully exported data to currency.csv")


@app.route('/currency_calculator', methods=['GET', 'POST'])
def calculate():
    currencies = get_currency_codes_data()
    selected_currency = None
    result = ''

    if request.method == 'POST':
        form_data = request.form
        selected_currency = form_data.get('currency_code')
        print(selected_currency)
        value = form_data.get('value')
        new_value = int(value) * get_currency_bid(selected_currency)
        result = new_value
        print(result)
    return render_template('currency_calculator.html', currencies=currencies, selected_currency=selected_currency,
                           result=result)


export_items_to_csv()