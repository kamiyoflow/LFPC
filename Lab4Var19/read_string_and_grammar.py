import json
from pprint import pprint
def read_json_file(file_name):
    fo = open(file_name,"r")
    data_string = fo.read()
    data = json.loads(data_string)
    fo.close()
    return data

def get_string():
    return read_json_file("input.json")["input"]

def get_terminals():
    return read_json_file("grammar.json")["Grammar"]["Terminal"]

def get_nonterminals():
    return read_json_file("grammar.json")["Grammar"]["Nonterminal"]

def get_productions():
    return read_json_file("grammar.json")["Grammar"]["Productions"]

def get_start():
    return read_json_file("grammar.json")["Grammar"]["Start"]
