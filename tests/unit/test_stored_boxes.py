from src.stored_boxes import StoredBoxes


def test_get_top_boxes():
    boxes = StoredBoxes([['P','A','K'],['U','Q'],['B'],['T','F']])
    assert boxes.top_boxes == 'KQBF'
