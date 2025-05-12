# 1-1-1
# Peter
# peter@husky.nz
# wow


import sys

# Get number of arguments (excluding script name)
num_args = len(sys.argv) - 1

# Print result with proper grammar
print(f"{num_args} argument{'s' if num_args > 1 else ''}.")
