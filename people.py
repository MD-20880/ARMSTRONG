class People:

    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def __str__(self):
        return self.name + ":" + self.skills
