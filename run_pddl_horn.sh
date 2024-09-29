domain="cats"
prefix="benchmarks/$domain"
repo_dir="pddl-horndl"
update_rules_path="tmp/_update_rules.txt"

# path to a (patched) clipper
clipper="/home/zinzin2312/repos/clipper/clipper-distribution/target/clipper/clipper.sh"

# path to compiler.py
compiler="$repo_dir/horn_dl_pddl_compiler/compiler.py"
tseitin="$repo_dir/horn_dl_pddl_compiler/tseitin.py"

# input
i=6
owl=$repo_dir/$prefix/original/TTL.owl
input_domain=$repo_dir/$prefix/original/domain.pddl
input_problem=$repo_dir/$prefix/original/catProblem$i.pddl

# where the result should be written to
result_domain="_temp_compiledDomain.pddl"
result_problem="_temp_compiledProblem$i.pddl"
tseitin_domain="benchmarks/output/$domain/compiledDomain$i.pddl"
tseitin_problem="benchmarks/output/$domain/compiledProblem$i.pddl"

# run compilation
python3 "$compiler" "$owl" "$input_domain" "$input_problem" -d "$result_domain" -p "$result_problem" --clipper "$clipper" --clipper-mqf --debug -v $@

# run tseitin transformation
python3 "$tseitin" "$result_domain" "$result_problem" -d "$tseitin_domain" -p "$tseitin_problem" -v $@

rm "$result_domain" "$result_problem"
