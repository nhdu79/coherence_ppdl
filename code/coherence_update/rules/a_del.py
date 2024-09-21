# General rules for deleting atomic concepts and roles
# ~ First 2 bullet points/Sec 2.4


# QUESTION: DOES FUNCTIONAL ROLE COUNT AS ROLE?

def build_del_concept_and_incompatible_rules_for_atomic_concepts(a_concepts):
    """
        Build rules for deleting atomic concepts and their incompatible rules
        param:
            a_concepts: string[]
    """
    rules = []
    for a_concept in a_concepts:
        r_del = f"del{a_concept}(X) :- del{a_concept}Request(X), {a_concept}(X)."
        r_inc = f"incompatibleUpdate() :- ins{a_concept}Request(?X), del{a_concept}Request(X)."
        rules.extend([r_del, r_inc])

    return rules


def build_del_role_and_incompatible_rules_for_roles(roles):
    """
        Build rules for deleting roles and their incompatible rules
        param:
            roles: string[]
    """
    rules = []
    for role in roles:
        r_del = f"del{role}(X, Y) :- del{role}Request(X, Y), {role}(X, Y)."
        r_inc = f"incompatibleUpdate() :- ins{role}Request(X), del{role}Request(X)."
        rules.extend([r_del, r_inc])

    return rules


def build_funct_P_and_funct_inv_P_rules(functs, functs_inv):
    """
        Build rules for funct(P) and invFunct(P)
        param:
            functs: string[]
            functs_inv: string[]
    """
    rules = []
    for funct in functs:
        rules.extend(functP(funct))
    for funct_inv in functs_inv:
        rules.extend(functInvP(funct_inv))

    return rules


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

