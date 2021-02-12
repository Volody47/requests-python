import requests


# Exercise 1.1
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the response status code equals 200
def test_check_status_code_equals_200():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.status_code == 200

# Exercise 1.2
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the value of the response header 'Content-Type' equals 'application/json'
def test_check_response_header_equals_application_json():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.headers['Content-Type'] == "application/json"