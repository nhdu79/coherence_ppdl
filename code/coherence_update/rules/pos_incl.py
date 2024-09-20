# Positive inclusion rules (Sec 2.4)

def atomicB_in_atomicA(b_repr, a_repr):
    """
        :param b_repr: string
        :param a_repr: string
        :param super_predicates: string[]
    """
    r_del = f"del{b_repr}(X) :- {b_repr}(X), del{a_repr}Request(X)."
    r_inc = f"incompatibleUpdate() :- ins{b_repr}Request(X), del{a_repr}Request(X)."

    return [r_del, r_inc]


def atomicB_in_atomicA_closure(b_repr, a_repr, ai_reprs):
    """
        param ai_reprs: list of A_i concepts where
            A in A_i
    """
    r_closure = f"ins{a_repr}closure(X) :- del{b_repr}(X), not {a_repr}(X), not ins{a_repr}Request(X), not del{a_repr}Request(X)"

    for ai_repr in ai_reprs:
        r_closure += f", not del{ai_repr}Request(X)"
    r_closure += "."

    return [r_closure]


def domP_in_atomicB(p_repr, b_repr):
    """
        Caution: p_repr is representation of `P`, not `domP` (or existsP)
    """
    r_del = f"del{p_repr}(X,Y) :- {p_repr}(X,Y), del{b_repr}Request(X)."
    r_inc = f"incompatibleUpdate() :- ins{p_repr}Request(X,Y), del{b_repr}Request(X)."
    return [r_del, r_inc]


def domP_in_atomicB_closure(p_repr, b_repr, bi_reprs):
    """
        param bi_reprs: list of B_i concepts where
            b in B_i
    """
    r_closure = f"ins{b_repr}closure(X) :- del{p_repr}(X,Y), not {b_repr}(X), not ins{b_repr}Request(X), not del{b_repr}Request(X)"

    for bi_repr in bi_reprs:
        r_closure += f", not del{bi_repr}Request(X)"
    r_closure += "."

    return [r_closure]


def rngP_in_atomicB(p_repr, b_repr):
    """
        Caution: p_repr is representation of `P`, not `rngP` (or existsPMinus)
    """
    r_del = f"del{p_repr}(X,Y) :- {p_repr}(X,Y), del{b_repr}Request(Y)."
    r_inc = f"incompatibleUpdate() :- ins{p_repr}Request(X,Y), del{b_repr}Request(Y)."
    return [r_del, r_inc]


def rngP_in_atomicB_closure(p_repr, b_repr, bi_reprs):
    """
        param bi_reprs: list of B_i concepts where
            b in B_i

    """
    r_closure = f"ins{b_repr}closure(X) :- del{p_repr}(Y,X), not {b_repr}(X), not ins{b_repr}Request(X), not del{b_repr}Request(X)"

    for bi_repr in bi_reprs:
        r_closure += f", not del{bi_repr}Request(X)"
    r_closure += "."

    return [r_closure]


def roleR_in_roleP(r_repr, p_repr):
    r_del = f"del{r_repr}(X,Y) :- {r_repr}(X,Y), del{p_repr}Request(X,Y)."
    r_inc = f"incompatibleUpdate() :- ins{r_repr}Request(X,Y), del{p_repr}Request(X,Y)."
    return [r_del, r_inc]


# TODO(dnh): Implement si_reprs
def roleR_in_roleP_closure(r_repr, p_repr, pi_reprs, si_reprs):
    """
        param pi_reprs: list of P_i roles where
            P in P_i
        param si_reprs: list of S_i roles where
            P in inv(S_i)
    """
    r_closure = f"ins{p_repr}closure(X,Y) :- del{r_repr}(X,Y), not {p_repr}(X,Y), not ins{p_repr}Request(X,Y), not del{p_repr}Request(X,Y)"

    for pi_repr in pi_reprs:
        r_closure += f", not del{pi_repr}Request(X,Y)"

    for si_repr in si_reprs:
        r_closure += f", not del{si_repr}Request(Y,X)"
    r_closure += "."

    return [r_closure]


def roleR_in_invP(r_repr, p_repr):
    """
        Caution: p_repr is representation of `P`, not `invP`.
    """
    r_del = f"del{r_repr}(X,Y) :- {r_repr}(X,Y), del{p_repr}Request(Y,X)."
    r_inc = f"incompatibleUpdate() :- ins{r_repr}Request(X,Y), del{p_repr}Request(Y,X)."
    return [r_del, r_inc , r_closure]


def roleR_in_invP_closure(r_repr, p_repr, pi_reprs, si_reprs):
    """
        param pi_reprs: list of P_i roles where
            P in P_i
        param si_reprs: list of S_i roles where
            P in inv(S_i)
    """

    r_closure = f"ins{p_repr}closure(X,Y) :- del{r_repr}(Y,X), not {p_repr}(X,Y), not ins{p_repr}Request(X,Y), not del{p_repr}Request(X,Y)"
    for pi_repr in pi_reprs:
        r_closure += f", not del{pi_repr}Request(X,Y)"
    for si_repr in si_reprs:
        r_closure += f", not del{si_repr}Request(Y,X)"
    r_closure += "."
    return [r_closure]


def invR_in_roleP(left_repr, right_repr):
    r_del = f"del{left_repr}(X,Y) :- {left_repr}(X,Y), del{right_repr}Request(Y,X)."
    r_inc = f"incompatibleUpdate() :- ins{left_repr}Request(X,Y), del{right_repr}Request(Y,X)."

    return [r_del, r_inc]


def functP(repr):
    """
        Caution: repr is representation of `P`, not `functP`
    """
    r_del = f"del{repr}(X,Y) :- {repr}(X,Y), ins{repr}Request(X,Z), Y!=Z."
    r_inc = f"incompatibleUpdate() :- ins{repr}Request(X,Y), ins{repr}Request(X,Z), Y!=Z."
    return [r_del, r_inc]


def functInvP(repr):
    """
        Caution: repr is representation of `P`, not `functP`
    """
    r_del = f"del{repr}(X,Y) :- {repr}(X,Y), ins{repr}Request(Z,Y), X!=Z."
    r_inc = f"incompatibleUpdate() :- ins{repr}Request(X,Y), ins{repr}Request(Z,Y), X!=Z."
    return [r_del, r_inc]


POS_INCL_METHOD_MAP = {
    "aAInaBSub": atomicB_in_atomicA,
    "rInPSub": roleR_in_roleP,
    "rInPMinusSub": roleR_in_invP,
    "rMinusInPSub": invR_in_roleP,
    "ePInaBSub": domP_in_atomicB,
    "ePMinusInaBSub": rngP_in_atomicB,
}

POS_INCL_CLOSURE_METHOD_MAP = {
    "aAInaBSub": atomicB_in_atomicA_closure,
    "rInPSub": roleR_in_roleP_closure,
    "rInPMinusSub": roleR_in_invP_closure,
    "rMinusInPSub": roleR_in_invP_closure,
    "ePInaBSub": domP_in_atomicB_closure,
    "ePMinusInaBSub": rngP_in_atomicB_closure,
}
