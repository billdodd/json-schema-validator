import getopt
import json
import jsonschema
import sys


def display_usage(program):
    print("Usage: {} -j <json-filename> -s <schema-filename>".format(program))


def open_and_load_json(filename):
    with open(filename) as json_file:
        return json.load(json_file)


def validate_json(json_data, schema_data):
    if json_data is None:
        print("JSON payload is empty", file=sys.stderr)
        return 1
    if schema_data is None:
        print("JSON schema is empty", file=sys.stderr)
        return 1
    try:
        jsonschema.validate(json_data, schema_data)
    except jsonschema.ValidationError as e:
        print("JSON validation error: {}".format(e.message), file=sys.stderr)
        return 1
    except jsonschema.SchemaError as e:
        print("JSON schema error: {}".format(e.message), file=sys.stderr)
        return 1
    else:
        print("JSON Schema validation successful.")
        return 0


def main(argv):
    """
    main
    """

    json_filename = ""
    schema_filename = ""

    try:
        opts, args = getopt.gnu_getopt(argv[1:], "j:s:", ["json=", "schema="])
    except getopt.GetoptError:
        print("Error parsing options", file=sys.stderr)
        display_usage(argv[0])
        sys.exit(1)

    if len(opts) != 2:
        display_usage(argv[0])
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-j", "--json"):
            json_filename = arg
        elif opt in ("-s", "--schema"):
            schema_filename = arg
        else:
            display_usage(argv[0])
            sys.exit(1)

    if len(args) > 0:
        print("Extra args found: {}".format(args), file=sys.stderr)
        display_usage(argv[0])
        sys.exit(1)

    if len(json_filename) == 0:
        print("JSON filename missing", file=sys.stderr)
        display_usage(argv[0])
        sys.exit(1)

    if len(schema_filename) == 0:
        print("Schema filename missing", file=sys.stderr)
        display_usage(argv[0])
        sys.exit(1)

    json_data = open_and_load_json(json_filename)
    schema_data = open_and_load_json(schema_filename)

    rc = validate_json(json_data, schema_data)

    exit(rc)


if __name__ == "__main__":
    main(sys.argv)
