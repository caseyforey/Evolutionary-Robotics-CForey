import solution
import constants as c
import copy
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}
        self.next_available_id = 0
        for key in range(c.POPULATION):
            self.parents[key] = solution.SOLUTION(self.next_available_id)
            self.next_available_id+=1
    
    def evolve(self):
        pass
        for parent in self.parents:
            self.parents[parent].start_simulation('GUI')
        # self.parent.evaluate('GUI')
        # for gen in range(c.NUMBER_OF_GENERATIONS):
        #     self.evolve_for_one_generation()
        # self.parent.evaluate('GUI')


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
        self.child.set_id(self.next_available_id)
        self.next_available_id += 1

    def select(self):
        if (self.parent.fitness > self.child.fitness):
            self.parent = self.child
