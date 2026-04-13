import re

from src.stored_boxes import StoredBoxes
from src.instruction import RobotInstructions, MovementInstruction


class InstructionParser:
    """Parses the input content to extract the initial state of 
    box stacks and the movement instructions.
    """
    def __init__(self):
        """Initialize the InstructionParser with placeholders for 
        stored boxes and instructions.
        """
        self._stored_boxes: StoredBoxes | None = None
        self._instructions: RobotInstructions | None = None

    def parse(self, content: str):
        """Parse the input content to extract the box stacks' state 
        and movement instructions.

        Args:
            content: The raw input string containing the state and instructions.
        """
        state_raw, instructions_raw = content.split('\n\n')
        self._stored_boxes = self._parse_state(state_raw)
        self._instructions = self._parse_instructions(instructions_raw)

    def _parse_state(self, state_raw: str) -> StoredBoxes:
        """Parse the raw state string to create the initial box stacks.

        Args:
            state_raw: The raw string representing the initial state of the stacks.

        Returns:
            A StoredBoxes object representing the initial state.
        """
        lines = self._split_lines(state_raw)
        stack_indexes = self._get_stack_indexes(lines[-2])
        stack_count = len(stack_indexes)
        # 'stacks' could be a custom Python object but because
        # it does not require any helper or special methods
        # a list of stacks (lists) is enough
        # Create empty stacks (FILO)
        stacks = [[] for _ in range(stack_count)]
        self._populate_stacks(stacks, stack_indexes, lines[:-2])
        return StoredBoxes(starting_state=stacks)

    def _get_stack_indexes(self, stack_numbers_row: str) -> list[int]:
        """Get the indexes in the string that correspond to stack positions.

        Args:
            stack_numbers_row: The string row containing stack numbers.

        Returns:
            A list of integer indexes for each stack.
        """
        stack_indexes = []
        for i, char in enumerate(stack_numbers_row):
            if char.isnumeric():
                stack_indexes.append(i)
        return stack_indexes

    def _populate_stacks(self, stacks: list[list[str]], stack_indexes: list[int], 
                         state_lines: list[str]):
        """Populate the stacks with boxes based on the state lines.

        Args:
            stacks: The list of stacks to populate.
            stack_indexes: The indexes in each line that correspond to stacks.
            state_lines: The lines representing the box arrangement.
        """
        for state_line in state_lines[::-1]:
            for i, stack_index in enumerate(stack_indexes):
                if state_line[stack_index].isalpha():
                    stacks[i].append(state_line[stack_index])

    def _parse_instructions(self, instructions_raw: str) -> RobotInstructions:
        """Parse the raw instructions string to create a queue of movement instructions.

        Args:
            instructions_raw: The raw string containing movement instructions.

        Returns:
            A RobotInstructions object containing all parsed instructions.
        """
        lines = self._split_lines(instructions_raw)

        instructions = RobotInstructions()
        pattern = re.compile(r'move (\d+) from (\d+) to (\d+)')
        for line in lines:
            match = re.search(pattern, line)
            if not match:
                break
            number_of_boxes, source_stack, destination_stack = match.groups()
            instruction = MovementInstruction(
                int(number_of_boxes),
                int(source_stack),
                int(destination_stack)
            )
            instructions.add(instruction)

        return instructions
    
    def _split_lines(self, text: str) -> list[str]:
        return text.split('\n')

    @property
    def stored_boxes(self) -> StoredBoxes:
        # additional logic can be added here
        # otherwise this descriptor is not necessary
        return self._stored_boxes

    @property
    def instructions(self) -> RobotInstructions:
        return self._instructions
 