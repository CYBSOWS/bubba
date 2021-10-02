from either import Either

actual = 0
t = Either.right(actual)
assert t.get_right() == actual

actual = -1
t = Either.left(actual)
assert t.get_left() == actual

actual = "Foobar"
t = Either.right(actual)
t.map(lambda x : print(x))

t.fold(lambda x : print('?!'), lambda y : print(y))

