import json
import subprocess
import numpy as np


file_path = 'data.json'


def fileWrite(rate):
    global file_path
    with open(file_path, 'r') as file:
        full_data = json.load(file)
    if "data" not in full_data:
        full_data["data"] = {}
    full_data["rate"] = {
        'rate': rate
    }
    with open(file_path, 'w') as file:
        json.dump(full_data, file, indent=4)
    accuracy = subprocess.run(["python3", "accuracy.py"], capture_output=True, text=True)
    accuracy = accuracy.stdout.strip()
    va = [rate, accuracy]
    return va


def fileRead():
    global file_path
    with open(file_path, 'r') as file:
        full_data = json.load(file)
    rate = full_data['rate']['rate']
    accuracy = subprocess.run(["python3", "accuracy.py"], capture_output=True, text=True)
    accuracy = accuracy.stdout.strip()
    try:
        accuracy = float(accuracy)
    except ValueError:
        print("ValueError turning prince into a fucking readable number.")
    va = [rate, accuracy]
    return va


def compute(va):
    global file_path
    while True:
        try:
            min_value = float(input("Enter min value : "))
            max_value = float(input("Enter max value : "))
            increment = float(input("Enter incrementation value : "))
            break
        except ValueError:
            print("Input must be a number")
    sequence = np.arange(min_value, max_value, increment)
    for value in sequence:
        with open(file_path, 'r') as file:
            full_data = json.load(file)
        full_data["rate"] = {
            'rate': value
        }
        with open(file_path, 'w') as file:
            json.dump(full_data, file, indent=4)
        subprocess.run(["python3", "learning.py"])
        accuracy = subprocess.run(["python3", "accuracy.py"], capture_output=True, text=True)
        accuracy = accuracy.stdout.strip()
        try:
            accuracy = float(accuracy)
        except ValueError:
            print("ValueError turning prince into a fucking readable number.")
        if accuracy < va[1]:
            va[0] = value
            va[1] = accuracy
        print(f"\r learning rate : {value:.4f} | accuracy : {accuracy} | best accuracy : {va[1]}", end="")
    with open(file_path, 'r') as file:
        full_data = json.load(file)
    full_data["rate"] = {
        'rate': va[0]
    }
    with open(file_path, 'w') as file:
        json.dump(full_data, file, indent=4)


def main():
    va = fileRead()
    compute(va)


if __name__ == "__main__":
    main()
