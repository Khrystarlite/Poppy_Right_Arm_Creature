from numpy import mean
from collections import deque

from pypot.primitive import LoopPrimitive


class ArmsTurnCompliant(LoopPrimitive):
    """ Automatically turns the arms compliant when a force is applied. """
    def setup(self):
        for m in self.robot.arms:
            m.compliant = False
            m.torque_limit = 20

        freq = 1. / self.period
        self.r_arm_torque = deque([0], 0.2 * freq)

    def update(self):
        for side in ('r'):
            recent_arm_torques = getattr(self, '{}_arm_torque'.format(side))
            motors = getattr(self.robot, '{}_arm'.format(side))

            recent_arm_torques.append(max([abs(m.present_load) for m in motors]))

            mt = mean(recent_arm_torques)

            if mt > 20:
                for m in motors:
                    m.compliant = True
            elif mt < 7:
                for m in motors:
                    m.compliant = False

