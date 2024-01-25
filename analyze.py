import numpy as np
import matplotlib.pyplot as mpl
backLegSensorValues = np.load('data/backleg.npy')
frontLegSensorValues = np.load('data/frontleg.npy')

mpl.plot(backLegSensorValues, label = 'Back Leg', linewidth = 1.5)
mpl.plot(frontLegSensorValues, label = 'Front Leg' , linewidth = 0.75)

mpl.legend(loc = 1)
mpl.show()