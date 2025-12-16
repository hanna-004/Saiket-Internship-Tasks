import requests

def get_exchange_rate(base_currency, target_currency):
    api_key = ""  # Replace with your API key
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"

    try:
        response = requests.get(url)
        data = response.json()

        if data['result'] != 'success':
            print("Error fetching exchange rates. Please try again later.")
            return None

        rate = data['conversion_rates'].get(target_currency)
        if rate is None:
            print(f"Invalid target currency: {target_currency}")
            return None
        return rate

    except Exception as e:
        print("An error occurred:", e)
        return None

def currency_converter():
    print("=== Currency Converter ===")
    base_currency = input("Enter base currency (e.g., USD, INR, EUR): ").upper()
    target_currency = input("Enter target currency (e.g., USD, INR, EUR): ").upper()
    
    try:
        amount = float(input(f"Enter amount in {base_currency}: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        converted_amount = amount * rate
        print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")

# Run the converter
currency_converter()
