def is_set(cards):  
  features = ["shading", "color", "number", "shape"]
  for feature in features:
      unique_values = set()
      for card in cards:
        unique_values.add(card[feature])
      #TODO: return error if len(u_v) == 0 or if len(u_v) > len(cards)
      if 1 < len(unique_values) < len(cards):
        return False              
  return True
