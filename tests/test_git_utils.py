import unittest
from gitwriter.git_utils import fetch_staged_git_changes, create_commit_message_from_diff

class TestGitUtils(unittest.TestCase):

    def test_get_git_diff_no_changes(self):
        # Simulate no changes
        diff = fetch_staged_git_changes()
        self.assertEqual(diff, "")

    def test_generate_commit_message(self):
        # Simulated git diff
        fake_diff = "diff --git a/file.txt b/file.txt\nindex e69de29..4b825dc 100644\n--- a/file.txt\n+++ b/file.txt\n@@ -0,0 +1 @@\n+Hello, World!"
        message = create_commit_message_from_diff(fake_diff)
        self.assertIsInstance(message, str)
        self.assertTrue(len(message) > 0)

if __name__ == '__main__':
    unittest.main()