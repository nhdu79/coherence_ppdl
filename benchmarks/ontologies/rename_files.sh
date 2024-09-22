# loop through domainProblem15.pddl to domainProblem34.pddl and rename them to domainProblem1.pddl to domainProblem20.pddl
# This is to make the file names consistent with the domainProblem1.pddl to domainProblem20.pddl in the training set

for ((i=15; i<=34; i++)); do
  # Calculate the new number (1 to 20)
  new_num=$((i - 14))

  # Create the old and new filenames
  old_filename="elevatorProblem${i}.pddl"
  new_filename="elevatorProblem${new_num}.pddl"

  # Check if the old file exists before renaming
  if [ -f "$old_filename" ]; then
    echo "Renaming $old_filename to $new_filename"
    mv "$old_filename" "$new_filename"
  else
    echo "File $old_filename does not exist."
  fi
done
