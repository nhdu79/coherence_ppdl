# Negation inclusion rules (Sec 2.4)

# TODO(dnh):  Last 2 closure rules

def atomicB_in_not_atomicA(b_repr, a_repr):
    """
        Caution: a_repr is representation of `A`, not `not A`
    """
    r_del_b = f"del{b_repr}(X) :- {b_repr}(X), ins{a_repr}Request(X)."
    r_del_a = f"del{a_repr}(X) :- {a_repr}(X), ins{b_repr}Request(X)."
    r_inc = f"incompatibleUpdate() :- ins{b_repr}Request(X), ins{a_repr}Request(X)."

    return [r_del_b, r_del_a, r_inc]


def atomicA_closure(a_repr, b_reprs, j_reprs, r_reprs):
    """
        param a_repr: string
        param b_reprs: list of B_i concepts where
            A in lnot B_i
        param j_reprs: list of J_i roles where
            A in lnot dom(J_i)
        param r_reprs: list of R_i roles where
            A in lnot rng(R_i)
    """
    r_closure = f"ins{a_repr}(X) :- ins{a_repr}closure(X)"
    for b_repr in b_reprs:
        r_closure += f", not ins{b_repr}Request(X)"

    for j_repr, idx in enumerate(j_reprs):
        r_closure += f", not ins{j_repr}Request(X,Y{idx+1})"

    for r_repr, idx in enumerate(r_reprs):
        r_closure += f", not ins{r_repr}Request(Y{idx+1},X)"
    r_closure += "."

    return [r_closure]


def roleP_closure(p_repr, r_reprs, s_reprs, t_reprs, q_reprs, w_reprs, u_reprs, a_reprs, b_reprs):
    """
        param p_repr: string
        param r_reprs: list of R_i roles where
            P in lnot r_i
        param s_reprs: list of S_i roles where
            P in lnot rng(S_i)
        param t_reprs: list of T_i roles where
            dom(P) in lnot dom(T_i)
        param q_reprs: list of Q_i roles where
            dom(P) in lnot rng(Q_i)
        param w_reprs: list of W_i roles where
            rng(P) in lnot dom(W_i)
        param u_reprs: list of U_i roles where
            rng(P) in lnot rng(U_i)
        param a_reprs: list of A_i concepts where
            dom(P) in lnot A_i
        param b_reprs: list of B_i concepts where
            rng(P) in lnot B_i
    """
    r_closure = f"ins{p_repr}(X,Y) :- ins{p_repr}closure(X,Y)"
    for r_repr in r_reprs:
        r_closure += f", not ins{r_repr}Request(X,Y)"
    for s_repr in s_reprs:
        r_closure += f", not ins{s_repr}Request(Y,X)"
    for t_repr, idx in enumerate(t_reprs):
        r_closure += f", not ins{t_repr}Request(X,Y{idx+1})"
    for q_repr, idx in enumerate(q_reprs):
        r_closure += f", not ins{q_repr}Request(Y{idx+1},X)"
    for w_repr, idx in enumerate(w_reprs):
        r_closure += f", not ins{w_repr}Request(Y,X{idx+1})"
    for u_repr, idx in enumerate(u_reprs):
        r_closure += f", not ins{u_repr}Request(X{idx+1},Y)"
    for a_repr in a_reprs:
        r_closure += f", not ins{a_repr}Request(X)"
    for b_repr in b_reprs:
        r_closure += f", not ins{b_repr}Request(Y)"
    r_closure += "."

    return [r_closure]


def atomicB_in_not_domP(b_repr, p_repr):
    """
        Caution: p_repr is representation of `P`, not `not existsP`
    """
    r_del_b = f"del{b_repr}(X) :- {b_repr}(X), ins{p_repr}Request(X,Y)."
    r_del_p = f"del{p_repr}(X,Y) :- {p_repr}(X,Y), ins{b_repr}Request(X)."
    r_inc = f"incompatibleUpdate() :- ins{b_repr}Request(X), ins{p_repr}Request(X,Y)."

    return [r_del_b, r_del_p, r_inc]


def domP_in_not_atomicB(p_repr, b_repr):
    """
        Caution: p_repr is representation of `P`, not `existsP`
            b_repr is representation of `B`
    """
    r_del_p = f"del{b_repr}(X,Y) :- {b_repr}(X,Y), ins{p_repr}Request(X)."
    r_del_b = f"del{p_repr}(X) :- {p_repr}(X), ins{b_repr}Request(X,Y)."
    r_inc = f"incompatibleUpdate() :- ins{p_repr}Request(X), ins{b_repr}Request(X,Y)."

    return [r_del_b, r_del_p, r_inc]


def r_in_not_P(r_repr, p_repr):
    """
        Caution: p_repr is representation of `P`, not `not P`
    """
    r_del_r = f"del{r_repr}(X,Y) :- {r_repr}(X,Y), ins{p_repr}Request(X,Y)."
    r_del_p = f"del{p_repr}(X,Y) :- {p_repr}(X,Y), ins{r_repr}Request(X,Y)."
    r_inc = f"incompatibleUpdate() :- ins{r_repr}Request(X,Y), ins{p_repr}Request(X,Y)."

    return [r_del_r, r_del_p, r_inc]


def r_in_not_invP(r_repr, p_repr):
    """
        Caution: p_repr is representation of `P`, not `not invP`
    """
    r_del_r = f"del{r_repr}(X,Y) :- {r_repr}(X,Y), ins{p_repr}Request(Y,X)."
    r_del_p = f"del{p_repr}(X,Y) :- {p_repr}(X,Y), ins{r_repr}Request(Y,X)."
    r_inc = f"incompatibleUpdate() :- ins{r_repr}Request(Y,X), ins{p_repr}Request(Y,X)."

    return [r_del_r, r_del_p, r_inc]


NEG_INCL_METHOD_MAP = {
    "aAInNotaBSub": atomicB_in_not_atomicA,
    "aBInNotePSub": atomicB_in_not_domP,
    "ePInNotaBSub": domP_in_not_atomicB,
    "rInNotPSub": r_in_not_P,
    "rInNotPMinusSub": r_in_not_invP
}



