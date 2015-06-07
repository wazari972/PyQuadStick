'''
logitech.py - Python class for Logitech joysticks

    Copyright (C) 2014 Simon D. Levy

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as 
    published by the Free Software Foundation, either version 3 of the 
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

'''

from quadstick.game import Game

import time

class ExtremePro3D(Game):

    def __init__(self, jsid=0, hidden=False):
        '''
        Creates a new ExtremePro3D object.
        '''
        Game.__init__(self, 'Logitech Extreme 3D Pro', jsid, hidden)

        self.trigger_is_down = False

        self.yaw_axis = 3 if self.platform == 'Windows' else 2

        self.holdbutton = 1
        self.autobutton = 0

    def _startup_message(self):

        return 'Please cycle throttle to begin.'

    def _get_axis3(self):

        Game._pump(self)   
        return self.joystick.get_axis(3) 
 

    def poll(self):
        '''
        Polls the Logitech joystick:

          Foward/back      : Pitch
          Side-to-side     : Roll
          Twist:           : Yaw
          Throttle         : Climb/descend
          Trigger:         : Toggle autopilot

        Altitude and position hold are always on.

        Returns demands (pitch, roll, yaw, throttle) and switches (pos-hold, alt-hold, autopilot).
        '''

        return Game._poll(self)

    def _get_pitch(self):
    
        return Game._get_axis(self, 1)

    def _get_roll(self):
    
        return -Game._get_axis(self, 0)

    def _get_yaw(self):

        return Game._get_axis(self, self.yaw_axis)

    def _get_throttle(self):

        return (-self._get_axis3() + 1) / 2