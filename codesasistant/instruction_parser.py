
from codesasistant.github_interface import GithubInterface
from codesasistant.code_generator import CodeGenerator

class InstructionParser:

        def __init__(self):
            self.github_interface = GithubInterface()

        def parse_instruction(self, instruction):
            # This is a simplified parser that expects instructions in the format: "Create python code {code} in {repo}"
            split_instruction = instruction.split(" ")

            if "python" in split_instruction:
               code = CodeGenerator.generate_python_code(" ".join(split_instruction[3:-2]))
               self.github_interface.commit_code(split_instruction[-1], "new_code.py", "GPT generated code", code)
            elif "bash" in split_instruction:
                 code = CodeGenerator.generate_bash_code(" ".join(split_instruction[3:-2]))
                 self.github_interface.commit_code(split_instruction[-1], "new_code.sh", "GPT generated code", code)

