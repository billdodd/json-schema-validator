
# JSON Schema Validator

Simple python 3 program to perform JSON schema validation using the `jsonschema` package

## Prerequisites

Install jsonschema:
```
pip3 install jsonschema
```

## Syntax

```
python3 validate_json.py -j <json-filename> -s <schema-filename>
```

## Sample usage

```
$ python3 validate_json.py -j sample_json_good.json -s sample_schema.json  
JSON Schema validation successful.
```

```
$ python3 validate_json.py -j sample_json_bad.json -s sample_schema.json 
JSON validation error: 'Invalid' is not of type 'number'
```
