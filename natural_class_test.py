import unittest
from natural_class import is_set

class TestIsSet(unittest.TestCase):

       def test_allCards_differentValuesForAllFeatures_isSet(self):
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

              self.assertTrue(is_set(cards))

       def test_allCards_sameValuesForAllFeatures_isSet(self):
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
              self.assertTrue(is_set(cards))

       def test_allCards_differentValuesForTwoFeaturesAndSameValuesForOtherTwo_isSet(self):
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
              self.assertTrue(is_set(cards))


       def test_allCards_firstFeatureNotMeetSetCondition_isNotSet(self):


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
              self.assertFalse(is_set(cards))

       def test_allCards_lastFeatureNotMeetSetCondition_isNotSet(self):

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
              self.assertFalse(is_set(cards))

       def test_allCards_noFeatureMeetSetCondition_isNotSet(self):

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
              self.assertFalse(is_set(cards))

if __name__ == '__main__':
       unittest.main()