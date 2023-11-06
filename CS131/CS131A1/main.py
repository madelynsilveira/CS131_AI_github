#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS131 - Artificial Intelligence
#
# version 1.0.2 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
#

import bt_library as btl

from battery_less_than_30 import BatteryLessThan30
from find_home import FindHome, GoHome, Dock
from spot_clean import Spot, CleanSpot, DoneSpot
from gen_clean import General, DustySpot, CleanFloor, DoneGeneral
from nothing import DoNothing
from globals import BATTERY_LEVEL, GENERAL_CLEANING, SPOT_CLEANING, DUSTY_SPOT_SENSOR, HOME_PATH

# Instantiation of the tree.
battery = btl.Sequence([
    BatteryLessThan30(),
    FindHome(),
    GoHome(),
    Dock()
])

spots = btl.Sequence([
    Spot(),
    btl.Timer(20, CleanSpot()),
    DoneSpot()
])

dusty = btl.Priority([
    btl.Sequence([
        DustySpot(),
        btl.Timer(35, CleanSpot())]), #should return running until done
    CleanFloor() # TODO: until failure
])

general = btl.Sequence([
    General(),
    btl.Selection([
        dusty,
        DoneGeneral()])
])

tree_root = btl.Priority([
    battery,
    btl.Selection([
        spots,
        general]),
    DoNothing()
])


# Main body of the assignment
current_blackboard = btl.Blackboard()
current_blackboard.set_in_environment(BATTERY_LEVEL, 29)
current_blackboard.set_in_environment(SPOT_CLEANING, False)
current_blackboard.set_in_environment(GENERAL_CLEANING, True)
current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, False)
current_blackboard.set_in_environment(HOME_PATH, "")

cycles = 50
while cycles > 0:
    # Make cycles easier to read
    print('\nCYCLE NUMBER ' + str(51 - cycles))

    # Evaluating the tree
    result = tree_root.run(current_blackboard)

    # Changing the environment
    battery = current_blackboard.get_in_environment(BATTERY_LEVEL, 31) - 1
    current_blackboard.set_in_environment(BATTERY_LEVEL, battery)
    cycles = cycles - 1




