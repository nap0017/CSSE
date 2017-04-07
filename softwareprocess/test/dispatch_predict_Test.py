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




