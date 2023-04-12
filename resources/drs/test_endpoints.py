#import all packages and modules to make requests and test 
import requests
import json
import unittest
import jsonschema
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from utils import *

class TestEndpoints(unittest.TestCase):  
    
    def test_successful_request(self):
        for object_id in SUCCESS_STATUS_OBJECTS:
            response = requests.get(endpoint_url.replace("{object_id}", object_id))
            self.assertEqual(response.status_code, 200, f"Failed to retrieve DRS object. Response status code: {response.status_code}")
    
    def test_failed_request(self):
        for object_id in FAILURE_STATUS_OBJECTS:
            response = requests.get(endpoint_url.replace("{object_id}", object_id))
            self.assertEqual(response.status_code, 404, f"Expected a 404 status code for nonexistent object, but got {response.status_code}")
    
    def test_content_type(self):
        for object_id in DRS_OBJECTS:
            response = requests.get(endpoint_url.replace("{object_id}", object_id))
            self.assertEqual(response.headers.get("Content-Type"), "application/json", f"Expected 'Content-Type' header to be 'application/json', but got '{response.headers.get('Content-Type')}'")
    
    def test_success_schema(self):
        for object_id in SUCCESS_STATUS_OBJECTS:
            response = requests.get(endpoint_url.replace("{object_id}", object_id))
            self.assertTrue(response.json(), "Failed to retrieve DRS object")
            try:
                jsonschema.validate(response.json(), DRS_SCHEMA)
            except jsonschema.exceptions.ValidationError as e:
                self.fail(f"Response does not follow DRS v1.2 specification. Error: {e}")

    def test_failure_schema(self):
        for object_id in FAILURE_STATUS_OBJECTS:
            response = requests.get(endpoint_url.replace("{object_id}", object_id))
            self.assertTrue(response.json(), "Failed to retrieve DRS object")
            try:
                jsonschema.validate(response.json(), DRS_SCHEMA)
            except jsonschema.exceptions.ValidationError:
                pass # Expecting schema validation to fail for nonexistent object, so no action needed

    def test_missing_access_url_or_id(self):
        for object_id in SUCCESS_STATUS_OBJECTS:
            response = requests.get(endpoint_url.replace("{object_id}", object_id))
            response_json = response.json()
            self.assertIsNotNone(response_json, "Access API did not return a valid JSON response")
            self.assertNotIn("access_url", response_json, "Access API returned unexpected access_url field")
            self.assertNotIn("access_id", response_json, "Access API returned unexpected access_id field")
    
    def test_access_id_with_valid_access_url(self):
        for object_id in SUCCESS_STATUS_OBJECTS:
            response = requests.get(endpoint_url.replace("{object_id}", object_id))
            response_json = response.json()
            access_url = response_json.get("access_url")
            if access_url:
                self.assertIsNotNone(access_url, "Access API did not return a valid access_url for access_id")
                response = requests.get(access_url)
                self.assertEqual(response.status_code, 200, "Access API returned invalid access_url for access_id")    

    def test_access_id_with_invalid_access_url(self):
        for object_id in SUCCESS_STATUS_OBJECTS:
            response = requests.get(endpoint_url.replace("{object_id}", object_id))
            response_json = response.json()
            access_id = response_json.get("access_id")
            if access_id:
                invalid_access_url = "http://invalid_access_url"
                response = requests.get(invalid_access_url)
                self.assertNotEqual(response.status_code, 200, "Access API returned valid access_url for invalid access_id")
    
    
    def print_request(self, request):
        print('Request: {}'.format(request))
        print('Request method: {}'.format(request.method))
        print('Request headers: {}'.format(request.headers))
        print('Request body: {}'.format(request.body))

    def print_response(self, response):
        print('Response: {}'.format(response))
        print('Response code: {}'.format(response.status_code))
        print('Response headers: {}'.format(response.headers))
        print('Response body: {}'.format(response.text))

if __name__ == '__main__':
    unittest.main()
