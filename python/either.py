class Either:
    def __init__(self, right, left, isRight):
        self.right = right
        self.left = left
        self.isRight = isRight

    def get_right(self):
        if not isRight:
            raise Exception('Either: guard call with Either#is_right')
        return self.right

    def get_left(self):
        if isRight:
            raise Exception('Either: guard call with Either#is_left')
        return self.right

    def is_right(self):
        return self.isRight

    def is_left(self):
        return not self.isRight

    @staticmethod
    def left(left):
        return Either(None, left, False)

    @staticmethod
    def right(left):
        return Either(right, None, True)
