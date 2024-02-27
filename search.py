import os
import parallelHC
# for _ in range(5):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")

phc = parallelHC.PARALLEL_HILL_CLIMBER()
phc.evolve()