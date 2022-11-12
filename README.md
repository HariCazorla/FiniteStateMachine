# FiniteStateMachine
A Simple State machine implementation in python

The repository has three states defined
- StateA (Initial State)
- StateB
- StateC (Final State)

Following transitions are defined,
- StateA -on-sucess--> StateB
- StateA -on-failure--> StateC
- StateB -on-sucess--> StateC 
- StateB -on-failure--> StateC

We can add more states and more custom transitions among these states as well.

Follow these steps to run the program,

```
python3 -m venv sm
source sm/bin/activate
python main.py
```

Expected Output

```
Initialising state machine...
starting with StateA
StateA:: Job completed successfully...
transitioning to StateB
StateB:: Job completed successfully...
transitioning to StateC
StateC:: Job completed successfully...
Reached final state!
```