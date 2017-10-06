import argparse
import json
import jsonschema
import sys


def open_and_load_json(filename):
    """
    Open a JSON file, load it and return the JSON object as a dict
    :param filename: JSON filename
    :return: JSON object as a dict
    """
    with open(filename) as json_file:
        return json.load(json_file)


def validate_json(validator, json_data, schema_data):
    """
    Validate a JSON data payload against a JSON schema
    :param validator: jsonschema validation method to use
    :param json_data: JSON data payload to validate
    :param schema_data: JSON schema to validate against
    :return: 0 for success, 1 for failure
    """
    if json_data is None:
        print("JSON payload is empty", file=sys.stderr)
        return 1
    if schema_data is None:
        print("JSON schema is empty", file=sys.stderr)
        return 1
    try:
        validator(json_data, schema_data)
    except jsonschema.ValidationError as e:
        print("JSON validation error: {}".format(e.message), file=sys.stderr)
        return 1
    except jsonschema.SchemaError as e:
        print("JSON schema error: {}".format(e.message), file=sys.stderr)
        return 1
    else:
        print("JSON Schema validation successful.")
        return 0


def main():
    """
    main
    """

    parser = argparse.ArgumentParser(description='Validate a JSON payload against a JSON schema')
    parser.add_argument('schema_filename', help='filename of JSON schema')
    parser.add_argument('json_filename', help='filename of JSON payload')
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument('-3', '--draft3', action='store_true', help='use JSON draft-3 validator')
    group1.add_argument('-4', '--draft4', action='store_true', help='use JSON draft-4 validator')

    args = parser.parse_args()

    if args.draft3:
        validator = jsonschema.Draft3Validator
    elif args.draft4:
        validator = jsonschema.Draft4Validator
    else:
        validator = jsonschema.validate

    json_data = open_and_load_json(args.json_filename)
    schema_data = open_and_load_json(args.schema_filename)

    rc = validate_json(validator, json_data, schema_data)

    exit(rc)


if __name__ == "__main__":
    main()
