import os
from utils.functions import read_predicates, read_unary_predicate
from coherence_update.classes.tbox import TBox
from coherence_update.classes.inclusion import INCLUSION_TYPES_ORDER
from coherence_update.update import CohrenceUpdate
import pprint

path = os.path.dirname(os.path.abspath(__file__))
tmp_dir = os.path.join(path, '..', 'tmp')
inclusions = read_predicates(tmp_dir, INCLUSION_TYPES_ORDER)
roles = read_unary_predicate(tmp_dir, 'normForRole')
a_atomics = read_unary_predicate(tmp_dir, 'atomic')
tbox = TBox(inclusions, roles=roles, a_concepts=a_atomics)

update = CohrenceUpdate(tbox)
rules1 = update.build_atomic_del_rules()
rules2 = update.build_update_rules("positive")
rules3 = update.build_update_rules("negative")


print("\n\nAtomic del rules:")
pprint.pprint(rules1)
print("\nPositive update rules:")
pprint.pprint(rules2)
print("\nNegative update rules:")
pprint.pprint(rules3)

breakpoint()

del inclusions

# inclusion = "http://www.semanticweb.org/anon/ontologies/2021/3/lift_at,_:7"
# print(get_inclusion_type(inclusion, predicates))
