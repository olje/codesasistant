import unittest
from gpt_chat_bot.code_generator import CodeGenerator

class TestCodeGenerator(unittest.TestCase):

        def test_generate_python_code(self):
            instruction = "print('Hello, World!')"
            code = CodeGenerator.generate_python_code(instruction)
            self.assertEqual(code, instruction)

        def test_generate_bash_code(self):
            instruction = "echo 'Hello, World!'"
            code = CodeGenerator.generate_bash_code(instruction)
            self.assertEqual(code, instruction)

if __name__ == '__main__':
unittest.main()

