# Positive inclusion rules (Sec 2.4)


def atomicB_in_atomicA(left_repr, right_repr, super_predicates_of_right):
    """
        :param left_repr: string (name of inclusion class)
        :param right_repr: string (name of inclusion class)
        :param super_predicates: string[] (list of super concepts/roles represented as md5 hash)
    """
    r_del = f"del{left_repr}(X) :- {left_repr}(X), del{right_repr}request(X)."
    r_inc = f"incompatibleupdate() :- ins{left_repr}request(X), del{right_repr}request(X)."

    r_closure = f"ins{right_repr}closure(X) :- del{left_repr}(X), not {right_repr}(X), not ins{right_repr}request(X), not del{right_repr}request(X)"
    for pred_repr in super_predicates_of_right:
        r_closure += f", not del{pred_repr}request(X)"
    r_closure += "."

    return [r_del, r_inc, r_closure]


def domP_in_atomicB(left_repr, right_repr, super_predicates_of_right):
    """
        Caution: left_repr is representation of `P`, not `domP` (or existsP)

        existsP \sqsubseteq B
    """

    r_del = f"del{left_repr}(X,Y) :- {left_repr}(X,Y), del{right_repr}request(X)."
    r_inc = f"incompatibleupdate() :- ins{left_repr}request(X,Y), del{right_repr}request(X)."

    r_closure = f"ins{right_repr}closure(X) :- del{left_repr}(X,Y), not {right_repr}(X), not ins{right_repr}request(X), not del{right_repr}request(X)"
    for pred_repr in super_predicates_of_right:
        r_closure += f", not del{pred_repr}request(X)"
    r_closure += "."

    return [r_del, r_inc, r_closure]


def rngP_in_atomicB(left_repr, right_repr, super_predicates_of_right):
    """
        Caution: left_repr is representation of `P`, not `rngP` (or existsPMinus)

        existsPMinus \eqsubseteq B
    """
    r_del = f"del{left_repr}(X,Y) :- {left_repr}(X,Y), del{right_repr}request(Y)."
    r_inc = f"incompatibleupdate() :- ins{left_repr}request(X,Y), del{right_repr}request(Y)."

    r_closure = f"ins{right_repr}closure(X) :- del{left_repr}(Y,X), not {right_repr}(X), not ins{right_repr}request(X), not del{right_repr}request(X)"
    for pred_repr in super_predicates_of_right:
        r_closure += f", not del{pred_repr}request(X)"
    r_closure += "."

    return [r_del, r_inc, r_closure]


# TODO(dnh): Implement super_inv_predicates_of_right
def roleR_in_roleP(left_repr, right_repr, super_predicates_of_right, super_inv_predicates_of_right):
    """
        Caution: super_inv_predicates_of_right contains repr of `S` where
        `P \sqsubseteq invS` (NOT `invS`)
    """

    r_del = f"del{left_repr}(X,Y) :- {left_repr}(X,Y), del{right_repr}request(X,Y)."
    r_inc = f"incompatibleupdate() :- ins{left_repr}request(X,Y), del{right_repr}request(X,Y)."

    r_closure = f"ins{right_repr}closure(X,Y) :- del{left_repr}(X,Y), not {right_repr}(X,Y), not ins{right_repr}request(X,Y), not del{right_repr}request(X,Y)"
    for pred_repr in super_predicates_of_right:
        r_closure += f", not del{pred_repr}request(X,Y)"
    for pred_repr in super_inv_predicates_of_right:
        r_closure += f", not del{pred_repr}request(Y,X)"

    r_closure += "."

    return [r_del, r_inc, r_closure]


def roleR_in_invP(left_repr, right_repr, super_predicates_of_right, super_inv_predicates_of_right):
    """
        Caution: right_repr is representation of `P`, not `invP`.
                 super_inv_predicates_of_right contains repr of `S` where
                 `P \sqsubseteq invS` (NOT `invS`).
    """
    r_del = f"del{left_repr}(X,Y) :- {left_repr}(X,Y), del{right_repr}request(Y,X)."
    r_inc = f"incompatibleupdate() :- ins{left_repr}request(X,Y), del{right_repr}request(Y,X)."

    r_closure = f"ins{right_repr}closure(X,Y) :- del{left_repr}(Y,X), not {right_repr}(X,Y), not ins{right_repr}request(X,Y), not del{right_repr}request(X,Y)"
    for pred_repr in super_predicates_of_right:
        r_closure += f", not del{pred_repr}request(X,Y)"

    for pred_repr in super_inv_predicates_of_right:
        r_closure += f", not del{pred_repr}request(Y,X)"

    r_closure += "."

    return [r_del, r_inc , r_closure]


def invR_in_roleP(left_repr, right_repr):
    r_del = f"del{left_repr}(X,Y) :- {left_repr}(X,Y), del{right_repr}request(Y,X)."
    r_inc = f"incompatibleupdate() :- ins{left_repr}request(X,Y), del{right_repr}request(Y,X)."

    return [r_del, r_inc]


def functP(repr):
    """
        Caution: repr is representation of `P`, not `functP`
    """
    r_del = f"del{repr}(X,Y) :- {repr}(X,Y), ins{repr}request(X,Z), Y!=Z."
    r_inc = f"incompatibleupdate() :- ins{repr}request(X,Y), ins{repr}request(X,Z), Y!=Z."
    return [r_del, r_inc]


def functInvP(repr):
    """
        Caution: repr is representation of `P`, not `functP`
    """
    r_del = f"del{repr}(X,Y) :- {repr}(X,Y), ins{repr}request(Z,Y), X!=Z."
    r_inc = f"incompatibleupdate() :- ins{repr}request(X,Y), ins{repr}request(Z,Y), X!=Z."
    return [r_del, r_inc]
