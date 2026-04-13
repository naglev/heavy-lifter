class StoredBoxes:
    """Represents the current state of all box stacks.
    """
    def __init__(self, starting_state: list[list[str]]):
        """Initialize the stored boxes with a given starting state.

        Args:
            starting_state: A list of lists, where each sublist represents a stack of boxes.
        """
        self._state = starting_state

    def __getitem__(self, index: int) -> list[str]:
        """Get the stack of boxes at the specified index.

        Args:
            index: The index of the stack to retrieve.

        Returns:
            The list of boxes at the given stack index.
        """
        return self._state[index]

    @property
    def state(self) -> list[list[str]]:
        return self._state

    @property
    def top_boxes(self) -> str:
        """Get a string representing the top box of each stack.

        Returns:
            A string where each character is the top box from each stack.
        """
        # If this property is frequently accessed
        # then it should be cached
        output = ''
        for stack in self._state:
            output += stack[-1]
        return output
