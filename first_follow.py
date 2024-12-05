grammar = {}
line = int(input())
start = 'S'
for i in range(line):
    x,y = (input().split("->"))
    if i==0:
        start = x
    y = list(y.split("|"))
    grammar[x] = y

first = {}
follow = {}

def calculate_first(symbol):
    if symbol in first:
        return first[symbol]

    first[symbol] = set()
    for production in grammar[symbol]:
        if production[0] not in grammar:
            first[symbol].add(production[0])

        else:
            first[symbol].update(calculate_first(production[0]))

    return first[symbol]

def calculate_follow(symbol, nextI):

    for non_terminal in grammar:
        for production in grammar[non_terminal]:

            if symbol in production:
                index = production.index(symbol)
                if index + nextI > len(production) - 1:
                    if symbol!=non_terminal:
                        if non_terminal not in follow:
                            follow[non_terminal] = set()
                        follow[symbol].update(calculate_follow(non_terminal, 1))
                else:
                    next_symbol = production[index + nextI]
                    if next_symbol not in grammar:
                        follow[symbol].add(next_symbol)
                    else:
                        follow[symbol].update(first[next_symbol])
                        if '#' in follow[symbol]:
                            follow[symbol].remove('#')
                            follow[symbol].update(calculate_follow(symbol, nextI+1))
    
    return follow[symbol]

follow[start] = set("$")
for symbol in grammar:
    calculate_first(symbol)
for symbol in grammar:
    if symbol!=start:
        follow[symbol] = set()
    calculate_follow(symbol, 1)

for symbol in grammar:
    print(f"FIRST({symbol}) = {first[symbol]}")
print()
for symbol in grammar:
    print(f"FOLLOW({symbol}) = {follow[symbol]}")