from AbstractState import AbstractState
from StateMachine import StateMachine
from abc import ABC, abstractmethod

class AbstractStateMachineFactory(ABC):
    @abstractmethod
    def create_state_machine() -> StateMachine :
        pass