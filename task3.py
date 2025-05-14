def turing_machine_addition(input_string):
    """Simulate a Turing Machine to compute the sum of two unary numbers."""
    tape = list(input_string) + ['_'] * 100  # Tape with padding
    head_position = 0
    state = 'q0'  # Initial state
    
    # Transition function
    transitions = {
        ('q0', '1'): ('q0', '1', 'R'),  # Move right over the first number
        ('q0', '+'): ('q1', '+', 'R'),  # Move right over the '+'
        ('q1', '1'): ('q1', '1', 'R'),  # Move right over the second number
        ('q1', ''): ('q2', '1', 'L'),  # Replace '' with '1' and move left
        ('q2', '1'): ('q2', '1', 'L'),  # Move left over the second number
        ('q2', '+'): ('q3', '', 'R'),  # Replace '+' with '' and move right
        ('q3', '1'): ('q3', '1', 'R'),  # Move right over the first number
        ('q3', ''): ('q4', '', 'L'),  # Halt
    }
    
    # Simulation loop
    while True:
        symbol = tape[head_position]
        if (state, symbol) not in transitions:
            break  # Halt if no transition is defined
        
        next_state, write_symbol, direction = transitions[(state, symbol)]
        tape[head_position] = write_symbol  # Write the symbol
        if direction == 'R':
            head_position += 1  # Move right
        elif direction == 'L':
            head_position -= 1  # Move left
        state = next_state  # Update the state
    
    # Return the resulting tape as a string
    return ''.join(tape).strip('_')

# Example input: "111+11"
input_string = "111+11"
result = turing_machine_addition(input_string)
print(f"Input: {input_string} -> Output: {result}")