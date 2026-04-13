from src.stored_boxes import StoredBoxes


def test_show_top_boxes():
    boxes = StoredBoxes([['P','A','K'],['U','Q'],['B'],['T','F']])
    assert boxes.show_top_boxes() == 'KQBF'
    