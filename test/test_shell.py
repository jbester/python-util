import os.path
import shutil
import unittest
from .. import *
import io
import re
import tempfile


class ShellTest(unittest.TestCase):
    def test_chomp(self):
        # remove crlf
        self.assertEqual('hello', chomp("hello\r\n"))
        # remove cr
        self.assertEqual('hello', chomp("hello\r"))
        # remove lf
        self.assertEqual('hello', chomp("hello\n"))
        # ignore any string that doesn't have cr or lf
        self.assertEqual('hello', chomp("hello"))
        # ignore any crlf in the middle of the string
        self.assertEqual('hello\r\nhello', chomp("hello\r\nhello"))

    def test_warn(self):
        s = io.StringIO()
        warn("MSG", file=s)
        output = s.getvalue()
        match = re.fullmatch(r'^MSG at ([^ ]+) ([0-9]+)\n', output)
        # verify matches regex
        self.assertIsNotNone(match)
        # verify group 1 points to the file path
        self.assertIsNotNone(match.group(1))
        self.assertTrue(os.path.exists(match.group(1)))
        self.assertTrue(os.path.isfile(match.group(1)))

    def test_in_directory(self):
        """Verify in directory changes cwd"""
        temp_directory = os.path.realpath(tempfile.mkdtemp())
        # verify we aren't in the new temp folder
        self.assertNotEqual(os.getcwd(), temp_directory)
        # verify we *are* in the temp folder
        with in_directory(temp_directory):
            self.assertEqual(os.getcwd(), temp_directory)
        # verify we are back out
        self.assertNotEqual(os.getcwd(), temp_directory)
        shutil.rmtree(temp_directory, ignore_errors=True)

    def test_in_directory_exceptions(self):
        """Verify in directory changes curdirectory even with exceptions"""
        temp_directory = os.path.realpath(tempfile.mkdtemp())
        # verify we aren't in the temp folder
        self.assertNotEqual(os.getcwd(), temp_directory)
        try:
            # verify we *are* in the temp folder
            with in_directory(temp_directory):
                self.assertEqual(os.getcwd(), temp_directory)
        except Exception:
            pass
        # verify we aren't in the temp folder
        self.assertNotEqual(os.getcwd(), temp_directory)
        shutil.rmtree(temp_directory, ignore_errors=True)

    def test_directory_cleaned(self):
        """Verify directory cleaned after with block"""
        temp_directory = os.path.realpath(tempfile.mkdtemp())
        # verify temp directory exists
        self.assertTrue(os.path.isdir(temp_directory))
        self.assertTrue(os.path.exists(temp_directory))

        # directory will exist until the with block ends
        with directory_removed_after(temp_directory, ignore_errors=True):
            # create a new file
            file_path = os.path.join(temp_directory, 'a.txt')
            with open(file_path, 'w') as output:
                print("hello world", file=output)
            self.assertTrue(os.path.isfile(file_path))

        # verify temp file and directory is erased
        self.assertFalse(os.path.isdir(temp_directory))
        self.assertFalse(os.path.exists(temp_directory))
        self.assertFalse(os.path.exists(file_path))

    def test_file_removed_after(self):
        """Verify file cleaned after with block"""
        temp_directory = os.path.realpath(tempfile.mkdtemp())
        # create a path within the temp directory
        file_path = os.path.join(temp_directory, 'a.txt')
        # verify it doesn't exist
        self.assertFalse(os.path.exists(file_path))

        # file will be erased after the
        with file_removed_after(file_path):
            with open(file_path, 'w') as output:
                print("hello world", file=output)
            self.assertTrue(os.path.exists(file_path))
        self.assertFalse(os.path.exists(file_path))

        shutil.rmtree(temp_directory, ignore_errors=True)

if __name__ == '__main__':
    unittest.main()
