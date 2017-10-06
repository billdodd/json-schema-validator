
# JSON Schema Validator

Simple python 3 program to perform JSON schema validation using the `jsonschema` package

## Prerequisites

Install jsonschema:
```
pip3 install jsonschema
```

## Syntax

```
usage: validate_json.py [-h] [-3 | -4] schema_filename json_filename

Validate a JSON payload against a JSON schema

positional arguments:
  schema_filename  filename of JSON schema
  json_filename    filename of JSON payload

optional arguments:
  -h, --help       show this help message and exit
  -3, --draft3     use JSON draft-3 validator
  -4, --draft4     use JSON draft-4 validator
```

## Sample usage

Validate file `sample_json_good.json` against schema `sample_schema.json` using default validator:

```
$ python3 validate_json.py sample_schema.json sample_json_good.json
JSON Schema validation successful.
```

Validate file `sample_json_good.json` against schema `sample_schema.json` using draft-3 validator:

```
$ python3 validate_json.py -3 sample_schema.json sample_json_good.json
JSON Schema validation successful.
```

Validate file `sample_json_good.json` against schema `sample_schema.json` using draft-4 validator:

```
$ python3 validate_json.py -4 sample_schema.json sample_json_good.json
JSON Schema validation successful.
```

Validate file `sample_json_bad.json` against schema `sample_schema.json` using default validator:

```
$ python3 validate_json.py sample_schema.json sample_json_bad.json
JSON validation error: 'Invalid' is not of type 'number'
```
