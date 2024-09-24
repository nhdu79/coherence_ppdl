## Quick instruction:

* Change the path in the file code/nemo/t_closure.rls to your local path to the coherence_ppdl folder
    - This also works with all files under benchmarks/

```
@import TRIPLE :- turtle{resource="{{ PATH_TO_REPO }}/coherence_ppdl/benchmarks/ontologies/elevator/elevator.ttl"} .

```

* Given Nemo is present (via nmo cli), to extract all predicates and write them to /tmp directory, run:
``` bash
    nmo code/nemo/t_closure.rls --export all --export-dir tmp

```

* In the /code folder, to write all coherence update rules, run:
    ``` python
        python main.py
    ```
    - A breakpoint() is added at the end for rules inspection; the 5 types are (in order of appearance):
        - Atomic del and funct rules
        - Positive update rules
        - Negative update rules
        - Positive closure update rules
        - Negative closure update rules


## Project structure:

* /benchmarks: Contains all ontologies and .pddl files
* /code: Contains all code files
    - /nemo: Contains all the Nemo code file
    - /coherence_update: Contains all Python code files
* /tmp: Contains all the extracted predicates from Nemo



# coherence_ppdl

## Nemo Installation

### URL: https://github.com/knowsys/nemo

## Clipper Installation

### URL: https://github.com/ghxiao/clipper
