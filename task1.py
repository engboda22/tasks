EPSILON = 'ε'

def epsilon_closure(nfa, state):
    closure = set([state])
    stack = [state]
    while stack:
        current = stack.pop()
        for next_state in nfa['transitions'].get(current, {}).get(EPSILON, []):
            if next_state not in closure:
                closure.add(next_state)
                stack.append(next_state)
    return closure

def epsilon_closure_set(nfa, states):
    closure = set()
    for state in states:
        closure.update(epsilon_closure(nfa, state))
    return closure

def move(nfa, states, symbol):
    result = set()
    for state in states:
        result.update(nfa['transitions'].get(state, {}).get(symbol, []))
    return result

def nfa_to_dfa(nfa):
    symbols = set()
    for state in nfa['transitions']:
        for symbol in nfa['transitions'][state]:
            if symbol != EPSILON:
                symbols.add(symbol)

    start_closure = frozenset(epsilon_closure(nfa, nfa['start']))
    dfa_states = {start_closure}
    dfa_transitions = {}
    unmarked_states = [start_closure]
    dfa_final_states = set()

    while unmarked_states:
        current = unmarked_states.pop()
        dfa_transitions[current] = {}

        for symbol in symbols:
            move_result = move(nfa, current, symbol)
            closure_result = epsilon_closure_set(nfa, move_result)
            closure_frozen = frozenset(closure_result)

            if not closure_result:
                continue

            if closure_frozen not in dfa_states:
                dfa_states.add(closure_frozen)
                unmarked_states.append(closure_frozen)

            dfa_transitions[current][symbol] = closure_frozen

    for dfa_state in dfa_states:
        if any(state in nfa['accept'] for state in dfa_state):
            dfa_final_states.add(dfa_state)

    return {
        'states': dfa_states,
        'alphabet': symbols,
        'transitions': dfa_transitions,
        'start': start_closure,
        'accept': dfa_final_states
    }

# مثال بسيط للاستخدام:
nfa = {
    'states': {'q0', 'q1', 'q2'},
    'alphabet': {'a', 'b'},
    'transitions': {
        'q0': {'ε': ['q1', 'q2']},
        'q1': {'a': ['q1']},
        'q2': {'b': ['q2']}
    },
    'start': 'q0',
    'accept': {'q1'}
}

dfa = nfa_to_dfa(nfa)

# طباعة الحالة النهائية للدالة DFA
print("DFA States:")
for state in dfa['states']:
    print(state)
print("Start State:", dfa['start'])
print("Accept States:", dfa['accept'])
print("Transitions:")
for state, transitions in dfa['transitions'].items():
    for symbol, target in transitions.items():
        print(f"{state} --{symbol}--> {target}")