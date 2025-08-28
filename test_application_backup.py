import unittest
import os
import sys

class TestTalentVibeApplication(unittest.TestCase):
    
    def test_application_file_exists(self):
        """Test that the main application file exists"""
        self.assertTrue(os.path.exists('application.py'), "application.py should exist")
    
    def test_requirements_file_exists(self):
        """Test that requirements.txt exists"""
        self.assertTrue(os.path.exists('requirements.txt'), "requirements.txt should exist")
    
    def test_frontend_directory_exists(self):
        """Test that frontend directory exists"""
        self.assertTrue(os.path.exists('frontend'), "frontend directory should exist")
    
    def test_ebextensions_directory_exists(self):
        """Test that .ebextensions directory exists"""
        self.assertTrue(os.path.exists('.ebextensions'), ".ebextensions directory should exist")
    
    def test_upload_page_exists(self):
        """Test that UploadPage.js exists"""
        upload_page_path = os.path.join('frontend', 'src', 'UploadPage.js')
        self.assertTrue(os.path.exists(upload_page_path), "UploadPage.js should exist")
    
    def test_file_dropzone_component_exists(self):
        """Test that FileDropZone component exists"""
        dropzone_path = os.path.join('frontend', 'src', 'components', 'FileDropZone.js')
        self.assertTrue(os.path.exists(dropzone_path), "FileDropZone.js should exist")
    
    def test_progress_bar_component_exists(self):
        """Test that ResumeProgressBar component exists"""
        progress_bar_path = os.path.join('frontend', 'src', 'components', 'ResumeProgressBar.js')
        self.assertTrue(os.path.exists(progress_bar_path), "ResumeProgressBar.js should exist")
    
    def test_application_import(self):
        """Test that application.py can be imported"""
        try:
            # Add current directory to path
            sys.path.insert(0, os.getcwd())
            import application
            self.assertTrue(hasattr(application, 'app'), "application should have 'app' attribute")
        except ImportError as e:
            self.fail(f"Failed to import application: {e}")
    
    def test_api_endpoints_exist(self):
        """Test that new API endpoints are defined"""
        try:
            with open('application.py', 'r') as f:
                content = f.read()
                self.assertIn('/api/jd/check', content, "JD check endpoint should exist")
                self.assertIn('/api/resumes/check-duplicates', content, "Duplicate check endpoint should exist")
        except FileNotFoundError:
            self.fail("application.py not found")

if __name__ == '__main__':
    unittest.main()
