import attr

@attr.s
class Token:
    lexeme = attr.ib()
    token_class = attr.ib()

