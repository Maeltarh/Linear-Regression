import json
import pandas as pd


predicted_values = {}
actual_values = {}


def calculate():
    global predicted_values, actual_values
    errors = 0
    for km, price in actual_values.items():
        predicted_price = predicted_values.get(str(km))  # Ensure key is string if necessary
        if predicted_price is not None:
            errors += (abs(predicted_price - price) / abs(price) * 100)
    errors = errors / len(actual_values.values())
#    try:
#        errors = int(errors)
#    except ValueError:
#        print("ValueError turning prince into a fucking readable number.")
#        exit()
    print(f"{errors}")


def fileRead():
    global predicted_values, actual_values
    file_path = 'data.json'
    with open(file_path, 'r') as file:
        data = json.load(file)
    predicted_values = data['data']['result']
    actual_values = data['data']['raw']
    calculate()


def main():
    fileRead()


if __name__ == "__main__":
    main()
