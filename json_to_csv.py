import json
import csv

# Function to convert JSON to CSV
def json_to_csv(json_file, csv_file):
    # Open and load the JSON data
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Open the CSV file for writing
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())

        # Write header (keys from the JSON data)
        writer.writeheader()

        # Write rows (values from each JSON entry)
        for row in data:
            writer.writerow(row)

# Example usage
json_file = 'data.json'  # Input JSON file
csv_file = 'output.csv'  # Output CSV file

json_to_csv(json_file, csv_file)
