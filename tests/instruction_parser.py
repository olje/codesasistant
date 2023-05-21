import unittest
from unittest.mock import patch, MagicMock
from gpt_chat_bot.instruction_parser import InstructionParser

class TestInstructionParser(unittest.TestCase):

        @patch('gpt_chat_bot.instruction_parser.GithubInterface')
        @patch('gpt_chat_bot.instruction_parser.CodeGenerator')
        def test_parse_instruction(self, mock_code_generator, mock_github_interface):
            mock_code_generator.generate_python_code.return_value = "print('Hello, World!')"
            ip = InstructionParser()
            ip.parse_instruction("Create python code print('Hello, World!') in repo")
            mock_code_generator.generate_python_code.assert_called_with("print('Hello, World!')")
            mock_github_interface().commit_code.assert_called_with("repo", "new_code.py", "GPT generated code", "print('Hello, World!')")

if __name__ == '__main__':
   unittest.main()

