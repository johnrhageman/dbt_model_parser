## Helper script to generate column specs from compiled dbt models. 

### Usage

* Run `git clone git@github.com:johnrhageman/dbt_model_parser.git` to clone the repo
* Run `python3 -m venv venv` to create a virtual environment named venv in the folder
* Run `source venv/bin/activate` to switch to your newly created environment
* Run `pip install -r requirements.txt` to install the required libraries
* Make sure your models are compiled in your dbt project by running `dbt compile`
* Pass in the filename of a compiled model file to generate a column spec
    * Example: `python3 dbt-model-parser.py --model /Users/johnhageman/code/rigup/dbt/sample_project/target/compiled/my_new_project/example/production_user.sql`