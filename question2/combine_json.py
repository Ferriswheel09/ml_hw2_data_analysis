import json

# List to store combined data
combined_data = []

# Read and combine the first JSON file
with open('./friends_dev.json', 'r') as file:
    data = json.load(file)
    combined_data.extend(data)

# Read and combine the second JSON file
with open('./friends_test.json', 'r') as file:
    data = json.load(file)
    combined_data.extend(data)

# Read and combine the third JSON file
with open('./friends_train.json', 'r') as file:
    data = json.load(file)
    combined_data.extend(data)

# Write the combined data to a new JSON file
with open('combined.json', 'w') as file:
    json.dump(combined_data, file, indent=4)