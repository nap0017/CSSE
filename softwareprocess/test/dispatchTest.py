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

    def test400_010_ShouldReturnCalculatedAltitude(self):
        sighting={'op':'adjust','observation': '10d0.0','height':'6.0','horizon':'artificial','pressure':'1010','temperature':'72'}
        result={'altitude':'9d54.7'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['altitude'],mySample['altitude'])
    def test400_020_ShouldReturnCalculatedAltitude(self):
        sighting={'op':'adjust','observation': '45d15.2','height':'6.0','horizon':'natural','pressure':'1010','temperature':'71'}
        result={'altitude':'45d11.7'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['altitude'],mySample['altitude'])



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
    def test200_030_ShouldReturnError(self):
        sighting=42
        result={'error': 'parameter is not a dictionary'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])
    def test200_040_ShouldReturnError(self):
        sighting={'op': 'unknown'}
        result={'error': 'op is not a legal operation'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])
    def test200_050_ShouldReturnError(self):
        sighting=None
        result={'error': 'parameter is missing'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])
    def test200_060_ShouldReturnError(self):
        sighting={'op':'adjust'}
        result={'error': 'mandatory information is missing'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])
    def test200_070_ShouldReturnError(self):
        sighting={'op':'adjust','observation': '101'}
        result={'error': 'observation is invalid'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])
    def test200_080_ShouldReturnError(self):
        sighting={'op':'adjust','observation': '101d'}
        result={'error': 'observation is invalid'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])
    def test200_090_ShouldReturnError(self):
        sighting={'op':'adjust','observation': '80d61.0'}
        result={'error': 'observation is invalid'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])
    def test300_010_ShouldReturnError(self):
        sighting={'op':'adjust','observation': '80d59.0','height':'20a'}
        result={'error': 'height is invalid'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])
    def test300_020_ShouldReturnError(self):
        sighting={'op':'adjust','observation': '80d59.0','height':'20','temperature':'10a'}
        result={'error': 'temperature is invalid'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])
    def test300_030_ShouldReturnError(self):
        sighting={'op':'adjust','observation': '80d59.0','height':'20','temperature':'10','pressure':'10a'}
        result={'error': 'pressure is invalid'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])
    def test300_040_ShouldReturnError(self):
        sighting={'op':'adjust','observation': '80d59.0','height':'20','temperature':'10','pressure':'100','horizon':'10a'}
        result={'error': 'horizon is invalid'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])
