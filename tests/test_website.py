"""
DevOpsPulse CI/CD Automated Test Suite
Executes during CI step on GitHub Actions runner.
"""

import os
import re
import unittest

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

class TestWebsiteStructure(unittest.TestCase):
    def setUp(self):
        self.index_path = os.path.join(PROJECT_ROOT, 'index.html')
        self.css_path = os.path.join(PROJECT_ROOT, 'assets', 'style.css')
        self.js_path = os.path.join(PROJECT_ROOT, 'assets', 'app.js')
        self.workflow_path = os.path.join(PROJECT_ROOT, '.github', 'workflows', 'deploy.yml')

        with open(self.index_path, 'r', encoding='utf-8') as f:
            self.html_content = f.read()

    def test_html_file_exists_and_not_empty(self):
        """Verify index.html exists and is non-empty."""
        self.assertTrue(os.path.exists(self.index_path), "index.html missing")
        self.assertGreater(len(self.html_content), 500, "index.html is too short or empty")

    def test_html5_standards(self):
        """Verify HTML5 standards compliance."""
        self.assertTrue(self.html_content.startswith('<!DOCTYPE html>'), "Missing HTML5 DOCTYPE declaration")
        self.assertIn('<meta charset="UTF-8">', self.html_content, "Missing UTF-8 charset declaration")
        self.assertIn('name="viewport"', self.html_content, "Missing responsive viewport meta tag")
        self.assertIn('<title>', self.html_content, "Missing page title tag")

    def test_assets_exist_and_linked(self):
        """Verify linked CSS and JS assets exist and are populated."""
        self.assertTrue(os.path.exists(self.css_path), "assets/style.css missing")
        self.assertTrue(os.path.exists(self.js_path), "assets/app.js missing")

        with open(self.css_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
        self.assertGreater(len(css_content), 100, "style.css is empty")

        with open(self.js_path, 'r', encoding='utf-8') as f:
            js_content = f.read()
        self.assertGreater(len(js_content), 100, "app.js is empty")

        self.assertIn('assets/style.css', self.html_content, "index.html does not link assets/style.css")
        self.assertIn('assets/app.js', self.html_content, "index.html does not link assets/app.js")

    def test_pipeline_stages_present(self):
        """Verify all 5 core CI/CD pipeline stages are defined."""
        stages = ['stage-trigger', 'stage-lint', 'stage-test', 'stage-build', 'stage-deploy']
        for stage in stages:
            self.assertIn(f'id="{stage}"', self.html_content, f"Missing pipeline stage element: {stage}")

    def test_metadata_hooks_present(self):
        """Verify build metadata placeholder hooks exist for CI replacement."""
        self.assertIn('id="build-id"', self.html_content, "Missing build-id hook")
        self.assertIn('id="commit-sha"', self.html_content, "Missing commit-sha hook")
        self.assertIn('id="deploy-time"', self.html_content, "Missing deploy-time hook")

    def test_github_actions_workflow_configuration(self):
        """Verify GitHub Actions deployment workflow is properly configured."""
        self.assertTrue(os.path.exists(self.workflow_path), ".github/workflows/deploy.yml is missing")
        with open(self.workflow_path, 'r', encoding='utf-8') as f:
            wf_content = f.read()

        # Check required workflow triggers and permissions
        self.assertIn('push:', wf_content, "Workflow must trigger on push")
        self.assertIn('pages: write', wf_content, "Workflow requires pages write permission")
        self.assertIn('actions/checkout', wf_content, "Workflow must checkout repository")
        self.assertIn('actions/deploy-pages', wf_content, "Workflow must deploy to GitHub Pages")

if __name__ == '__main__':
    unittest.main()
