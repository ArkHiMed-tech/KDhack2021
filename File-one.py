class genetics:
    def __init__(self, sex):
        self.sex = sex

    def set_color_of_eyes(self, color):
        self.color_of_eyes = color

    def set_father(self, father):
        self.father_color_of_eyes = father.color_of_eyes

    def set_mother(self, mother):
        self.mother_color_of_eyes = mother.color_of_eyes

    def chance_of_color(self):
        if self.father_color_of_eyes == 'brown' and self.mother_color_of_eyes == 'brown':
            brown = 75
            green = 18.75
            blue = 6.25
        elif self.father_color_of_eyes == 'blue' and self.mother_color_of_eyes == 'blue':
            brown = 0
            green = 1
            blue = 99
        else:
            return 'Нестандартная ситуация.'
        return 'Шанс, что у ребенка будут карие глаза - {0}, зеленые глаза - {1}, голубые глаза - {2}.'.format(brown, green, blue)

father = genetics('men')
father.set_color_of_eyes('brown')
mother = genetics('woman')
mother.set_color_of_eyes('brown')
other_mother = genetics('woman')
other_mother.set_color_of_eyes('blue')

child = genetics('men')
child.set_father(father)
child.set_mother(mother)

print(child.chance_of_color())

child.set_mother(other_mother)

print(child.chance_of_color())
    
