cards = []
cards.append({"color":"green",
              "shape":"oval",
              "number":2,
              "shading":"filled"})

cards.append({"color":"red",
              "shape":"oval",
              "number":3,
              "shading":"filled"})

cards.append({"color":"red",
              "shape":"oval",
              "number":1,
              "shading":"filled"})

features = ["color", "shading", "number", "shape"]
for feature in features:
    values = []
    for card in cards:
        values.append(card[feature])
    #print(values)
    if len(set(values))==len(values) or len(set(values))==1:
        pass
    else:
        print("Not a set")

#THE END
