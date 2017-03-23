import unittest
import softwareprocess.dispatch as DP
import math


class dispatchTest(unittest.TestCase):

# -----------------------------------------------------------------------
# ---- Acceptance Tests
# 100 dipatch function
#    Desired level of confidence:    boundary value analysis
#    Input-output Analysis
#        inputs:
#        outputs:
#    Happy path analysis:
#           'op':'predict'
#           'op':'correct'
#           'op':'locale'
#    Sad path analysis:
#
# Happy path

    def test100_010_ShouldReturnSameDictionary(self):
        sighting={'op':'predict'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(sighting,mySample)
    def test100_010_ShouldReturnSameDictionary(self):
        sighting={'op':'predict'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(sighting,mySample)

# Sad Path
