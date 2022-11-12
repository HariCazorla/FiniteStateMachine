from AbstractState import AbstractState

class ConcreteStateC(AbstractState):
    def __init__(self) -> None:
        self._state = "StateC"
    
    def __repr__(self) -> str:
        return self._state
    
    def get_state(self):
        return self._state
        
    def do_job(self):
        print(f"{self.get_state()}:: Job completed successfully...")
        return True