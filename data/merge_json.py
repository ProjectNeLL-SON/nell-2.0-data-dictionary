import os
import json

def merge_json_files_in_directory(directory_path):
    merged_data = {}
    
    # 1. List all the JSON files in the directory
    json_files = [f for f in os.listdir(directory_path) if f.endswith('.json')]
    
    for json_file in json_files:
        with open(os.path.join(directory_path, json_file), 'r') as file:
            # 2. Open each file, read its contents, and parse it as JSON
            data = json.load(file)
            
            # 3. Merge the parsed JSON data
            merged_data.update(data)
            
    return merged_data

# Merge JSON files from a specific directory
merged_data = merge_json_files_in_directory('data/json')

# 4. (Optional) Write the merged JSON data to a new file
with open('data/data.json', 'w') as output_file:
    json.dump(merged_data, output_file, indent=4)
