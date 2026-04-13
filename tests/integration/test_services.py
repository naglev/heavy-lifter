from pathlib import Path

from src.services import do_the_heavy_lifting


def test_heavy_lifting_use_case():
    path = Path(__file__).parent.joinpath('instruction_set_test.txt')
    heavy_lifter_version = 'v1'

    output = do_the_heavy_lifting(path, heavy_lifter_version)

    assert output == 'FPAT'
