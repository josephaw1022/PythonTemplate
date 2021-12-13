
import os ,sys , unittest
currentDir = os.path.dirname(os.path.realpath(__file__)) 
parentDir = os.path.dirname(currentDir)
sys.path.append(parentDir)

from Application import Application



class TestingApplication(unittest.TestCase):
    """Testing Class

    - Very basic unit test
    - Meant to be more of a starting place and not something configured
    
    """

    def test_add(self):
        self.assertEqual(Application().welcomeMessage, "Delete me and get started on your project!")





if __name__=='__main__':
    unittest.main()