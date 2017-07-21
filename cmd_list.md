Commands/Statements | Purpose
---|---
initiate TM as m_name | this initiates the turing machine with name 'm_name'
m_name.states = (S1, S2, ...) | adds the lists of all states S1, S2, ... for the machine 'm_name' to work on
m_name.initial_state = S | to add a state S as initial_state to the machine 'm_name'
m_name.final_states = (S1, S2, ...) | to add list of states as final_states S1,S2,... to the machine 'm_name'
m_name.T(S1,i) => (S2, o, D) | adds corresponding transition function (from state 'S1' on i/p 'i' To state 'S2' and write 'o', then move to direction 'D') into the transition table of the machine 'm_name'
m_name.display_transition_function | to display the all transition functions added up previously to the machine 'm_name'
m_name.input = abbabb | to give input "abbabb" to machine 'm_name' without any prompts
m_name.read_input | to get prompt for reading input for the machine 'm_name'
m_name.run_TM | run the machine 'm_name' with the transition funtions provided
m_name.run_TM_in_step | run the machine 'm_name' in step-by-step (user acknowledge each step) with the transition funtions provided.
m_name.initiate_again | this restarts the Turing MAchine 'm_name' (restarts the machine state & machine tape)


Notes:
---
  * Directions can be only 'R' or 'L' (Right & Left - respectively)
  * The Machine must be initiated (initiate TM as <>) before going with anyother commands
  * All commands must be prefixed by the machine name - This enables to have multiple machines intialised in the same code file/console
  * run_TM will execute the machine with available inputs and available transition functions & end up in the maximum reachable state & machine tape
  * The machine should be reinitiated (using initiate_again) before executing the machine again so that the current state of machine, input machine Tape are brought back to original state for correct executing of Machine
  * On executing machine (run_TM) for more than one time (without reinitiating using initiate_again), this runs the machine from the lately completed state during previous execution.
