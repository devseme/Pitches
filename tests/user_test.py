import unittest

from app.models import User
class UserTest(unittest.TestCase):
    '''
    Test class to test our user class
    '''
    
    def setUp(self):
        '''
        set up method that will run before other tests
        '''
        self.new_user = User(username ='ian',password='qwerty')

    def test_passwor_setter(self):
        self.assertTrue(self.new_user.password is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password
    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('qwerty'))                
        