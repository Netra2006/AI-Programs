
from itertools import product
import re

def check_entailment():
    kb = input("Enter Knowledge Base: ")
    query = input("Enter Query: ")

    # Extract propositional symbols
    symbols = sorted(set(re.findall(r'\b[A-Z]\b', kb + " " + query)))

    found = False

    # Generate all truth assignments
    for values in product([True, False], repeat=len(symbols)):
        assignment = dict(zip(symbols, values))

        # Evaluate Knowledge Base
        kb_value = eval(kb, {"__builtins__": {}}, assignment)

        # Check query if KB is true
        if kb_value:
            query_value = eval(query, {"__builtins__": {}}, assignment)

            if not query_value:
                print("\nNOT ENTAILED")
                print("Counterexample:", assignment)
                found = True
                break

    if not found:
        print("\nENTAILED")


check_entailment()
