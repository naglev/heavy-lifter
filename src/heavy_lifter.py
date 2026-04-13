import abc

from src.stored_boxes import StoredBoxes
from src.instruction import RobotInstructions, MovementInstruction


class HeavyLifter(metaclass=abc.ABCMeta):
    """Abstract base class for heavy lifter implementations that rearrange boxes
    according to a set of movement instructions.
    """
    @abc.abstractmethod
    def rearrange(self, boxes: StoredBoxes, instructions: RobotInstructions)  -> None:
        """Rearrange the boxes according to the provided instructions.

        Args:
            boxes: The current state of stored boxes.
            instructions: The queue of movement instructions to execute.
        """
        raise NotImplementedError


class HeavyLifterV1(HeavyLifter):
    """Heavy lifter implementation that moves boxes one by one from the source stack
    to the destination stack for each instruction.
    """
    def rearrange(self, boxes: StoredBoxes, instructions: RobotInstructions) -> None:
        """Execute all movement instructions, moving boxes one at a time.

        Args:
            boxes: The current state of stored boxes.
            instructions: The queue of movement instructions to execute.
        """
        while instructions:
            inst = instructions.next_instruction()
            self._execute(boxes, inst)

    def _execute(self, boxes: StoredBoxes, instruction: MovementInstruction) -> None:
        """Move the specified number of boxes from the source stack to the destination stack.

        Args:
            boxes: The current state of stored boxes.
            instruction: The movement instruction to execute.
        """
        for _ in range(instruction.number_of_boxes):
            try:
                box = boxes[instruction.source_stack - 1].pop()
            except IndexError:
                return
            boxes[instruction.destination_stack - 1].append(box)


class HeavyLifterV2(HeavyLifter):
    """Placeholder for an alternative heavy lifter implementation.
    """
    def rearrange(self, boxes: StoredBoxes, instructions: RobotInstructions) -> None:
        pass
