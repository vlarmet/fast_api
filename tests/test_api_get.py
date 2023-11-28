import pytest
import json
from multiprocessing import Process
import requests

# test envoi du json client
def test_proba():
    
    with open('tests/client1.json') as data_file:
        myjson = json.load(data_file)
        myjson = json.dumps(myjson)
    prob = requests.get(url = 'http://127.0.0.1:8000/prediction/', data = myjson).text
    prob = json.loads(prob)
    assert round(prob["probability"] , 2) == 0.07
        

def test_proba_2():
       
    with open('tests/client2.json') as data_file:
        myjson = json.load(data_file)
        myjson = json.dumps(myjson)
    prob = requests.get(url = 'http://127.0.0.1:8000/prediction/', data = myjson).text
    prob = json.loads(prob)
    assert round(prob["probability"] , 2) == 0.46

# test envoi du json client
def test_proba3():
    
    
    myjson = '{"index" : 73}'
    prob = requests.get(url = 'http://127.0.0.1:8000/prediction2/', data = myjson).text
    prob = json.loads(prob)
        
    assert round(prob["probability"] , 2) == 0.48
        