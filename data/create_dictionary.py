"""
Short script to create a dictionary for PR algo. Requires python 3.6+
for default ordered dictionaries.
Use main() to get the dictionary.
Dictionary contains swimmer names as keys, and meet[] objects as values.
Concrete example: {'Phelps Michael' : [2016 Olympics, Worlds], 'Adrian, Nathan G' :[2016 Olympics, Pan America]}
"""

import json
from Meet import Meet

"""
Helper function used to load .json files as dictionaries. I is the
ith json file to load
"""
def load_data(i):
    with open('result' + str(i) + '.json', 'r') as fp:
        dict1 = json.load(fp)
    return dict1

"""
Merges two dictionaries. For conflicting keys, appends a '1' at
the end to remove key conflicts and ensure that they are all added. 
DICT adds it's key-value pairs into MERGE.
"""
def merge_data(merge, dict):
    for comp in dict:
        dummy = comp
        while dummy in merge:
            dummy += '1'
        merge[dummy] = dict[comp]

"""
Uses merge_data() and load_data() to create a dictionary with
swimmer-meet[] key-value pairs. Returns this dictionary.
"""
def main():
    merge = load_data(1)
    dict2 = load_data(2)
    dict3 = load_data(3)
    dict4 = load_data(4)
    dict5 = load_data(5)
    dict6 = load_data(6)
    dict7 = load_data(7)
    dict8 = load_data(8)
    dict9 = load_data(9)
    dict10 = load_data(10)
    dict11 = load_data(11)
    dict12 = load_data(12)
    merge_data(merge, dict2)
    merge_data(merge, dict3)
    merge_data(merge, dict4)
    merge_data(merge, dict5)
    merge_data(merge, dict6)
    merge_data(merge, dict7)
    merge_data(merge, dict8)
    merge_data(merge, dict9)
    merge_data(merge, dict10)
    merge_data(merge, dict11)
    merge_data(merge, dict12)
    print(len(merge))
    swimmer_dict = {}

    for competition in merge:
        lost_to = []
        for competitor in merge[competition]:
            time = merge[competition][competitor][1]
            meet = Meet(competition, lost_to, time)
            if competitor in swimmer_dict.keys():
                swimmer_dict[competitor].append(meet)
            else:
                swimmer_dict[competitor] = [meet]
            lost_to.append(competitor)

    return swimmer_dict
