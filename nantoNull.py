import json
import math

def convert_nan_to_null(value):
    if isinstance(value, float) and value == 'nan':
    #(math.isnan(value) or value == 'nan'):
        return None
    return value

def process_record(record):
    for key, value in record.items():
        if isinstance(value, dict):
            record[key] = process_record(value)
        elif isinstance(value, list):
            record[key] = [convert_nan_to_null(item) if isinstance(item, float) else item for item in value]
        else:
            record[key] = convert_nan_to_null(value)
    return record

# # Load JSON data
# with open('mydata.json', 'r') as json_file:
#     data = json.load(json_file)

# # Process each record in the data
# processed_data = [process_record(record) for record in data]

# # Save the processed data back to a new JSON file
# with open('mydata_processed.json', 'w') as json_file:
#     json.dump(processed_data, json_file, indent=4)

# print("Data processing complete. Saved to 'mydata_processed.json'.")
