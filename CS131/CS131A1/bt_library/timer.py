#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS131 - Artificial Intelligence
#
# Version 1.0.2 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
#

from .blackboard import Blackboard
from .common import NodeIdType, ResultEnum
from .decorator import Decorator
from .tree_node import TreeNode


class Timer(Decorator):
    """
    Specific implementation of the timer decorator.
    """
    TIMER_NOT_IN_USE = -1

    __time: int

    def __init__(self, time: int, child: TreeNode):
        """
        Default constructor.

        :time: Duration of the timer [counts]
        :param child: Child associated to the decorator
        """
        super().__init__(child)

        self.__time = time

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """
        # If there is no state for the timer or the timer is not in use,
        # the current time is what the timer decorator was defined with
        time_elapsed = self.additional_information(blackboard, Timer.TIMER_NOT_IN_USE)
        elapsed_time = time_elapsed if time_elapsed > Timer.TIMER_NOT_IN_USE else self.__time

        # Advance the time
        elapsed_time = elapsed_time - 1

        # If the timer expired, do not evaluate the child.
        # Just return immediately with a successful result
        if elapsed_time < 0:
            return self.report_succeeded(blackboard, Timer.TIMER_NOT_IN_USE)

        # Evaluate the child
        self.print_message(f"elapsed time = {elapsed_time}")
        result_child = self.child.run(blackboard)

        # If the child failed, terminate immediately the timer
        if result_child == ResultEnum.FAILED:
            return self.report_failed(blackboard, Timer.TIMER_NOT_IN_USE)

        return self.report_running(blackboard, elapsed_time)
