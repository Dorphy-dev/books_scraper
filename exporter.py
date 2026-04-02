import csv
import json

def export_to_csv(data, filename="books.csv"):
    keys = data[0].keys()

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

def export_to_json(data, filename="books.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
