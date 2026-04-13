from collections import deque
from dataclasses import dataclass


@dataclass
class MovementInstruction:
    """Represents a single movement instruction for the robot, specifying
    how many boxes to move and between which stacks.
    """
    number_of_boxes: int
    source_stack: int
    destination_stack: int


class RobotInstructions:
    """Manages a queue of movement instructions for the robot to execute in FIFO order.
    """
    def __init__(self) -> None:
        # A queue (FIFO) should be implemented with a Python deque (doubly linked list)
        # object because popping/adding from/to the ends is O(1) constant time
        self._queue = deque()

    def __bool__(self) -> bool:
        """Return True if there are instructions in the queue, False otherwise.
        """
        return bool(self._queue)

    def add(self, instruction: MovementInstruction) -> None:
        """Add a movement instruction to the end of the queue.

        Args:
            instruction: The MovementInstruction to add.
        """
        self._queue.append(instruction)

    def next_instruction(self) -> MovementInstruction:
        """Remove and return the next movement instruction from the queue.

        Returns:
            The next MovementInstruction in FIFO order.
        """
        return self._queue.popleft()
