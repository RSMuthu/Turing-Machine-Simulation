Commands/Statements | Purpose
---|---
initiate TM as <name> | this initiates the turing machine with name '<name>'
<name>.states = (S1, S2, ...) | adds the lists of all states S1, S2, ... for the machine <name> to work on
<name>.initial_state = S | to add a state S as initial_state to the machine <name>
<name>.final_states = (S1, S2, ...) | to add list of states as final_states S1,S2,... to the machine <name>
<name>.T(S1,i) => (S2, o, D) | adds corresponding transition function (from state 'S1' on i/p 'i' To state 'S2' and write 'o', then move to direction 'D') <br>into the transition table
<name>.display_transition_function | to display the all transition functions added up previously to the machine <name>
<name>.input = abbabb | to give input "abbabb" to machine <name> without any prompts
<name>.read_input | to get prompt for reading input for the machine <name>
<name>.run_TM | run the machine <name> with the transition funtions provided
<name>.initiate_again | this restarts the Turing MAchine <name> (restarts the machine state & machine tape)


###Notes:
  * Directions can be only 'R' or 'L' (Right & Left - respectively)
  * The Machine must be initiated (initiate TM as <>) before going with anyother commands
  * All commands must be prefixed by the machine name - This enables to have multiple machines intialised in the same code file/console
  * run_TM will execute the machine with available inputs and available transition functions & end up in the maximum reachable state & machine tape
  * The machine should be reinitiated (using initiate_again) before executing the machine again so that the current state of machine, input machine Tape are brought back to original state for correct executing of Machine
  * On executing machine (run_TM) for more than one time (without reinitiating using initiate_again), this runs the machine from the lately completed state during previous execution.