import solution
import constants as c
import copy
class HILL_CLIMBER:
    def __init__(self):
        self.parent = solution.SOLUTION()
    
    def evolve(self):
        self.parent.evaluate('GUI')
        for gen in range(c.NUMBER_OF_GENERATIONS):
            self.evolve_for_one_generation()
        self.parent.evaluate('GUI')


    def evolve_for_one_generation(self):
        self.spawn()

        self.mutate()

        self.child.evaluate('DIRECT')

        print(f'\n\nFITNESS: parent: {self.parent.fitness} child: {self.child.fitness}\n')

        self.select()

    def spawn(self):
        self.child = copy.deepcopy(self.parent)

    def mutate(self):
        self.child.mutate()

    def select(self):
        if (self.parent.fitness > self.child.fitness):
            self.parent = self.child

