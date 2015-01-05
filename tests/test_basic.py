from subprocess import call
from cookiecutter.main import cookiecutter
import unittest
import os


TEST_DIR = '.temp'


class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = newPath

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


class TestBasic(unittest.TestCase):

    def setUp(self):
        call(['mkdir', TEST_DIR])

    def test_basic(self):
        with cd(TEST_DIR):
            cookiecutter('../', no_input=True)
            assert(os.path.isdir('./example_project'))

    def tearDown(self):
        call(['rm', '-fr', TEST_DIR])

if __name__ == '__main__':
    unittest.main()
