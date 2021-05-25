from read_string_and_grammar import *
def extract_first_from_right(first_array,symbol):
    if symbol in get_terminals() and symbol not in first_array:
        first_array.append(symbol)
    elif symbol in get_nonterminals() and symbol not in first_array:
        first_array.append(symbol)
        find_first(first_array,symbol)
def find_first(first_array,nonterminal):
    for production in get_productions():
        for left, right in production.items():
            if(left == nonterminal):
                extract_first_from_right(first_array,right[0])
def extract_last_from_right(last_array,symbol):
    if symbol in get_terminals() and symbol not in last_array:
        last_array.append(symbol)
    elif symbol in get_nonterminals() and symbol not in last_array:
        last_array.append(symbol)
        find_last(last_array,symbol)
def find_last(last_array,nonterminal):
    for production in get_productions():
        for left, right in production.items():
            if(left == nonterminal):
                extract_last_from_right(last_array,right[-1])
def get_simple_precedent_matrix():
    simple_presedence_matrix = {}
    for nonterminal in get_nonterminals():
        first_array = []
        last_array = []
        find_first(first_array,nonterminal)
        find_last(last_array,nonterminal)
        simple_presedence_matrix[nonterminal] = {"first": first_array,"last": last_array}
    return simple_presedence_matrix
def get_first_of_nonterminal(nonterminal):
    return get_simple_precedent_matrix()[nonterminal]["first"]

def get_last_of_nonterminal(nonterminal):
    return get_simple_precedent_matrix()[nonterminal]["last"]

print("First Last Matrix is given below")
pprint(get_simple_precedent_matrix())
