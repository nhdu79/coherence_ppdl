import csv
import os
from collections import defaultdict
from pprint import pprint

def read_csv(file_name):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def read_predicates(tmp_dir, pred_types):
    predicates = defaultdict(list)
    for ns in pred_types:
        file_name = os.path.join(tmp_dir, f'{ns}.csv')
        data = read_csv(file_name)
        predicates[ns] = data

    # pprint(predicates)
    return predicates


def flatten_list(l):
    if not l:
        return []
    return [item for sublist in l for item in sublist]
