from subprocess import call
from cookiecutter.main import cookiecutter
from cd import cd
import unittest
import os


TEST_DIR = '.temp'


class TestMake(unittest.TestCase):

    def setUp(self):
        """Bootstrap the project"""
        call(['mkdir', TEST_DIR])
        with cd(TEST_DIR):
            cookiecutter('../', no_input=True)

    def test_make(self):
        """Fire off make build"""
        with cd(TEST_DIR):
            p = os.path.join('./example_project', 'RunRules', 'Simulation')
            with cd(p):
                exit = call(['make', 'build'])
                assert(exit == 0)

    def tearDown(self):
        """Kill the temps"""
        call(['rm', '-fr', TEST_DIR])

if __name__ == '__main__':
    unittest.main()
