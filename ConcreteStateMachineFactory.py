from AbstractStateMachineFactory import AbstractStateMachineFactory
from StateMachine import StateMachine
from ConcreteStateA import ConcreteStateA
from ConcreteStateB import ConcreteStateB
from ConcreteStateC import ConcreteStateC

class ConcreteStateMachineFactory(AbstractStateMachineFactory):
    def __init__(self) -> None:
        print(f"Initialising state machine...")
        self._state_machine = StateMachine()
    
    def create_state_machine(self) -> StateMachine:
        # Create States
        state1 = ConcreteStateA()
        state2 = ConcreteStateB()
        state3 = ConcreteStateC()
        
        self._state_machine.add_state(state1)
        self._state_machine.add_state(state2)
        self._state_machine.add_state(state3)
        # Set init state and final state
        self._state_machine.set_init_state(state1)
        self._state_machine.set_final_state(state3)
        # Define transition
        self._state_machine.add_transition(from_state=state1, to_state_on_sucess=state2, to_state_on_failure=state3)
        self._state_machine.add_transition(from_state=state2, to_state_on_sucess=state3, to_state_on_failure=state3)
        self._state_machine.add_transition(from_state=state3, to_state_on_sucess=None, to_state_on_failure=None)
        return self._state_machine