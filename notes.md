## PROBLEMS

* Problem 1:
    - There's a slight mismatch between the (elementary) rules described in the papers (for case positive + negative) and my implementation of cl(T).
    - In details, for the positive inclusion cases (Paper 1: Explanation in the DL-Lite of DLs), they only define the rules for positive inclusions, i.e.\ no negations for reflexivity.
        - Ans: Ignore !!!
    - Afterwards, we checked this and compare with the other paper for the negative inclusions (Paper 2: Tractable Reasoning and Efﬁcient Query Answering in Description Logics: The DL-Lite Family) and came up with a solution of adding 1 more rule: "X \sqsubseteq \lnot Y => Y \sqsubseteq \lnot X".
    => This would only work IF X and Y are allowed to be negated in that rule AND the transitivity rule; which is the case in the implementation; NOT in paper.
    => NOT LOGICALLY EQUIVALENT !!!

* Problem 2: Implicit inequality in paper ???? => Added the following in the inclusion identifcation:
    - aAinaBSub: A != B
    - rInPSub: R != P
        - Merge! In paper!
        - Mention in thesis! In implementaiton or sth

* Questions:
    - In horn-pddl, how do I pass a list of datalog rules to the compiler?
        - In `_create_datalog_rules_object()`, the `self.datalog_rules` is always empty???
    - After compiling into PDDL, which components are to be adjusted for the new rules per my definition?


## Elevator

* Concepts:
    - Floor
    - Passenger
    - LiftAt
    - Boarded
    - Served

* Roles:
    - origin
    - destin
    - next

* TBox T
    - funct(next)
    - dom(origin) ⊑ Passenger
    - rng(origin) ⊑ Floor
    - dom(destin) ⊑ Passenger
    - rng(destin) ⊑ Floor
    - Passenger ⊑ ¬Floor
    - Boarded ⊑ Passenger
    - Served ⊑ Passenger
    - LiftAt ⊑ Floor
* cl(T): contains T and:
    - funct(next)
    - rng(next) ⊑ rng(next)
    - dom(next) ⊑ dom(next)
    - origin ⊑ origin
    - destin ⊑ destin
    - next ⊑ next

    - dom(origin) ⊑ dom(origin)
    - dom(origin) ⊑ ¬Floor
    - dom(origin) ⊑ ¬LiftAt
    - dom(origin) ⊑ ¬rng(origin)
    - dom(origin) ⊑ ¬rng(destin)

    - rng(origin) ⊑ rng(origin)
    - rng(origin) ⊑ ¬Passenger
    - rng(origin) ⊑ ¬Boarded
    - rng(origin) ⊑ ¬Served
    - rng(origin) ⊑ ¬dom(origin)
    - rng(origin) ⊑ ¬dom(destin)

    - rng(destin) ⊑ rng(destin)
    - rng(destin) ⊑ ¬Passenger
    - rng(destin) ⊑ ¬Boarded
    - rng(destin) ⊑ ¬Served
    - rng(destin) ⊑ ¬dom(origin)
    - rng(destin) ⊑ ¬dom(destin)

    - dom(destin) ⊑ dom(destin)
    - dom(destin) ⊑ ¬LiftAt
    - dom(destin) ⊑ ¬Floor
    - dom(destin) ⊑ ¬rng(origin)
    - dom(destin) ⊑ ¬rng(destin)

    - Floor ⊑ ¬Passenger
    - Floor ⊑ ¬Boarded
    - Floor ⊑ ¬Served
    - Floor ⊑ ¬dom(origin)
    - Floor ⊑ ¬dom(destin)

    - LiftAt ⊑ LiftAt
    - LiftAt ⊑ ¬Passenger
    - LiftAt ⊑ ¬Boarded
    - LiftAt ⊑ ¬Served
    - LiftAt ⊑ ¬dom(origin)
    - LiftAt ⊑ ¬dom(destin)

    - Boarded ⊑ Boarded
    - Boarded ⊑ ¬Floor
    - Boarded ⊑ ¬LiftAt
    - Boarded ⊑ ¬rng(origin)
    - Boarded ⊑ ¬rng(destin)

    - Served ⊑ Served
    - Served ⊑ ¬Floor
    - Served ⊑ ¬LiftAt
    - Served ⊑ ¬rng(origin)
    - Served ⊑ ¬rng(destin)

    - Passenger ⊑ Passenger
    - Passenger ⊑ ¬LiftAt
    - Passenger ⊑ ¬Floor
    - Passenger ⊑ ¬rng(origin)
    - Passenger ⊑ ¬rng(destin)


## Cat

* Concepts:
    - ObjectX
    - Bomb
    - Cat
    - Package

* Roles:
    - contains


* TBox T:
    - funct(contains)
    - dom(contains) ⊑ Package
    - rng(contains) ⊑ ObjectX
    - Bomb ⊑ ObjectX
    - Bomb ⊑ ¬Cat
    - Cat ⊑ ObjectX
    - Package ⊑ dom(contains)


* cl(T): contains T and:
    - ObjectX ⊑ ObjectX
    - Bomb ⊑ Bomb
    - Cat ⊑ Cat
    - Cat ⊑ ¬Bomb
    - Package ⊑ Package
    - dom(contains) ⊑ dom(contains)
    - rng(contains) ⊑ rng(contains)
