# 1-1-1
# Peter
# peter@husky.nz
# wow


import sys

if len(sys.argv) == 1:
    print("No arguments were specified.")
else:
    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"Arg#{i}: {arg}")
