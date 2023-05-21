mport unittest
from unittest.mock import patch, MagicMock
from gpt_chat_bot.github_interface import GithubInterface

class TestGithubInterface(unittest.TestCase):

        @patch('gpt_chat_bot.github_interface.Github')
            def test_commit_code(self, mock_github):
                mock_repo = MagicMock()
                mock_github().get_repo.return_value = mock_repo
                gi = GithubInterface()
                gi.commit_code("repo", "file", "message", "code")
                mock_github().get_repo.assert_called_with("repo")
                mock_repo.create_file.assert_called_with("file", "message", "code")

if __name__ == '__main__':
   unittest.main()

