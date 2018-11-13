def is_set(cards):  
  features = ["shading", "color", "number", "shape"]
  for feature in features:
      values = []
      for card in cards:
          values.append(card[feature])
      #print(values)
      if len(set(values))==len(values) or len(set(values))==1:
          pass
      else:
          return False
  return True        

#If cards have different values for all features, it should be a set.
cards = []
cards.append({"color":"green",
              "shape":"oval",
              "number":2,
              "shading":"filled"})

cards.append({"color":"red",
              "shape":"diamond",
              "number":3,
              "shading":"empty"})

cards.append({"color":"purple",
              "shape":"swirl",
              "number":1,
              "shading":"striped"})

print(is_set(cards))

#If cards have same values for all features, it should be a set.
cards = []
cards.append({"color":"green",
              "shape":"oval",
              "number":2,
              "shading":"filled"})

cards.append({"color":"green",
              "shape":"oval",
              "number":2,
              "shading":"filled"})

cards.append({"color":"green",
              "shape":"oval",
              "number":2,
              "shading":"filled"})

print(is_set(cards))

#If cards have different values for 2 features, and the same values for the other 2, it should be a set.
cards = []
cards.append({"color":"green",
              "shape":"oval",
              "number":2,
              "shading":"filled"})

cards.append({"color":"red",
              "shape":"oval",
              "number":3,
              "shading":"filled"})

cards.append({"color":"purple",
              "shape":"oval",
              "number":1,
              "shading":"filled"})

print(is_set(cards))

#If first feature doesn't meet set condition, it shouldn't be a set.
cards = []
cards.append({"color":"green",
              "shape":"oval",
              "number":2,
              "shading":"filled"})

cards.append({"color":"red",
              "shape":"oval",
              "number":3,
              "shading":"striped"})

cards.append({"color":"purple",
              "shape":"oval",
              "number":1,
              "shading":"filled"})

print(is_set(cards))

#If last feature doesn't meet set condition, it shouldn't be a set.
cards = []
cards.append({"color":"green",
              "shape":"oval",
              "number":2,
              "shading":"filled"})

cards.append({"color":"red",
              "shape":"oval",
              "number":3,
              "shading":"filled"})

cards.append({"color":"purple",
              "shape":"diamond",
              "number":1,
              "shading":"filled"})

print(is_set(cards))

#If no feature meets set condition, it shouldn't be a set.
cards = []
cards.append({"color":"green",
              "shape":"oval",
              "number":1,
              "shading":"empty"})

cards.append({"color":"red",
              "shape":"oval",
              "number":3,
              "shading":"filled"})

cards.append({"color":"green",
              "shape":"swirly",
              "number":1,
              "shading":"filled"})

print(is_set(cards))

