def is_ambiguous(grammar, start_symbol, string):
    """Check if the grammar is ambiguous for the given string."""
    def derive_nonterminals(nonterminal, remaining_string, derivation):
        """Recursively derive non-terminals to match the string."""
        if not remaining_string:
            # If the string is fully matched, record the derivation
            derivations.append(derivation)
            return
        
        for production in grammar.get(nonterminal, []):
            if isinstance(production, str):  # Terminal symbol
                if remaining_string.startswith(production):
                    derive_nonterminals(start_symbol, remaining_string[len(production):], derivation + [production])
            else:  # Non-terminal symbol
                derive_nonterminals(production, remaining_string, derivation + [production])
    
    derivations = []
    derive_nonterminals(start_symbol, string, [])
    
    # If there are more than one derivation, the grammar is ambiguous
    return len(derivations) > 1

# Example CFG
grammar = {
    'S': ['AB', 'a'],
    'A': ['a'],
    'B': ['b']
}

# Check if the grammar is ambiguous for the string "ab"
start_symbol = 'S'
string = "ab"

if is_ambiguous(grammar, start_symbol, string):
    print(f"The grammar is ambiguous for the string '{string}'.")
else:
    print(f"The grammar is not ambiguous for the string '{string}'.")