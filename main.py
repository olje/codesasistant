from codesasistant.instruction_parser import InstructionParser

def main():
        parser = InstructionParser()
        parser.parse_instruction("Create python code print('Hello, World!') in your_repo")

if __name__ == "__main__":
   main()

