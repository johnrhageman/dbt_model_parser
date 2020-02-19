## Helper script to generate column specs from compiled dbt models. 

### Usage

* Run `git clone git@github.com:johnrhageman/dbt_model_parser.git` to clone the repo
* Run `python3 -m venv venv` to create a virtual environment named venv in the folder
* Run `source venv/bin/activate` to switch to your newly created environment
* Run `pip install -r requirements.txt` to install the required libraries
* Make sure your models are compiled in your dbt project by running `dbt compile`
* Pass in the filename of a compiled model file to generate a column spec
    * Example: `python3 dbt-model-parser.py --model /Users/johnhageman/code/rigup/dbt/sample_project/target/compiled/my_new_project/example/production_user.sql`
    * Example Output: 
    
```yaml
models:
  name: production_user
  description: description of production_user
  columns:
  - name: activated_at
    description: description of activated_at
    tests:
    - not_null
  - name: availability_status
    description: description of availability_status
    tests:
    - not_null
  - name: city
    description: description of city
    tests:
    - not_null
  - name: company_class
    description: description of company_class
    tests:
    - not_null
  - name: company_id
    description: description of company_id
    tests:
    - not_null
  - name: company_name
    description: description of company_name
    tests:
    - not_null
  - name: company_native_id
    description: description of company_native_id
    tests:
    - not_null
  - name: country
    description: description of country
    tests:
    - not_null
  - name: created_at
    description: description of created_at
    tests:
    - not_null
  - name: current_sign_in_at
    description: description of current_sign_in_at
    tests:
    - not_null
  - name: date_of_birth
    description: description of date_of_birth
    tests:
    - not_null
  - name: eligibility_status
    description: description of eligibility_status
    tests:
    - not_null
  - name: email
    description: description of email
    tests:
    - not_null
  - name: headline
    description: description of headline
    tests:
    - not_null
  - name: id
    description: description of id
    tests:
    - not_null
  - name: initial_use_case
    description: description of initial_use_case
    tests:
    - not_null
  - name: introduced_by
    description: description of introduced_by
    tests:
    - not_null
  - name: introduced_through
    description: description of introduced_through
    tests:
    - not_null
  - name: is_rigup
    description: description of is_rigup
    tests:
    - not_null
  - name: origin
    description: description of origin
    tests:
    - not_null
  - name: last_active_date
    description: description of last_active_date
    tests:
    - not_null
  - name: last_sign_in_at
    description: description of last_sign_in_at
    tests:
    - not_null
  - name: linkedin_url
    description: description of linkedin_url
    tests:
    - not_null
  - name: marketplace_status
    description: description of marketplace_status
    tests:
    - not_null
  - name: name
    description: description of name
    tests:
    - not_null
  - name: office_phone
    description: description of office_phone
    tests:
    - not_null
  - name: onboarding_status
    description: description of onboarding_status
    tests:
    - not_null
  - name: operational_role
    description: description of operational_role
    tests:
    - not_null
  - name: origin
    description: description of origin
    tests:
    - not_null
  - name: phone
    description: description of phone
    tests:
    - not_null
  - name: profile_id
    description: description of profile_id
    tests:
    - not_null
  - name: profile_status
    description: description of profile_status
    tests:
    - not_null
  - name: referral_code
    description: description of referral_code
    tests:
    - not_null
  - name: role
    description: description of role
    tests:
    - not_null
  - name: rua_description
    description: description of rua_description
    tests:
    - not_null
  - name: sign_in_count
    description: description of sign_in_count
    tests:
    - not_null
  - name: source
    description: description of source
    tests:
    - not_null
  - name: state
    description: description of state
    tests:
    - not_null
  - name: status
    description: description of status
    tests:
    - not_null
  - name: street_address
    description: description of street_address
    tests:
    - not_null
  - name: user_class
    description: description of user_class
    tests:
    - not_null
  - name: zipcode
    description: description of zipcode
    tests:
    - not_null
```
