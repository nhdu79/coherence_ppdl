from coherence_update.classes.inclusion import Inclusion
from collections import defaultdict
from utils.functions import get_repr

class TBox:
    def __init__(self, inclusions, roles=None, a_concepts=None):
        """
            :param inclusions: dict of inclusions
                key: inclusion type
                value: list of inclusions
            :param roles: list of roles
            :param a_concepts: list of atomic concepts
        """
        self.roles = roles
        self.a_concepts = a_concepts
        self.incl_dict = defaultdict(lambda: [])
        for incl_type, incl_list in inclusions.items():
            for incl in incl_list:
                left_uri, right_uri = incl[0], incl[1]
                left_atomic_uri, right_atomic_uri = incl[2], incl[3]
                new_incl = Inclusion(incl_type, left_uri, right_uri, left_atomic_uri, right_atomic_uri)
                self.incl_dict[incl_type].append(new_incl)

    def a_concepts_repr(self):
        return [get_repr(concept) for concept in self.a_concepts]

    def roles_repr(self):
        return [get_repr(role) for role in self.roles]
