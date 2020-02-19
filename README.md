## Helper script to generate column specs from compiled dbt models. 

### Usage

* Run `git clone git@github.com:johnrhageman/dbt_model_parser.git` to clone the repo
* Run `python3 -m venv venv` to create a virtual environment named venv in the folder
* Run `source venv/bin/activate` to switch to your newly created environment
* Run `pip install -r requirements.txt` to install the required libraries
* Make sure your models are compiled in your dbt project by running `dbt compile`
* Pass in the filename of a compiled model file to generate a column spec and a default test to create if needed
    * Example with a test: `python3 dbt-model-parser.py --model /Users/johnhageman/code/rigup/dbt/sample_project/target/compiled/my_new_project/example/production_user.sql --default-test unique`
    * Example Output: 
```yaml
models:
  name: production_user
  description: description of production_user
  columns:
  - name: activated_at
    description: description of activated_at
    tests:
    - unique
  - name: availability_status
    description: description of availability_status
    tests:
    - unique
  - name: city
    description: description of city
    tests:
    - unique
  - name: company_class
    description: description of company_class
    tests:
    - unique
  - name: company_id
    description: description of company_id
    tests:
    - unique
  - name: company_name
    description: description of company_name
    tests:
    - unique
  - name: company_native_id
    description: description of company_native_id
    tests:
    - unique
  - name: country
    description: description of country
    tests:
    - unique
  - name: created_at
    description: description of created_at
    tests:
    - unique
  - name: current_sign_in_at
    description: description of current_sign_in_at
    tests:
    - unique
  - name: date_of_birth
    description: description of date_of_birth
    tests:
    - unique
  - name: eligibility_status
    description: description of eligibility_status
    tests:
    - unique
  - name: email
    description: description of email
    tests:
    - unique
  - name: headline
    description: description of headline
    tests:
    - unique
  - name: id
    description: description of id
    tests:
    - unique
  - name: initial_use_case
    description: description of initial_use_case
    tests:
    - unique
  - name: introduced_by
    description: description of introduced_by
    tests:
    - unique
  - name: introduced_through
    description: description of introduced_through
    tests:
    - unique
  - name: is_rigup
    description: description of is_rigup
    tests:
    - unique
  - name: origin
    description: description of origin
    tests:
    - unique
  - name: last_active_date
    description: description of last_active_date
    tests:
    - unique
  - name: last_sign_in_at
    description: description of last_sign_in_at
    tests:
    - unique
  - name: linkedin_url
    description: description of linkedin_url
    tests:
    - unique
  - name: marketplace_status
    description: description of marketplace_status
    tests:
    - unique
  - name: name
    description: description of name
    tests:
    - unique
  - name: office_phone
    description: description of office_phone
    tests:
    - unique
  - name: onboarding_status
    description: description of onboarding_status
    tests:
    - unique
  - name: operational_role
    description: description of operational_role
    tests:
    - unique
  - name: origin
    description: description of origin
    tests:
    - unique
  - name: phone
    description: description of phone
    tests:
    - unique
  - name: profile_id
    description: description of profile_id
    tests:
    - unique
  - name: profile_status
    description: description of profile_status
    tests:
    - unique
  - name: referral_code
    description: description of referral_code
    tests:
    - unique
  - name: role
    description: description of role
    tests:
    - unique
  - name: rua_description
    description: description of rua_description
    tests:
    - unique
  - name: sign_in_count
    description: description of sign_in_count
    tests:
    - unique
  - name: source
    description: description of source
    tests:
    - unique
  - name: state
    description: description of state
    tests:
    - unique
  - name: status
    description: description of status
    tests:
    - unique
  - name: street_address
    description: description of street_address
    tests:
    - unique
  - name: user_class
    description: description of user_class
    tests:
    - unique
  - name: zipcode
    description: description of zipcode
    tests:
    - unique
```
    * Example without a test: `python3 dbt-model-parser.py --model /Users/johnhageman/code/rigup/dbt/sample_project/target/compiled/my_new_project/example/production_user.sql`
```yaml
models:
  name: production_user
  description: description of production_user
  columns:
  - name: activated_at
    description: description of activated_at
  - name: availability_status
    description: description of availability_status
  - name: city
    description: description of city
  - name: company_class
    description: description of company_class
  - name: company_id
    description: description of company_id
  - name: company_name
    description: description of company_name
  - name: company_native_id
    description: description of company_native_id
  - name: country
    description: description of country
  - name: created_at
    description: description of created_at
  - name: current_sign_in_at
    description: description of current_sign_in_at
  - name: date_of_birth
    description: description of date_of_birth
  - name: eligibility_status
    description: description of eligibility_status
  - name: email
    description: description of email
  - name: headline
    description: description of headline
  - name: id
    description: description of id
  - name: initial_use_case
    description: description of initial_use_case
  - name: introduced_by
    description: description of introduced_by
  - name: introduced_through
    description: description of introduced_through
  - name: is_rigup
    description: description of is_rigup
  - name: origin
    description: description of origin
  - name: last_active_date
    description: description of last_active_date
  - name: last_sign_in_at
    description: description of last_sign_in_at
  - name: linkedin_url
    description: description of linkedin_url
  - name: marketplace_status
    description: description of marketplace_status
  - name: name
    description: description of name
  - name: office_phone
    description: description of office_phone
  - name: onboarding_status
    description: description of onboarding_status
  - name: operational_role
    description: description of operational_role
  - name: origin
    description: description of origin
  - name: phone
    description: description of phone
  - name: profile_id
    description: description of profile_id
  - name: profile_status
    description: description of profile_status
  - name: referral_code
    description: description of referral_code
  - name: role
    description: description of role
  - name: rua_description
    description: description of rua_description
  - name: sign_in_count
    description: description of sign_in_count
  - name: source
    description: description of source
  - name: state
    description: description of state
  - name: status
    description: description of status
  - name: street_address
    description: description of street_address
  - name: user_class
    description: description of user_class
  - name: zipcode
    description: description of zipcode
```