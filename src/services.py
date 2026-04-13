from pathlib import Path

from src.parser import InstructionParser
from src.heavy_lifter import HeavyLifter, HeavyLifterV1, HeavyLifterV2


def do_the_heavy_lifting(file_path: Path, heavy_lifter_version: str) -> str:
    """Serve as the use case of the program. Create the domain models and
    coordinates them.

    Args:
        file_path: Path to the instruction set file.
        heavy_lifter_version: The selected version of the heavy lifter.
    """
    content = _read_file(file_path)

    parser = InstructionParser()
    parser.parse(content)
    stored_boxes = parser.stored_boxes
    instructions = parser.instructions

    heavy_lifter = _create_heavy_lifter(heavy_lifter_version)
    heavy_lifter.rearrange(stored_boxes, instructions)

    return stored_boxes.top_boxes


def _read_file(file_path: Path) -> str:
    with open(file_path, encoding='utf-8') as f:
        return f.read()


def _create_heavy_lifter(version: str) -> HeavyLifter:
    """Serve as a factory. Create the required version of the HeavyLifter.

    Args:
        version: Version of the HeavyLifter.
    """
    # I could have created a HeavyLifterFactory class but
    # that would have been overkill for this task
    lifters = {
        'v1': HeavyLifterV1,
        'v2': HeavyLifterV2
    }
    return lifters[version]()
