produtos = [
    ["Top Gun", "True"], ["Ferdinando", "False"],
    ["Suits", "False"], ["TBL", "True"]]

tamanhoP = len(produtos)

true = []
false = []

for i in range(tamanhoP):
    p = produtos[i]
    t = p[1]
    if t == "False":
        false += [p]
    elif t == "True":
        true += [p]

print(f"True: {true}")
print(f"False: {false}")
