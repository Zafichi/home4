import json
import csv


def json_to_csv(json_path, csv_path):
    with open(json_path, 'r') as json_file:
        json_str = json_file.read()
        data = json.loads(json_str)

    fields_name = []
    for row in data:
        for key in row:
            if key not in fields_name:
                fields_name.append(key)

    with open(csv_path, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fields_name)
        writer.writeheader()
        writer.writerows(data)


path_to_json = 'json_file.json'
path_to_csv = 'csv_fle.csv'
json_to_csv(path_to_json, path_to_csv)
