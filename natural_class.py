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