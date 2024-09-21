import os
from utils.functions import read_predicates, read_unary_predicate
from coherence_update.classes.tbox import TBox
from coherence_update.classes.inclusion import INCLUSION_TYPES_ORDER
from coherence_update.update import CohrenceUpdate
import pprint

try:
    path = os.path.dirname(os.path.abspath(__file__))
    tmp_dir = os.path.join(path, '..', 'tmp')
    inclusions = read_predicates(tmp_dir, INCLUSION_TYPES_ORDER)
    roles = read_unary_predicate(tmp_dir, 'normForRole')
    a_atomics = read_unary_predicate(tmp_dir, 'atomic')
    functs = read_unary_predicate(tmp_dir, 'normForFunct')
    inv_functs = read_unary_predicate(tmp_dir, 'functInv')
except FileNotFoundError as e:
    print(e)
    exit(1)

tbox = TBox(inclusions, roles=roles, a_concepts=a_atomics, functs=functs, functs_inv=inv_functs)

update = CohrenceUpdate(tbox)
rules1 = update.build_atomic_del_and_funct_rules()
rules2 = update.build_update_rules("positive")
rules3 = update.build_update_rules("negative")
rules4 = update.build_positive_closure_update_rules()
rules5 = update.build_negative_closure_update_rules()


# print("\n\nAtomic del and funct rules:")
# pprint.pprint(rules1)
# print("\nPositive update rules:")
# pprint.pprint(rules2)
# print("\nNegative update rules:")
# pprint.pprint(rules3)
print("\nPositive closure update rules:")
pprint.pprint(rules4)
print("\nNegative closure update rules:")
pprint.pprint(rules5)

breakpoint()

del inclusions

# inclusion = "http://www.semanticweb.org/anon/ontologies/2021/3/lift_at,_:7"
# print(get_inclusion_type(inclusion, predicates))
