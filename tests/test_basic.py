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
        with cd(os.path.join(TEST_DIR, 'my-project')):
            call(['./manage.py', 'Sim'])
            with cd(os.path.join('RunRules', 'Sim')):
                exit = call(['make', 'build'])
                assert(exit == 0)

    def tearDown(self):
        """Kill the temps"""
        call(['rm', '-fr', TEST_DIR])

if __name__ == '__main__':
    unittest.main()
