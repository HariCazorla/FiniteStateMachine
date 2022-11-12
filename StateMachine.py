from AbstractState import AbstractState

class StateMachine:
    def __init__(self) -> None:
        self._states = list()
        self._transition = dict()
        self._init_state = None
        self._final_state = None
    
    def get_states(self):
        return self._states
    
    def get_init_state(self) -> AbstractState:
        return self._init_state        
    
    def set_init_state(self, state: AbstractState):
        self._init_state = state
        
    def get_final_state(self) -> AbstractState:
        return self._final_state        
    
    def set_final_state(self, state: AbstractState):
        self._final_state = state
            
    def add_state(self, state: AbstractState):
        self._states.append(state)
        
    def add_transition(self, from_state, to_state_on_sucess, to_state_on_failure):
        transition = {
            "success": to_state_on_sucess,
            "failure": to_state_on_failure
        }
        self._transition[from_state] = transition
        
    def get_transitions(self):
        return self._transition
    
    def get_next_state(self, current_state: AbstractState, outcome: bool):
        if (outcome):
            return self._transition[current_state]["success"]
        else:
            return self._transition[current_state]["failure"]
        
    def run(self):
        state = self._init_state
        print(f"starting with {state.get_state()}")
        while(True):
            ret = state.do_job()
            if (state.get_state() == self._final_state.get_state()):
                print(f"Reached final state!")
                return
            state = self.get_next_state(current_state=state, outcome=ret)
            print(f"transitioning to {state.get_state()}")