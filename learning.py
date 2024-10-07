import json
import pandas as pd


tuples_raw = ([''], [''])
tuples_data = ([''], [''])
theta0 = 0
theta1 = 0
rate = 0.001


def calc_moyenne(km):
    return sum(km) / len(km)


def calc_ecartType(km, moyenne_km):
    variance = sum((x - moyenne_km) ** 2 for x in km) / len(km)
    return variance ** 0.5


def standardiser(km):
    moyenne_km = calc_moyenne(km)
    ecart_type = calc_ecartType(km, moyenne_km)
    return [(x - moyenne_km) / ecart_type for x in km]


def destandardiser(values, std):
    moyenne = calc_moyenne(std)
    ecart_type = calc_ecartType(std, moyenne)
    return values * ecart_type + moyenne


def creatResult(km, theta0std, theta1std):
    return [(theta0std + (theta1std * km)) for km in km]


def fileWrite(km, theta0std, theta1std):
    global tuples_raw
    result = creatResult(km, theta0std, theta1std)
    tuples_result = dict(zip(km, result))
    file_path = 'data.json'
    with open(file_path, 'r') as file:
        full_data = json.load(file)
    if "data" not in full_data:
        full_data["data"] = {}
    full_data["data"] = {
        'theta0': theta0std,
        'theta1': theta1std,
        'result': tuples_result,
        'raw': tuples_raw
    }
    with open(file_path, 'w') as file:
        json.dump(full_data, file, indent=4)


def fileRead():
    global tuples_raw, rate
    file_path = 'data.csv'
    df = pd.read_csv(file_path)
    tuples_raw = dict(zip(df['km'], df['price']))
    file_path = 'data.json'
    with open(file_path, 'r') as file:
        full_data = json.load(file)
    rate = full_data['rate']['rate']


def calculateError0(mileage, realPrice):
    global theta0, theta1
    estimatePrice = theta0 + (theta1 * mileage)
    result = estimatePrice - realPrice
    return result


def calculateError1(mileage, realPrice):
    global theta0, theta1
    estimatePrice = theta0 + (theta1 * mileage)
    result = estimatePrice - realPrice
    result *= mileage
    return result


def updateTheta():
    global tuples_data, rate, theta0, theta1
    sum0 = 0
    for km, price in tuples_data.items():
        sum0 += calculateError0(km, price)
    gradient0 = sum0 / len(tuples_data)
    sum1 = 0
    for km, price in tuples_data.items():
        sum1 += calculateError1(km, price)
    gradient1 = sum1 / len(tuples_data)
    theta0 -= rate * gradient0
    theta1 -= rate * gradient1


def destandardize_theta(theta1_std, mean_km, std_km, mean_price, std_price):
    theta1 = theta1_std * (std_price / std_km)
    theta0 = mean_price - (theta1 * mean_km)
    return theta0, theta1


def main():
    global theta0, theta1, tuples_raw, tuples_data
    fileRead()
    km = list(tuples_raw.keys())
    price = list(tuples_raw.values())
    tuples_data = dict(zip(standardiser(km), standardiser(price)))
    it = 0
    while True:
        it += 1
        oldTheta0 = theta0
        oldTheta1 = theta1
        updateTheta()
        if (abs(oldTheta0 - theta0) <= 0.0001 and abs(oldTheta1 - theta1) <= 0.0001):
            break
    mean_km = calc_moyenne(km)
    std_km = calc_ecartType(km, mean_km)
    mean_price = calc_moyenne(price)
    std_price = calc_ecartType(price, mean_price)
    theta0std, theta1std = destandardize_theta(theta1, mean_km=mean_km, std_km=std_km, mean_price=mean_price, std_price=std_price)
    fileWrite(km, theta0std, theta1std)


if __name__ == "__main__":
    main()
