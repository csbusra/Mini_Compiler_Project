grammar = input()
left, right = grammar.split("->")
right = right.split("|")

alpha = []
beta = []

for r in right:
  if r.startswith(left):
    alpha.append(r[1:])
  else:
    beta.append(r)

for i in range(len(alpha)):
  alpha[i] = alpha[i]+left+"'"
alpha.append("ε")

for i in range(len(beta)):
  beta[i] = beta[i]+left+"'"


print("After elimination of left recursion the grammar is:")
print(left+" -> "+"|".join(beta))
print(left+"'"+" -> "+"|".join(alpha))