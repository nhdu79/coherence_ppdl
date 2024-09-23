cd pddl-horndl

domain="elevator"
prefix="benchmarks/$domain"

# path to a (patched) clipper
clipper="/home/zinzin2312/repos/clipper/clipper-distribution/target/clipper/clipper.sh"

# path to compiler.py
compiler="horn_dl_pddl_compiler/compiler.py"
tseitin="horn_dl_pddl_compiler/tseitin.py"

for i in `seq 16 1 16`
do
# input
owl=$prefix/original/TTL.owl
input_domain=$prefix/original/domain.pddl
input_problem=$prefix/original/elevatorProblem$i.pddl

# where the result should be written to
result_domain="_temp_compiledDomain$i.pddl"
result_problem="_temp_compiledProblem$i.pddl"
tseitin_domain="$prefix/pddl/compiledDomain$i.pddl"
tseitin_problem="$prefix/pddl/compiledProblem$i.pddl"

# run compilation
python3 "$compiler" "$owl" "$input_domain" "$input_problem" -d "$result_domain" -p "$result_problem" --clipper "$clipper" --clipper-mqf --debug -v $@

# run tseitin transformation
python3 "$tseitin" "$result_domain" "$result_problem" -d "$tseitin_domain" -p "$tseitin_problem" -v $@

rm "$result_domain" "$result_problem"
done
