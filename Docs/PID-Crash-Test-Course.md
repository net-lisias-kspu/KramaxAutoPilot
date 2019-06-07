@steve_v

https://forum.kerbalspaceprogram.com/index.php?/topic/150846-151-kramax-autopilot-continued-course-guidance-and-auto-land-for-spaceplanes/&do=findComment&comment=3599826

Kp: The proportional parameter controls the magnitude of the response to a given error value. E.g. in pitch hold mode, the change in elevator deflection applied per cycle is proportional to the difference between our current pitch and the setpoint (the error), multiplied by Kp.
Ki: The integral parameter increases the response proportional to the both magnitude of the error and the time for which it has persisted - in this example it corrects any steady-state offset in the final pitch achieved. The longer we're not at the right pitch, the harder it pulls on the stick.
Kd: The derivative parameter doesn't use the error value directly, instead it applies a  correction based on the rate of change of the error. It's there to control oscillation - if our actual pitch is close to and moving rapidly towards the setpoint, the D factor controls how much to back off so we don't overshoot.  Think D for damping.
Scalar: Divide all of the above values by this number, useful for those "Just chill the %@#$ out, airplane" situations.

Once you grok these, observe what your aircraft is doing in order to decide what to change:
If it's oscillating and those oscillations get worse over time, your control is unstable because it's applying excessively large corrections. Reduce Kp.
If it's oscillating and the oscillations are not getting worse (or getting better slowly), try increasing Kd to damp it out faster. If the oscillations are large, Kp might still be a little bit too high as well.
If your craft isn't oscillating, but it never gets quite to the heading/altitude you set, add a dash of Ki to nudge it the rest of the way. Ki is like salt, add only as much it needs.﻿


In the case of cascade control like Kramax, you will often have two PID controllers to play with per axis... Yeah, I know, bear with me.
Using vertical speed hold as an example, the "outer loop" as it is known (shown when you click the "PID" button) compares your current vertical speed to the setpoint and outputs the angle of attack required to correct it.
The "inner loop" (shown when you click the "Srf" button) takes the output of the outer loop as a setpoint and controls the elevators to try to put the craft at that angle.
The other control modes are similar: Heading and bank-angle, altitude and vertical speed, etc. The individual PID controllers are just assembled in different chains depending on the autopilot mode.

To determine which PID controller in a chain is causing your problems, open the inner loop settings and look at the "target" at the top. If the value is oscillating then it's a good bet the outer loop is the one that needs tuning, as that's where the value is coming from.
If that target value is fairly stable but the control surfaces on the aircraft are oscillating, t﻿hen it's the inner loop that is the problem.
