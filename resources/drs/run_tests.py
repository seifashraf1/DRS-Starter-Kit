import requests
import json
import jsonschema
import logging
import sys
from utils import *
from test_endpoints import *

level = logging.DEBUG
log = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('%(message)s'))
handler.setLevel(level)
log.addHandler(handler)
log.setLevel(level)

class style:
    reset = 0
    bold = 1
    dim = 2
    italic = 3
    underline = 4
    blink = 5
    rblink = 6
    reversed = 7
    conceal = 8
    crossed = 9

class fg:
    black = 30
    red = 31
    green = 32
    yellow = 33
    blue = 34
    magenta = 35
    cyan = 36
    gray = 37
    reset = 39

def color(value):
    return "\033[" + str(int(value)) + "m"

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

def run_tests(object_id):
    successful_requests = 0
    response = call_api(object_id)
    response_body = response.json()
    if response.status_code == 200:
        print_response(object_id, "test_successful_request", True, "Successfully retrieved DRS object")
        successful_requests+=1
    else:
        print_response(object_id, "test_successful_request", False, f"Failed to retrieve DRS object. Response status code: {response.status_code}")

    if response.headers.get("Content-Type")=="application/json":
        print_response(object_id, "test_content_type", response.headers.get("Content-Type") == "application/json", f"Expected 'Content-Type' header to be 'application/json', and got '{response.headers.get('Content-Type')}'")
        successful_requests+=1
    else:
        print_response(object_id, "test_content_type", False, f"Expected 'Content-Type' header to be 'application/json', but got '{response.headers.get('Content-Type')}'")

    if response_body['self_uri'].split("/")[3] == object_id and response.status_code == 200:      
        print_response(object_id, "test_success_schema", True, "DRS object ID matches the ID in the response")
        successful_requests+=1
    else:
        print_response(object_id, "test_success_schema", False, "DRS object ID does not match the ID in the response")

    if all(key in response.json() for key in ("access_methods", "checksums", "created_time", "description", "id", "mime_type", "name", "size", "updated_time", "version")):    
        print_response(object_id, "test_success_access_methods", True, "Response contains all expected fields")
        successful_requests+=1
    else:
        print_response(object_id, "test_success_access_methods", False, "Response does not contain all expected fields")

    return successful_requests

if __name__ == '__main__':
    passed_tests = 0
    for object_id in SUCCESS_STATUS_OBJECTS:
        passed_tests+=run_tests(object_id)
    
    #log.info the number of passed_tests and failed_tests
    log.info(f"{(color(fg.green) + color(style.bold))}PASSED TESTS: {passed_tests}")
    log.info(f"{(color(fg.red) + color(style.bold))}FAILED TESTS: {8- passed_tests}")

    if passed_tests == 8:
        log.info(f"{(color(fg.green) + color(style.bold))}ALL TESTS PASSED"
                f"{color(fg.reset) + color(style.reset)}")
    else:
        log.info(f"{(color(fg.red) + color(style.bold))}SOME TESTS FAILED"
                f"{color(fg.reset) + color(style.reset)}")
