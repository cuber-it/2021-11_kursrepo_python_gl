import sys
import os
if len(sys.argv) != 5:
    print(f"usage {sys.argv[0]} py-InFile py-OutFile pattern replacement", file=sys.stderr)
    sys.exit(1)

#Eingabe
#with 