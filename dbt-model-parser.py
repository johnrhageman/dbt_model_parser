import sqlparse
import argparse
import yaml

parser = argparse.ArgumentParser(description='Generate column spec from copiled dbt model')
parser.add_argument('--model', dest='filename', help='The path to the compiled dbt model SQL, typically in project/target/compiled/project_name folder')
parser.add_argument('--default-test', dest='default_test', help='The test to use for the default column test generation', default='None')

args = parser.parse_args()

model_name = str(args.filename.split('/')[-1]).replace('.sql', '')

with open(args.filename, 'r') as myfile:
  sql_query = myfile.read()

col_list = []
s = sqlparse.parse(sql_query)
token_list = s[0].tokens
for token in token_list:
    if isinstance(token, sqlparse.sql.IdentifierList):
        for identifier in token.get_identifiers():
           
            if(' AS ' in str(identifier)):
                split_id = str(identifier).split(' AS ')
                
                col_list.append(split_id[-1])
            elif('.' in str(identifier)):
                split_id = str(identifier).split('.')
                
                col_list.append(split_id[-1])

if args.default_test != 'None':
    x = [{"name": x, "description": "description of {}".format(x), "tests": [args.default_test]} for x in col_list]
else:
    x = [{"name": x, "description": "description of {}".format(x)} for x in col_list]
yaml_dict = {"models": {"name": model_name, "description": "description of {}".format(model_name), "columns": x}}

print(yaml.dump(yaml_dict, default_flow_style=False, sort_keys=False))