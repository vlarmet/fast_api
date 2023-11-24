import pytest
import requests
import json



def test_proba():
       
    with open('tests/client1.json') as data_file:
        myjson = json.load(data_file)
    myjson = json.dumps(myjson)
    r = requests.get("http://127.0.0.1:8000/prediction/", data = myjson)
    r = json.loads(r.text)
    assert round(r["probability"] , 2) == 0.07
