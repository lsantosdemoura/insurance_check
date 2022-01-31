# Insurance check
API for validating the user's insurance

---
## REQUIREMENTS
- [poetry](https://python-poetry.org/docs/#installation)
- [python 3.10](https://www.python.org/downloads/)

---

## USAGE
### Run the project
```shell
git clone git@github.com:lsantosdemoura/insurance_check.git
cd insurance_check
# installing
make dependencies
# finally running
make run-api
```
### Consulting a user's insurance using curl
```shell
curl -X 'POST' \
  'http://localhost:8000/check/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "age": 29,
  "dependents": 0,
  "income": 60000,
  "marital_status": "single",
  "risk_questions": [
    false,
    true,
    false
  ],
"vehicle": {"year": 2018}
}'

{"auto":"economic","disability":"economic","home":"ineligible","life":"economic"}
```

### Run the tests
```shell
make dev-dependencies
make test
```

### Run tests with coverage
```shell
make dev-dependencies
make test-coverage
```
### Project decisions

My main goal during the development of this project was to create something that could scale easily
that's why I chose FastApi for it, easy development, good scalability and great performance.

I also wanted to make the project easy to create, remove and edit rules, so I used a pipeline to
run all of them, so to add a new one you just need to create a function on `rules.py`
put it on the list of rules, and that's it, you got a new rule
