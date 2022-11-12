from abc import ABC, abstractmethod

class AbstractState:
    @abstractmethod
    def do_job(self) -> bool:
        pass
    
    @abstractmethod
    def get_state():
        pass