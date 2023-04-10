#import all packages and modules to make requests and test 
import requests
import json
import unittest
import jsonschema
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from utils import *

class TestEndpoints(unittest.TestCase):
    
    def test_success_objects(self):
        for object_id in SUCCESS_STATUS_OBJECTS:
            response = requests.get(endpoint_url.replace("{object_id}", object_id))
            self.assertEqual(response.status_code, 200, f"Failed to retrieve DRS object. Response status code: {response.status_code}")
    
    def test_failure_objects(self):
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

    def test_success_access_methods(self):
        for object_id in SUCCESS_STATUS_OBJECTS:
            response = requests.get(endpoint_url.replace("{object_id}", object_id))
            #get access id from access method and check the access id is in the response
            access_id = response.json().get("access_methods")[0].get("access_id")
            self.assertTrue(access_id in response.json().get("access_methods")[0].get("access_url").get("url"), "Expected 'access_id' to be in 'access_url.url'")
            self.assertTrue(response.json(), "Failed to retrieve DRS object")
            self.assertTrue(response.json().get("access_methods"), "Expected 'access_methods' to be populated")
            for access_method in response.json().get("access_methods"):
                self.assertTrue(access_method.get("access_url"), "Expected 'access_url' to be populated")
                self.assertTrue(access_method.get("type"), "Expected 'type' to be populated")
                self.assertTrue(access_method.get("access_id"), "Expected 'access_id' to be populated")
                self.assertTrue(access_method.get("region"), "Expected 'region' to be populated")
                self.assertTrue(access_method.get("url"), "Expected 'url' to be populated")
                self.assertTrue(access_method.get("headers"), "Expected 'headers' to be populated")
                self.assertTrue(access_method.get("http_method"), "Expected 'http_method' to be populated")
                self.assertTrue(access_method.get("access_url").get("url"), "Expected 'access_url.url' to be populated")
                self.assertTrue(access_method.get("access_url").get("headers"), "Expected 'access_url.headers' to be populated")
                self.assertTrue(access_method.get("access_url").get("http_method"), "Expected 'access_url.http_method' to be populated")
    
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