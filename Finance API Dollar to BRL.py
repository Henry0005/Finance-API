import requests

def convert_currency(amount, from_currency, to_currency):
    API_KEY = "3c8328e9c2e64402b63014720dbf8094"
    base_url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}"
    response = requests.get(base_url)
    data = response.json()
    exchange_rate = data["rates"][to_currency]/data["rates"][from_currency]
    return amount * exchange_rate

amount = float(input("Enter amount in USD: "))
converted_amount = convert_currency(amount, "USD", "BRL")

print(f"{amount} USD is equal to {converted_amount} BRL")
