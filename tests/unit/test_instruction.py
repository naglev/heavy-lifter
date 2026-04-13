import pytest

from src.instruction import RobotInstructions, MovementInstruction


@pytest.fixture
def robot_instructions():
    return RobotInstructions()


def test_add_and_retrieve_instruction(robot_instructions):
    instruction = MovementInstruction(number_of_boxes=5, source_stack=1, destination_stack=2)
    
    robot_instructions.add(instruction)
    result = robot_instructions.next_instruction()
    
    assert result == instruction
    assert result.number_of_boxes == 5
    assert result.source_stack == 1
    assert result.destination_stack == 2


def test_queue_fifo_order(robot_instructions):
    instruction1 = MovementInstruction(number_of_boxes=1, source_stack=1, destination_stack=2)
    instruction2 = MovementInstruction(number_of_boxes=2, source_stack=2, destination_stack=3)

    robot_instructions.add(instruction1)
    robot_instructions.add(instruction2)

    assert robot_instructions.next_instruction() == instruction1
    assert robot_instructions.next_instruction() == instruction2
