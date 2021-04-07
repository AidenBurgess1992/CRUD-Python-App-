import csv


def read_data(filename):
    data = []
    with open(filename) as the_file:
        for line in the_file.readlines():
            data.append(line.strip())
    return data


def write_data(filename, data):
    with open(filename, mode="w") as the_file:
        for row in data:
            the_file.write(f"{row}\n")


def read_csv_data(filename):
    data = []
    with open(filename) as the_file:
        reader = csv.DictReader(the_file)
        for line in reader:
            data.append(line)
    return data


def write_csv_data(filename, data):
    with open(filename, mode="w", newline="\n") as the_file:
        writer = csv.DictWriter(the_file, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def save(data):
    write_csv_data("./data/products.csv", data)
    write_csv_data("./data/orders.csv", data)
    write_csv_data("./data/couriers.csv", data)
