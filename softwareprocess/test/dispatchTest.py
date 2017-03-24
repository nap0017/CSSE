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
        result={'op':'predict'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result,mySample)
    def test100_020_ShouldReturnSameDictionary(self):
        sighting={'op':'predict','observation':'015d04.9', 'height':'6.0'}
        result={'op':'predict','observation':'015d04.9', 'height':'6.0'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result,mySample)
    def test100_030_ShouldReturnSameDictionary(self):
        sighting={'op':'correct'}
        result={'op':'correct'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result,mySample)
    def test100_040_ShouldReturnSameDictionary(self):
        sighting={'op':'correct','observation':'015d04.9', 'height':'6.0'}
        result={'op':'correct','observation':'015d04.9', 'height':'6.0'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result,mySample)
    def test100_050_ShouldReturnSameDictionary(self):
        sighting={'op':'locale'}
        result={'op':'locale'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result,mySample)
    def test100_060_ShouldReturnSameDictionary(self):
        sighting={'op':'locale','observation':'015d04.9', 'height':'6.0'}
        result={'op':'locale','observation':'015d04.9', 'height':'6.0'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result,mySample)

# Sad Path
    def test200_010_ShouldReturnError(self):
        sighting={}
        result={'error':'no op  is specified'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result,mySample)
