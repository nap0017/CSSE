import unittest

import softwareprocess.dispatch as DP

class dispatch_correct_Test(unittest.TestCase):

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
# {'op': 'correct'}  : Should return error


# Happy path



    def test100_001_ShouldReturnCorrectedDistanceAndAzimuth(self):
        sighting={'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        result={'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'correctedDistance':'3950', 'correctedAzimuth':'164d42.9'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['correctedDistance'],mySample['correctedDistance'])
        self.assertEqual(result['correctedAzimuth'],mySample['correctedAzimuth'])

    def test100_002_ShouldReturnCorrectedDistanceAndAzimuth(self):
        sighting={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4',  'assumedLat':'35d59.7', 'assumedLong':'74d35.3'}
        result={'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':'74d35.3', 'correctedDistance':'104', 'correctedAzimuth':'0d36.8'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['correctedDistance'],mySample['correctedDistance'])
        self.assertEqual(result['correctedAzimuth'],mySample['correctedAzimuth'])





# Sad Path

    def test200_001_ShouldReturnError(self):
        sighting={'op': 'correct'}
        result={'error':'mandatory information is missing', 'op': 'correct'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])

    def test200_002_ShouldReturnError(self):
        sighting={'op':'correct', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        result={'error':'mandatory information is missing', 'op':'correct', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])

    def test200_003_ShouldReturnError(self):
        sighting={'op':'correct','lat': 16 , 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        result={'error':'invalid lat', 'op':'correct','lat': 16 , 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])

    def test200_004_ShouldReturnError(self):
        sighting={'op':'correct','lat':'16d32.3' , 'long':'95d41.6', 'altitude':15,  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        result={'error':'invalid altitude', 'op':'correct','lat':'16d32.3' , 'long':'95d41.6', 'altitude':15,  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])

    def test200_005_ShouldReturnError(self):
        sighting={'op':'correct', 'lat':'16.0d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        result={'error':'invalid lat','op':'correct', 'lat':'16.0d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])

    def test200_006_ShouldReturnError(self):
        sighting={'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-153d38.4', 'assumedLong':'74d35.3'}
        result={'error':'invalid assumedlat','op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-153d38.4', 'assumedLong':'74d35.3'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])

    def test200_007_ShouldReturnError(self):
        sighting={'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-70d38.4', 'assumedLong':'-74d35.3'}
        result={'error':'invalid assumedlong','op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-70d38.4', 'assumedLong':'-74d35.3'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])

    def test200_008_ShouldReturnError(self):
        sighting={'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'-13d42.3',  'assumedLat':'-70d38.4', 'assumedLong':'74d35.3'}
        result={'error':'invalid altitude','op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'-13d42.3',  'assumedLat':'-70d38.4', 'assumedLong':'74d35.3'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])

    def test200_009_ShouldReturnError(self):
        sighting={'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':'74d35.3','correctedDistance':'3950'}
        result={'error':'invalid input correctedDistance','op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])

    def test200_010_ShouldReturnError(self):
        sighting={'op':'correct', 'lat':'16d32..3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        result={'error':'invalid lat','op':'correct', 'lat':'16d32..3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])


    def test200_011_ShouldReturnError(self):
        sighting={'op':'correct', 'lat':'1632.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        result={'error':'invalid lat','op':'correct', 'lat':'16d32..3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        mySample = DP.dispatch(sighting)
        self.assertEqual(result['error'],mySample['error'])

