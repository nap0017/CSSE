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
       # self.assertEqual(sighting,mySample)
        self.assertEqual('predict', mySample['op'])
    def test100_020_ShouldReturnSameDictionary(self):
        sighting={'op':'correct'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(sighting,mySample)
    def test100_030_ShouldReturnSameDictionary(self):
        sighting={'op':'locale'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(sighting,mySample)
    def test100_040_ShouldReturnError(self):
        sighting={}
        result={'error':'no op  is specified'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result,mySample)
