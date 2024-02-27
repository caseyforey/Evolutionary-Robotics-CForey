import solution
import constants as c
import copy
import os
import sys
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.clear_files()
        self.parents = {}
        self.next_available_id = 0
        for key in range(c.POPULATION):
            self.parents[key] = solution.SOLUTION(self.next_available_id)
            self.next_available_id+=1

    def clear_files(self):
        directory = os.path.dirname(os.path.realpath(__file__))
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            # checking if it is a file
            if os.path.isfile(f) :
                if (('.txt' in filename) | ('.nndf' in filename)):
                    os.system(f'del {filename}')

    def evolve(self):
        self.evaluate(self.parents)

        for parent in self.parents:
            self.evolve_for_one_generation()
        
        self.show_best()



    def evolve_for_one_generation(self):
    
        self.spawn()

        self.mutate()

        self.evaluate(self.children)

        self.Print()

        self.select()

    def spawn(self):
        self.children = {}
        for parent in self.parents:
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].set_id(self.next_available_id)
            self.next_available_id += 1

    def mutate(self):
        for child in self.children:
            self.children[child].mutate()

    def Print(self):
        for key in self.parents:
            print(f'\nFITNESS: parent: {self.parents[key].fitness} child: {self.children[key].fitness}\n')
    
    def evaluate(self, solutions):
        for idx in solutions:
            solutions[idx].start_simulation('DIRECT')
        
        for idx in solutions:
            solutions[idx].wait_for_simulation()

    def select(self):
        for key in self.parents:
            if (self.parents[key].fitness > self.children[key].fitness):
                self.parents[key] = self.children[key]

    def show_best(self):
        fitness = sys.float_info.max
        best_idx = None
        for key in self.parents:
            new_fit = self.parents[key].fitness
            if new_fit < fitness:
                fitness = new_fit
                best_idx = key
        self.parents[best_idx].start_simulation('GUI')

    
