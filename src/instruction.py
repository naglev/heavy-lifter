from collections import deque
from dataclasses import dataclass


@dataclass
class MovementInstruction:
    number_of_boxes: int
    source_stack: int
    destination_stack: int


class RobotInstructions:
    def __init__(self):
        # A queue (FIFO) should be implemented with a Python deque (doubly linked list) 
        # object because popping/adding from/to the ends is O(1) constant time
        self._queue = deque()
    
    def add(self, instruction: MovementInstruction):
        self._queue.append(instruction)

    def next_instruction(self) -> MovementInstruction:
        return self._queue.popleft()
