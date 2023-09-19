# Mock Data Generator
Mock Data Generator is a Python algorithm designed to create mock data files based on a specified data schema. This is useful when you need to create mocked data for testing, for example.

## Usage
You can use the Mock Data Generator by providing a data schema, the number of rows to be generated, and the output file name. 
Here's an example:
```
data_schema = {
    'Full Name': {'type': 'string', 'max_length': 50},
    'Nickname': {'type': 'string', 'max_length': 10},
    'Age': {'type': 'int', 'max_length': 2},
}

num_rows = 1000
output_file_name = 'users.csv'

MockDataGenerator(data_schema, num_rows, output_file_name).run()
```
Here, we are generating a CSV file named 'users.csv' with 1000 data rows.
The data schema is requesting three columns: 'Full Name' (string of up to 50 characters), 'Nickname' (string of up to 10 characters), and 'Age' (integer with up to 2 digits).

## Constructor Parameters
data_schema (dict): A dictionary with the data columns to be created into the data file. 
The keys are column names, and the values are other dictionaries containing:  
  type: the data type of the column (can be 'string', 'int', 'float', or 'bool').  
  max_length: the maximum length of the column.  
  num_rows (int): The number of data rows to be generated in the file.  

output_file_name (str): Name of the output file that will contain the generated data.

## Generating Data
The run() method is responsible for generating the data based on the specified schema. It creates a CSV file with a column header corresponding to the schema and fills the rows with fictional data following the schema specifications.

## Data Type Support
The Mock Data Generator supports four data types:  

string: Strings based on the specified maximum length.  
int: Integer numbers within a range compatible with the maximum length.  
float: Random floating-point numbers within a range compatible with the maximum length.  
bool: Random boolean values (True or False).

## Author
Bruna Rafaella De Oliveira Neves, September 2023.
