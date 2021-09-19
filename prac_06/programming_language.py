class ProgramLanguage:

    def __init__(self, name, type, reflection, year):
        self.name = name
        self.type = type
        self.reflection = reflection
        self.year = year

    def__str__(self):
    return "{}, {} Dynamic Typing, {}=Reflection, First appeared in {}".format(self.name, self.type, self.reflection,
    self.year)

    program_langauges = [ruby, python, visual_basic]
    print(program_languages)
    print("The dynamically typed languages are:")


