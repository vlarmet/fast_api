import pytest
import json
from multiprocessing import Process
from ..main import get_prediction


def test_proba():
    
    with open('tests/client1.json') as data_file:
        myjson = json.load(data_file)
    prob = get_prediction(myjson)
        
    assert round(prob["probability"] , 2) == 0.07
        

def test_proba_2():
       
    with open('tests/client2.json') as data_file:
        myjson = json.load(data_file)
    prob = get_prediction(myjson)
        
    assert round(prob["probability"] , 2) == 0.46