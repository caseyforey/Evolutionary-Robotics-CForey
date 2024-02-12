import numpy as np
import matplotlib.pyplot as mpl
backLegSensorValues = np.load('data/backleg.npy')
frontLegSensorValues = np.load('data/frontleg.npy')

backLegAngles = np.load('data/backlegAngles.npy')

frontLegAngles = np.load('data/frontlegAngles.npy')

#mpl.plot(backLegSensorValues, label = 'Back Leg', linewidth = 1.5)
#mpl.plot(frontLegSensorValues, label = 'Front Leg' , linewidth = 0.75)
mpl.plot(backLegAngles, label = 'back leg' , linewidth = 2)
mpl.plot(frontLegAngles, label = 'front leg' , linewidth = 0.75)

mpl.legend(loc = 1)
mpl.show()