import re

from src.stored_boxes import StoredBoxes
from src.instruction import RobotInstructions, MovementInstruction


class InstructionParser:
    def __init__(self):
        self._stored_boxes: StoredBoxes | None = None
        self._instructions: RobotInstructions | None = None

    def parse(self, content):
        state_raw, instructions_raw = content.split('\n\n')
        self._stored_boxes = self._parse_state(state_raw)
        self._instructions = self._parse_instructions(instructions_raw)
        
    def _parse_state(self, state_raw) -> StoredBoxes:
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
    
    def _get_stack_indexes(self, stack_numbers_row) -> list[list]:
        stack_indexes = []
        for i, char in enumerate(stack_numbers_row):
            if char.isnumeric():
                stack_indexes.append(i)
        return stack_indexes

    def _populate_stacks(self, stacks, stack_indexes, state_lines):
        for state_line in state_lines[::-1]:
            for i, stack_index in enumerate(stack_indexes):
                if state_line[stack_index].isalpha():
                    stacks[i].append(state_line[stack_index])
        
    def _parse_instructions(self, instructions_raw) -> RobotInstructions:
        lines = self._split_lines(instructions_raw)

        instructions = RobotInstructions()
        pattern = re.compile(r'move (\d+) from (\d+) to (\d+)')
        for line in lines:
            match = re.search(pattern, line)
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
 