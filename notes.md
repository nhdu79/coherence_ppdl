## PROBLEMS

* Problem 1:
    - There's a slight mismatch between the (elementary) rules described in the papers (for case positive + negative) and my implementation of cl(T).
    - In details, for the positive inclusion cases (Paper 1: Explanation in the DL-Lite of DLs), they only define the rules for positive inclusions, i.e.\ no negations for reflexivity.
    - Afterwards, we checked this and compare with the other paper for the negative inclusions (Paper 2: Tractable Reasoning and Efﬁcient Query Answering in Description Logics: The DL-Lite Family) and came up with a solution of adding 1 more rule: "X \sqsubseteq \lnot Y => Y \sqsubseteq \lnot X".
    => This would only work IF X and Y are allowed to be negated in that rule AND the transitivity rule; which is the case in the implementation; NOT in paper.
    => How to move forward ???

* Problem 2: Implicit inequality in paper ???? => Added the following in the inclusion identifcation:
    - aAinaBSub: A != B
    - rInPSub: R != P


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
    - Passenger ⊑ ¬Floor
    - Boarded ⊑ Passenger
    - Served ⊑ Passenger
    - LiftAt ⊑ Floor

* cl(T): contains T and:
    - Passenger ⊑ Passenger
    - Boarded ⊑ Boarded
    - Served ⊑ Served
    - LiftAt ⊑ LiftAt

    - Floor ⊑ ¬Passenger
    - Floor ⊑ ¬Boarded
    - Floor ⊑ ¬Served

    - LiftAt ⊑ ¬Passenger
    - LiftAt ⊑ ¬Boarded
    - LiftAt ⊑ ¬Served

    - Boarded ⊑ ¬Floor
    - Boarded ⊑ ¬LiftAt

    - Served ⊑ ¬Floor
    - Served ⊑ ¬LiftAt

    - Passenger ⊑ ¬LiftAt
    - Passenger ⊑ ¬Floor
