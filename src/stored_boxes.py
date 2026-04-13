class StoredBoxes:
    def __init__(self, starting_state):
        self._state = starting_state

    def __getitem__(self, index):
        return self._state[index]

    def show_top_boxes(self):
        output = ''
        for stack in self._state:
            output += stack[-1]
        return output

    @property
    def state(self):
        return self._state
