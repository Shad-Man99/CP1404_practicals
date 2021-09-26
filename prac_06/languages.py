from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # For loop for printing names with dynamic typing

    program_languages = [ruby, python, visual_basic]
    print(program_languages)
    print("The dynamically typed languages are:")


main()