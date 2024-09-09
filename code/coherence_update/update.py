def build_del_concept_and_incompatible_rules_for_atomic_concepts(a_concepts):
    """
        Build rules for deleting atomic concepts and their incompatible rules
        param:
            a_concepts: string[]
    """
    rules = []
    for a_concept in a_concepts:
        del_rule = f"del_{a_concept}(?X) :- del_{a_concept}_request(?X), {a_concept}(?X) ."
        inc_rule = f"incompatible_update() :- ins_{a_concept}_request(?X), del_{a_concept}_request(?X) ."

    return rules


def build_del_role_and_incompatible_rules_for_roles(roles):
    """
        Build rules for deleting roles and their incompatible rules
        param:
            roles: string[]
    """
    rules = []
    for role in roles:
        del_rule = f"del_{role}(?X, ?Y) :- del_{role}_request(?X, ?Y), {role}(?X, ?Y) ."
        inc_rule = f"incompatible_update() :- ins_{role}_request(?X), del_{role}_request(?X) ."

    return rules


def build_rule_for_positive_inclusion(inclusion):
    """
        Build rules for positive inclusion
        param:
            inclusion: string separated by ','
    """
    return f"{inclusion}(?X) :- {inclusion}_request(?X) ."
