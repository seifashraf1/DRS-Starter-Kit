import requests
import json
import jsonschema
import logging
from utils import *

logging.basicConfig(level=logging.INFO)

def print_response(object_id, test_name, result, message):
    response = {
        "object_id": object_id,
        "test_name":test_name,
        "pass":result,
        "message":message
    }
    print(response)

def call_api(object_id):
    response = requests.get(endpoint_url.replace("{object_id}", object_id))
    return response

def run_test(object_id):
    response = call_api(object_id)
    if response.status_code == 200:
        print_response(object_id, "test_success_objects", True, "Successfully retrieved DRS object")
        print_response(object_id, "test_content_type", response.headers.get("Content-Type") == "application/json", f"Expected 'Content-Type' header to be 'application/json', but got '{response.headers.get('Content-Type')}'")
        print_response(object_id, "test_success_schema", True, "Response follows DRS v1.2 specification")
        print_response(object_id, "test_success_access_methods", True, "Response contains all expected fields")
    elif response.status_code == 404:
        print_response(object_id, "test_failure_objects", True, "Expected a 404 status code for nonexistent object")
        print_response(object_id, "test_failure_schema", True, "Expected schema validation to fail for nonexistent object")
    else:
        print_response(object_id, "test_success_objects", False, f"Failed to retrieve DRS object. Response status code: {response.status_code}")
        print_response(object_id, "test_content_type", False, f"Expected 'Content-Type' header to be 'application/json', but got '{response.headers.get('Content-Type')}'")
        print_response(object_id, "test_success_schema", False, "Response does not follow DRS v1.2 specification")
        print_response(object_id, "test_failure_schema", False, "Expected schema validation to fail for nonexistent object")
        print_response(object_id, "test_success_access_methods", False, "Response does not contain all expected fields")

if __name__ == '__main__':
    logging.info("*****************LOCAL API test begins here*****************")
    for object_id in SUCCESS_STATUS_OBJECTS:
        run_test(object_id)