import json
from datetime import datetime

class JsonFormatter:
    # Define date formats for conversion
    current_format = "%m/%d/%Y"  # Input date format
    target_format = "%Y-%m-%d"   # Output ISO date format

    def __init__(self, json_obj):
        """
        Initialize the JsonFormatter with the input JSON file path.

        :param json_obj: Path to the JSON file to be processed
        """
        self.json_file = json_obj

    def read_from_file(self):
        """
        Read and load JSON data from the input file.

        :return: Parsed JSON data as a Python dictionary
        """
        with open(self.json_file, mode="r", encoding="utf-8") as read_file:
            return json.load(read_file)

    def write_to_file(self, json_data, output_file):
        """
        Write the processed JSON data to an output file.

        :param json_data: The modified JSON data to be written
        :param output_file: Path to the output file
        """
        with open(output_file, mode="w", encoding="utf-8") as write_file:
            json.dump(json_data, write_file, indent=4)

    def convert_to_iso(self, json_data):
        """
        Convert the 'birth_date' field in the JSON data from the current format to ISO format ('%Y-%m-%d').

        :param json_data: JSON data containing birth dates
        :return: JSON data with 'birth_date' converted to ISO format
        """
        for item in json_data:
            try:
                # Try to parse the birth date using the current format
                date = datetime.strptime(item['birth_date'], JsonFormatter.current_format)
            except:
                # If the date is already in the target format, parse it as is
                datetime.strptime(item['birth_date'], JsonFormatter.target_format)
            else:
                # If the date is parsed successfully, convert it to ISO format
                item['birth_date'] = date.date().strftime(JsonFormatter.target_format)
        return json_data

    def remove_id(self, json_data):
        """
        Remove the 'id' field from each object in the JSON data.

        :param json_data: JSON data containing 'id' fields
        :return: JSON data with 'id' fields removed
        """
        for item in json_data:
            # Remove 'id' key if it exists
            item.pop('id', None)
        return json_data


# Example usage:
input_file = 'template.json'   # Input JSON file
output_file = 'data.json'      # Output JSON file

new_json = JsonFormatter(input_file)

new_data = new_json.read_from_file()

new_json.convert_to_iso(new_data)
new_json.write_to_file(new_data, output_file)

new_json.remove_id(new_data)
new_json.write_to_file(new_data, output_file)
