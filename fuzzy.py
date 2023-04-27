import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define the input variables
distance = ctrl.Antecedent(np.arange(0, 100, 1), 'distance')
speed = ctrl.Antecedent(np.arange(0, 100, 1), 'speed')

# Define the output variable
braking_force = ctrl.Consequent(np.arange(0, 101, 1), 'braking_force')

# Define the membership functions for the input variables
distance['near'] = fuzz.trimf(distance.universe, [0, 0, 50])
distance['medium'] = fuzz.trimf(distance.universe, [0, 50, 100])
distance['far'] = fuzz.trimf(distance.universe, [50, 100, 100])

speed['low'] = fuzz.trimf(speed.universe, [0, 0, 50])
speed['medium'] = fuzz.trimf(speed.universe, [0, 50, 100])
speed['high'] = fuzz.trimf(speed.universe, [50, 100, 100])

# Define the membership functions for the output variable
braking_force['none'] = fuzz.trimf(braking_force.universe, [0, 0, 0])
braking_force['low'] = fuzz.trimf(braking_force.universe, [0, 20, 40])
braking_force['medium'] = fuzz.trimf(braking_force.universe, [20, 50, 80])
braking_force['high'] = fuzz.trimf(braking_force.universe, [50, 100, 100])

# Define the fuzzy rules
rule1 = ctrl.Rule(distance['near'] & speed['low'], braking_force['high'])
rule2 = ctrl.Rule(distance['near'] & speed['medium'], braking_force['medium'])
rule3 = ctrl.Rule(distance['near'] & speed['high'], braking_force['low'])
rule4 = ctrl.Rule(distance['medium'] & speed['low'], braking_force['high'])
rule5 = ctrl.Rule(distance['medium'] & speed['medium'], braking_force['medium'])
rule6 = ctrl.Rule(distance['medium'] & speed['high'], braking_force['low'])
rule7 = ctrl.Rule(distance['far'] & speed['low'], braking_force['high'])
rule8 = ctrl.Rule(distance['far'] & speed['medium'], braking_force['low'])
rule9 = ctrl.Rule(distance['far'] & speed['high'], braking_force['none'])

# Create the control system
braking_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])

# Create the control system simulation
braking_simulation = ctrl.ControlSystemSimulation(braking_ctrl)

# Set the input values
braking_simulation.input['distance'] = 70
braking_simulation.input['speed'] = 80

# Evaluate the system
braking_simulation.compute()

# Print the output value
print(braking_simulation.output['braking_force'])
