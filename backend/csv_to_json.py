import csv,json

def CSV_TO_JSON(csv_path, json_path): 
    data = []
    with open(csv_path) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
            temp = {}
            temp['Class'] = rows['Class']
            temp['Section'] = rows['Section']
            temp['Type'] = rows['Type']
            data.append(temp)

    with open(json_path, 'w') as jsonFile:
        jsonFile.write(json.dumps(data, indent = 4))

