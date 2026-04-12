import abc


class HeavyLifter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def rearrange(self, boxes, instructions):
        raise NotImplementedError


class HeavyLifterV1(HeavyLifter):
    def rearrange(self, boxes, instructions):
        while instructions:
            inst = instructions.next_instruction()
            self._execute(boxes, inst)

    def _execute(self, boxes, instruction):
        for _ in range(instruction.number_of_boxes):
            try:
                box = boxes[instruction.source_stack - 1].pop()
            except IndexError:
                return
            boxes[instruction.destination_stack - 1].append(box)


class HeavyLifterV2(HeavyLifter):
    def rearrange(self, boxes, instructions):
        pass
