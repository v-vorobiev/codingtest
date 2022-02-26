import requests
import json
import time
from pytest import mark

global dict1

@mark.testing
class TestFestival:
    def test_api_data(self):
        url = 'https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals'
        response = requests.get(url)
        response_code = response.status_code
        j_data = json.loads(response.text)
        print("\n")
        print(response_code)
        global dict1
        dict1 = j_data[0]
        assert response_code == 200, "request failed"
        assert response.text, "response.text is empty"
        assert j_data, "json.loads failed"
        time.sleep(2)

    def test_general_data(self):
        global dict1
        print(dict1)
        assert 'name' in dict1, "'name' key for festivals is missing"
        assert 'bands' in dict1, "'bands' key is missing"

    def test_festivals(self):
        global dict1
        festivals = dict1['name']
        print('Festival: ' + festivals)
        assert festivals, "'name' key for festivals has no corresponding value"

    def test_bands(self):
        global dict1
        bands = dict1['bands']
        print(bands)
        assert bands, "'bands' key is empty"

        for i in range(len(bands)):
            assert bands[i], "one of 'bands' keys is empty"
            assert 'name' in bands[i], "'name' key for 'bands' is missing"
            band_name = bands[i]['name']
            print('Band: ' + band_name)
            assert band_name, "'name' key for 'bands' is empty"

        for i in range(len(bands)):
            assert 'recordLabel' in bands[i], "'recordLabel' key for 'bands' is missing"
            record_label = bands[i]['recordLabel']
            print('Label: ' + record_label)
            assert record_label, "'recordLabel' key for 'bands' is empty"

# plugin pytest-repeat installed
# to run tests 10 times command line code in terminal executed:
# pytest -m testing --count=10 test_festival.py

# pytest-html plugin installed
# to generate html report in pytest, command line code in terminal executed:
# pytest --html=report.html --capture=tee-sys test_festival.py







