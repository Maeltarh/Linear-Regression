import json


mileage = 0
theta0 = 0
theta1 = 0


def calculate():
    global mileage
    global theta0, theta1
    price = theta0 + (theta1 * mileage)
    try:
        price = int(price)
    except ValueError:
        print("ValueError turning prince into a fucking readable number.")
        exit()
    if price <= 100:
        print("Please enter a mileage between 0 and 300 000. We lake the data to help you beyond those values.")
        exit()
    print(f"Price is : {price}")


def fileRead():
    global theta0, theta1
    file_path = 'data.json'
    with open(file_path, 'r') as file:
        data = json.load(file)
    theta0 = data['data']['theta0']
    theta1 = data['data']['theta1']


def main():
    global mileage
    while True:
        try:
            mileage_input = input("Please give a Mileage\n")
            mileage = int(mileage_input)
        except ValueError:
            print("Input must be a number")
        else:
            fileRead()
            calculate()
            break


if __name__ == "__main__":
    main()
