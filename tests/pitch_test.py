import unittest
from app.models import Pitch

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch(id=50,title='first pitch',content='we can carry out pitches',category ='political aspirations',user_id= 10)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))