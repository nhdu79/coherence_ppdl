import os
from utils.functions import read_predicates
from coherence_update.classes.tbox import TBox
from coherence_update.classes.inclusion import INCLUSION_TYPES

path = os.path.dirname(os.path.abspath(__file__))
tmp_dir = os.path.join(path, '..', 'tmp')
incl_preds = read_predicates(tmp_dir, INCLUSION_TYPES)
tbox = TBox(incl_preds)

del incl_preds

breakpoint()

# inclusion = "http://www.semanticweb.org/anon/ontologies/2021/3/lift_at,_:7"
# print(get_inclusion_type(inclusion, predicates))
