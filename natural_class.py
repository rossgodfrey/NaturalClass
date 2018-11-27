def is_set(cards):  
  features = ["shading", "color", "number", "shape"]
  for feature in features:
      unique_values = set()
      for card in cards:
          unique_values.add(card[feature])
      if not (len(unique_values)==len(cards) or len(unique_values)==1):
          return False              
  return True