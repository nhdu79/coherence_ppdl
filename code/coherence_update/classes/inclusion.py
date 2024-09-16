from hashlib import md5
from collections import defaultdict

INCLUSION_TYPES = [
    # positive
    "aAInaBSub", "ePInaBSub", "ePMinusaBSub",
    "rInPSub", "rInPMinusSub", "rMinusInPSub",
    # negative
    "aAInNotaBSub", "aBInNotePSub", "ePInNotaBSub",
    "aBInNotePMinusSub", "ePMinusInNotaBSub",
    "rInNotPSub", "rInNotPMinusSub"
]

class Inclusion:
    left_pred_sup = defaultdict(list)

    def __init__(self, left_pred_uri, right_pred_uri, incl_type):
        """
        :param inclusion: string separated by ','
            inclusion_type: positive or negative
        """
        self.left_pred_uri = left_pred_uri
        self.right_pred_uri = right_pred_uri
        self.incl_type = incl_type
        self.left_pred_repr = left_pred_uri.split('/')[-1].split('#')[-1]
        self.right_pred_repr = right_pred_uri.split('/')[-1].split('#')[-1]
        Inclusion.left_pred_sup[self.left_pred_repr].append(self.right_pred_repr)

    def __dict__(self):
        return {
            'left_pred_uri': self.left_pred_uri,
            'right_pred_uri': self.right_pred_uri,
            'left_pred_repr': self.left_pred_repr,
            'right_pred_repr': self.right_pred_repr,
            'incl_type': self.incl_type
        }
