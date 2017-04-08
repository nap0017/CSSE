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



    def test100_001_ShouldReturnCalculatedLatitudeAnd(self):
        sighting={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42'}
        result={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42', 'long':'75d53.5', 'lat':'7d24.3'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['long'],mySample['long'])
        self.assertEqual(result['lat'],mySample['lat'])





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

    def test200_004_ShouldReturnDateError(self):
        sighting={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-99', 'time': '03:15:42'}
        result={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-99', 'time': '03:15:42', 'error':'invalid date'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])

    def test200_005_ShouldReturnDateError(self):
        sighting={'op':'predict', 'body': 'Betelgeuse', 'date': '2000-01-17', 'time': '03:15:42'}
        result={'op':'predict', 'body': 'Betelgeuse', 'date': '2000-01-17', 'time': '03:15:42', 'error':'invalid date'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])


    def test200_006_ShouldReturnDateError(self):
        sighting={'op':'predict', 'body': 'Betelgeuse', 'date': '2016/01/17', 'time': '03:15:42'}
        result={'op':'predict', 'body': 'Betelgeuse', 'date': '2016/01/17', 'time': '03:15:42', 'error':'invalid date'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])

    def test200_007_ShouldReturnTimeError(self):
        sighting={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:99:42'}
        result={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:99:42', 'error':'invalid time'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])

    def test200_008_ShouldReturnTimeError(self):
        sighting={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '99:15:10'}
        result={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '99:15:10', 'error':'invalid time'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])

    def test200_009_ShouldReturnTimeError(self):
        sighting={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:99'}
        result={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:99', 'error':'invalid time'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])


    def test200_010_ShouldReturnTimeError(self):
        sighting={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03.15.10'}
        result={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03.15.10', 'error':'invalid time'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])


    def test200_011_ShouldReturnTimeError(self):
        sighting={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42', 'long':'75d53.6', 'lat':'7d24.3'}
        result={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42', 'long':'75d53.6', 'lat':'7d24.3','error':'invalid input given(long)'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])

