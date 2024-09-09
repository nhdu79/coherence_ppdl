import csv
import os
from collections import defaultdict
from pprint import pprint
from constants import PREDICATE_TYPES, CODE_ROOT


def read_csv(file_name):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


p_types = defaultdict(list)
for ns in PREDICATE_TYPES:
    file_name = os.path.join(CODE_ROOT, '..', 'tmp', f'{ns}.csv')
    data = read_csv(file_name)
    p_types[ns] = data


pprint(p_types)
