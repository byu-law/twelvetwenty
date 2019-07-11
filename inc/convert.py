# All of the modules used in the "static" Python class
import csv
import json

"""
    Private Methods
"""

# Method used to validate an object as JSON data
def __is_data_valid_json(data):
    try:
        json.loads(data)

    except ValueError:
        return False

    else:
        return True


"""
    Public Methods
"""

# Method used to convert a CSV file into JSON
def csv_to_json(filename):
    data = []

    with open(filename) as file:
        for row in csv.DictReader(file):
            temp = {}
            for key in row.keys():
                if __is_data_valid_json(row[key]):
                    temp[key] = json.loads(row[key])

                else:
                    temp[key] = row[key]

            data.append(temp)

    return data
