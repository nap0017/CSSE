import unittest

import softwareprocess.dispatch as DP

class dispatch_predict_Test(unittest.TestCase):

# -----------------------------------------------------------------------
# ---- Acceptance Tests
#    dipatch function
#    Desired level of confidence:    boundary value analysis
#    Input-output Analysis
#        inputs:
#        outputs:
#    Happy path analysis:
#
#    Sad path analysis:
# {'op': 'predict'}  : Should return error






# Happy path










# Sad Path

    def test200_001_ShouldReturnError(self):
        sighting={'op': 'predict'}
        result={'error':'mandatory information is missing', 'op': 'predict'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])

    def test200_002_ShouldReturnError(self):
        sighting={'op':'predict', 'body': 'unknown', 'date': '2016-01-17', 'time': '03:15:42'}
        result={'op':'predict', 'body': 'unknown', 'date': '2016-01-17', 'time': '03:15:42', 'error':'star not in catalog'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])

    def test200_003_ShouldReturnDateError(self):
        sighting={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-99-17', 'time': '03:15:42'}
        result={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-99-17', 'time': '03:15:42', 'error':'invalid date'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])

    def test200_003_ShouldReturnDateError(self):
        sighting={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-99', 'time': '03:15:42'}
        result={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-99-17', 'time': '03:15:42', 'error':'invalid date'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])

