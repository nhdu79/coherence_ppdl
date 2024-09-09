import os

CODE_ROOT = os.path.dirname(os.path.abspath(__file__))

PREDICATE_TYPES = [
    "concept",
    "atomicConcept",
    "domOf",
    "exists",
    "invOf",
    "negOf",
    "rngOf",
    "role",
    "sub",
]


INCLUSION_TYPES = {
    "pos": [
        "ASubB",
        "existsPSubB",
        "existsPMinusSubB",
        "RSubP",
        "RSubPMinus",
        "RMinusSubP",
    ],
    "neg": []
}
