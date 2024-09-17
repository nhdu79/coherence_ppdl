from utils.functions import flatten_list
from coherence_update.classes.inclusion import Inclusion

class TBox:
    def __init__(self, incl_dict):
        """
            :param incl_dict: dictionary of inclusions
                :key: inclusion_type
                :value: list of inclusions
        """
        self.inclusions = []
        for incl_type, incl_list in incl_dict.items():
            new_incls = [Inclusion(incl[0], incl[1], incl_type) for incl in incl_list]
            self.inclusions.extend(new_incls)


    def get_super_predicates_of(self, pred_repr):
        """
            :param pred_repr md5 hash of the predicate uri
        """
        return Inclusion.left_pred_sup[pred_repr]


    def get_super_inv_predicates_of(self, pred_repr):
        pass

