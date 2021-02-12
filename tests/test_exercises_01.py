import requests


# Exercise 1.1
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the response status code equals 200
def test_get_user_with_id_1_check_status_code_equals_200():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.status_code == 200