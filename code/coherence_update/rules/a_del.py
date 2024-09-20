# General rules for deleting atomic concepts and roles
# ~ First 2 bullet points/Sec 2.4


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

