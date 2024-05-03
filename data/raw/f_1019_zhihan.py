import os
import glob
import zipfile


def f_1019(directory):
    """
    Zips all files located in the specified directory and returns the path to the created zip file.
    
    Parameters:
    directory (str): The directory path containing the files to be zipped.
    
    Returns:
    str: The path to the generated zip file, or None if the directory is empty.
    
    Requirements:
    - os
    - glob
    - zipfile
    
    Example:
    >>> f_1019('/path/to/files')
    '/path/to/files/files.zip'
    """
    # Check if directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' not found.")

    # Get all files (excluding directories) in the specified directory
    files = [f for f in glob.glob(os.path.join(directory, '*')) if os.path.isfile(f)]

    # If directory is empty or only contains sub-directories, return None
    if not files:
        return None

    # Define the zip file path
    zip_file_path = os.path.join(directory, 'files.zip')

    # Create a new zip file and add all files into it
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))

    return zip_file_path


import unittest
import os
import tempfile
import zipfile


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)

    def test_case_1(self):
        with open(os.path.join(self.test_dir, "testfile1.txt"), "w") as f:
            f.write("This is a test file.")
        zip_path = f_1019(self.test_dir)
        self.assertTrue(os.path.exists(zip_path))

    def test_case_2(self):
        for i in range(5):
            with open(os.path.join(self.test_dir, f"testfile{i}.txt"), "w") as f:
                f.write(f"This is test file {i}.")
        zip_path = f_1019(self.test_dir)
        self.assertTrue(os.path.exists(zip_path))

    def test_case_3(self):
        zip_path = f_1019(self.test_dir)
        self.assertIsNone(zip_path)

    def test_case_4(self):
        with self.assertRaises(FileNotFoundError):
            f_1019("/non/existent/directory")

    def test_case_5(self):
        os.makedirs(os.path.join(self.test_dir, "subdir"))
        with open(os.path.join(self.test_dir, "testfile.txt"), "w") as f:
            f.write("This is a test file.")
        zip_path = f_1019(self.test_dir)
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            self.assertEqual(len(zipf.namelist()), 1)


if __name__ == "__main__":
    run_tests()
