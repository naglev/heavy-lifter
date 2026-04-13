import pytest

from src.heavy_lifter import HeavyLifterV1
from src.instruction import RobotInstructions, MovementInstruction
from src.stored_boxes import StoredBoxes


@pytest.fixture
def heavy_lifter_v1():
    return HeavyLifterV1()


@pytest.fixture
def boxes():
    return StoredBoxes([['P','A','K'],['U','Q'],['B'],['T','F']])


def test_rearrange_boxes(heavy_lifter_v1, boxes):
    inst1 = MovementInstruction(2, 1, 3)
    inst2 = MovementInstruction(1, 3, 4)
    robot_insts = RobotInstructions()
    robot_insts.add(inst1)
    robot_insts.add(inst2)

    heavy_lifter_v1.rearrange(boxes, robot_insts)

    assert boxes.state == [['P'],['U','Q'],['B','K'],['T','F','A']]


def test_move_more_boxes_than_boxes_in_stack(heavy_lifter_v1, boxes):
    inst = MovementInstruction(5, 1, 3)
    robot_insts = RobotInstructions()
    robot_insts.add(inst)

    heavy_lifter_v1.rearrange(boxes, robot_insts)

    assert boxes.state == [[],['U','Q'],['B','K','A','P'],['T','F']]
