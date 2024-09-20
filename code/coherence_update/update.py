from collections import defaultdict
from coherence_update.rules.a_del import *
from coherence_update.rules.neg_incl import *
from coherence_update.rules.pos_incl import *

class CohrenceUpdate:
    def __init__(self, tbox):
        self.tbox = tbox

    def build_atomic_del_rules(self):
        atomic_concepts = self.tbox.a_concepts_repr()
        atomic_roles = self.tbox.roles_repr()
        r_concepts = build_del_concept_and_incompatible_rules_for_atomic_concepts(atomic_concepts)
        r_roles = build_del_role_and_incompatible_rules_for_roles(atomic_roles)

        return r_concepts + r_roles

    def build_update_rules(self, closure_type):
        mapping = closure_type == "positive" and POS_INCL_METHOD_MAP or NEG_INCL_METHOD_MAP
        rules = []
        for key, method in mapping.items():
            inclusions = self.tbox.incl_dict[key]
            for incl in inclusions:
                rules.extend(method(incl.get_left_repr(), incl.get_right_repr()))

        return rules

    def build_positive_closure_update_rules(self):
        # TODO: Implement
        rules = []
        return rules

    def build_negative_closure_update_rules(self):
        # TODO: Implement
        pass
