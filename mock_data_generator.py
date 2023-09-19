# Mock Data Generator
# Bruna Rafaella De Oliveira Neves
# September, 2023

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import random
import string


class MockDataGenerator:
    def __init__(self, data_schema: dict, num_rows: int, output_file_name: str) -> None:
        """
        Mock Data Generator is an algorithm to generate
        mocked data files based on specified schema.

        Parameters:
            data_schema (dict):
                A dictionary that specifies which data will be generated.
                The keys are the column names.
                The values are another dict, that contain:
                    type: the type of the data column
                            it can be: str, int, float, bool
                    max_length: the max length of the data
            num_rows (int): Number of rows to be generated.
            output_file_name (str): File name to be generated.

        Use case example:
            data_schema = {
                'Full Name': {'type': 'string', 'max_length': 50},
                'Nickname': {'type': 'string', 'max_length': 10},
                'Age': {'type': 'int', 'max_length': 2},
            }

            num_rows = 1000
            output_file_name = 'users.csv'

            MockDataGenerator(data_schema, num_rows, output_file_name).run()
        """
        self.data_schema = data_schema
        self.num_rows = num_rows
        self.output_file_name = output_file_name

    def run(self):
        # Opening data CSV
        with open(self.output_file_name, "w", newline="") as csvfile:
            # Write CSV header based on data_schema keys (column names)
            writer = csv.DictWriter(csvfile, fieldnames=self.data_schema.keys())
            writer.writeheader()

            for range_file in range(self.num_rows):
                # Row data dict
                row_data = {}
                for col_name, col_config in self.data_schema.items():
                    col_data_type = col_config["type"]
                    max_length = col_config["max_length"]

                    # Random strings
                    if col_data_type == "string":
                        value = "".join(
                            random.choice(string.ascii_letters)
                            for str in range(max_length)
                        )
                    # Random integers
                    elif col_data_type == "int":
                        value = random.randint(0, 10**max_length - 1)
                    # Random floats
                    elif col_data_type == "float":
                        value = round(random.uniform(0, 10**max_length), max_length)
                    # Random booleans
                    elif col_data_type == "bool":
                        value = random.choice([True, False])
                    else:
                        raise ValueError(f"Data type not suported: {col_data_type}")

                    row_data[col_name] = value

                # Writing row with data into the file
                writer.writerow(row_data)
            
            print(f"File generated: {self.output_file_name}")

############### Example to test ###############

# data_schema = {
#     "Full Name": {"type": "string", "max_length": 50},
#     "Nickname": {"type": "string", "max_length": 10},
#     "Age": {"type": "int", "max_length": 2},
# }

# num_rows = 100
# output = "dataexample.csv"

# MockDataGenerator(data_schema, num_rows, output).run()
