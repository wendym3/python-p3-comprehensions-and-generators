#!/usr/bin/env python3

def return_evens(num_list):
    evens = [num for num in num_list if num % 2 == 0]
    return evens  
    pass

def make_exclamation(sentence_list):
    exclamation =[sentence + '!' for sentence in sentence_list]
    return exclamation
    pass