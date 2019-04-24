import json
import Swimmer

def load_data(i):
    with open('result' + str(i) + '.json', 'r') as fp:
        dict1 = json.load(fp)
    return dict1

def merge_data(merge, dict):
    for comp in dict:
        dummy = comp
        while dummy in merge:
            dummy += '1'
        merge[dummy] = dict[comp]

def main():
    merge = load_data(1)
    dict2 = load_data(2)
    dict3 = load_data(3)
    dict4 = load_data(4)
    merge_data(merge, dict2)
    merge_data(merge, dict3)
    merge_data(merge, dict4)

    print(merge)

    swimmer_set = set()

    for competitor 


main()