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
        sighting={'op':'locate'}
        result={'op':'locate'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result,mySample)
    def test100_060_ShouldReturnSameDictionary(self):
        sighting={'op':'locate','observation':'015d04.9', 'height':'6.0'}
        result={'op':'locate','observation':'015d04.9', 'height':'6.0'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result,mySample)

# Sad Path
    def test200_010_ShouldReturnError(self):
        sighting={}
        result={'error':'no op  is specified'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result,mySample)
    def test200_020_ShouldReturnError(self):
        sighting={'observation': '15d04.9', 'height': '6.0', 'pressure': '1010', 'horizon': 'artificial', 'temperature': '72'}
        result={'error': 'no op  is specified'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])
    def test200_020_ShouldReturnError(self):
        sighting=42
        result={'error': 'parameter is not a dictionary'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])
