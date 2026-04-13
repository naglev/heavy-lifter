import pytest

from src.parser import InstructionParser
from src.stored_boxes import StoredBoxes
from src.instruction import RobotInstructions

# only public methods need to be tested because private methods are being tested by them indirectly

@pytest.fixture
def parser():
    return InstructionParser()


@pytest.fixture
def sample_data():
    return """|K|            
|A| |Q|     |F|
|P| |U| |B| |T|
 1   2   3   4
     bottom

move 1 from 3 to 4
move 2 from 1 to 3
move 1 from 1 to 2
move 2 from 4 to 1"""


def test_instruction_parser_populates_stored_boxes(parser, sample_data):
    parser.parse(sample_data)
    actual_state = parser.stored_boxes._state
    expected_state = [['P','A','K'],['U','Q'],['B'],['T','F']]
    assert isinstance(parser.stored_boxes, StoredBoxes)
    assert actual_state == expected_state


def test_instruction_parser_populates_instructions(parser, sample_data):
    parser.parse(sample_data)
    instructions = parser.instructions
    first_instruction = instructions.next_instruction()
    assert isinstance(instructions, RobotInstructions)
    assert first_instruction.number_of_boxes == 1
    assert first_instruction.source_stack == 3
    assert first_instruction.destination_stack == 4
