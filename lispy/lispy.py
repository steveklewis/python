def tokenize(chars):
    "Convert a string of characters into a list of tokens."
    return chars.replace('(',' ( ').replace(')', ' ) ').split()

program = "(begin (define r 10) (* pi (* r r)))"
print tokenize(program)

