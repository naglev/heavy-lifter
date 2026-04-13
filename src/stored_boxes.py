class StoredBoxes:
    def __init__(self, starting_state: list[list[str]]):
        self._state = starting_state

    def __getitem__(self, index: int) -> list[str]:
        return self._state[index]

    @property
    def state(self) -> list[list[str]]:
        return self._state

    @property
    def top_boxes(self) -> str:
        # If this property is frequently accessed
        # then it should be cached
        output = ''
        for stack in self._state:
            output += stack[-1]
        return output
