class Either:
    def __init__(self, right, left, isRight):
        self.right = right
        self.left = left
        self.isRight = isRight

    @staticmethod
    def left(left):
        return Either(None, left, False)

    @staticmethod
    def right(left):
        return Either(right, None, True)
