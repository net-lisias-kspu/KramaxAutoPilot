# Kramax Autopilot /L Unleashed

Kramax Autopilot is a course guidance and auto-land for spaceplanes.

[Unleashed](https://ksp.lisias.net/add-ons-unleashed/) fork by Lisias.


## In a Hurry

* [Latest Release](https://github.com/net-lisias-kspu/KramaxAutoPilot/releases)
* [Binaries](https://github.com/net-lisias-kspu/KramaxAutoPilot/tree/Archive)
* [Source](https://github.com/net-lisias-kspu/KramaxAutoPilot)
* [Issue Tracker](https://github.com/net-lisias-kspu/KramaxAutoPilot/issues)
* Documentation	
	+ [Project's README](https://github.com/net-lisias-kspu/KramaxAutoPilot/blob/master/README.md)
	+ [Install Instructions](https://github.com/net-lisias-kspu/KramaxAutoPilot/blob/master/INSTALL.md)
	+ [Change Log](./CHANGE_LOG.md)
	+ [TODO](./TODO.md) list


## Description

The original author some day started flying spaceplanes in Kerbal and discovered he could never land them successfully. His keyboard flying skills were sub-par. This despite him being an instrumented rated pilot of real planes.

He found a very good autopilot mod by [Crzyrndm](https://github.com/Crzyrndm) called "[Pilot Assistant](https://github.com/Crzyrndm/Pilot-Assistant)". But it did not have any course following abilities. He had taken the source code for Pilot Assistant and heavily modified it to add course guidance (both horizontal and vertical) so that it can autoland a spaceplane on the KSC runway. Many thanks to Crzyrndm -- this mod would never have happened without the excellent starting point. Note that he did not keep all the capabilities of Pilot Assistant -- he was very focused on auto-landing and things that were not really needed for that were omitted.

Flight plans can be loaded from configuration files located in the GameData folder. There is currently no capability to create new flight plans on the fly within the game, but you can edit the `GameData/KramaxAutoPilot/FlightPlans.cfg` file and add flight plans that way. Look at `GameData/KramaxAutoPilot/DefaultFlightPlans.cfg` for the format of the flight plans. The "Refresh" button on the flight plan load/save dialog will reload from that file so you do not have to restart the game every time you change a flight plan.

### Basic Instructions
You can use the autopilot to depart from KSC runway 09 as well as land on it. Here is a basic flight using the autopilot. You start lined up on KSC RW09.

### Departure
+ Show the autopilot window by selecting the airplane icon from your toolbar
+ Press the "Load/Store" button next to the "Flight Plan" button. This will display the flight plan loading window.
+ Select the plan named "KSC DEP 09". This is a flight plan that takes you straight out on a heading of 090 to space. You can close the flight plan loading window now.
+ Select the horizontal mode "NAV" and enable horizontal mode by selecting the button "Roll". The autopilot should track straight down the runway now.
+ It's suggested to use "pitch hold" mode for vertical control on departure. You can set this up for use after rotation by selecting the "Pitch" button and entering a desired pitch up amount (10-30 degrees, depending on your thrust to weight ratio).
+ Start your takeoff. It should track down the runway and after you liftoff, turn the vertical mode autopilot on by pressing the "Target Pitch" button. It should pitch up to your preset pitch value. It should retract your gear at 150m of altitude.
+ Now just control pitch angle to what works for your vehicle. When you get to high altitude where aerodynamics more or less stops, you should turn off the autopilot modes by pressing the "Roll" and "Vertical" buttons.
+ Hopefully you get to orbit

### Landing
+ You need to de-orbit. For KSC RW09, it was observed that when coming from an 80km orbit a 100m/s retrograde burn just before you get to the huge impact crater seems to work well. Depending on how fast your craft decelerates you may need to burn slightly earlier or later.
+ Setup the autopilot by loading the landing flight plan. You want to open the flight plan load/save window and select "KSC ILS 09" (ILS stands for "instrument landing system"). This flight plan has an initial point to aim for that is named "MAXKY". It is at 12000m, more or less on the equator about 75km West of KSC.
+ Descend into the atmo and try to stay on a heading of 090. You should generally be enable the autopilot around 20000m altitude. It's suggested to initially enable it in Bank mode (level) and pitch hold mode (4 to 6 degrees).
+ As you near 12000m altitude enable NAV mode and altitude hold of 12000m.
+ When you get very close to MAXKY, enable GS mode to follow the vertical guidance.
+ Now setup your landing speeds. Open up the "Approach Speeds" pane at the bottom. Change the speeds to match your craft. You want to land as slow as possible, so make your final speed something that is good margin above stall speed.
+ After passing MAXKY you can enable auto-throttle "Landing" mode to hold current speed and then decrease it to match the approach speeds as it heads for the next fixes.
+ At 500m (above ground) it should auto-lower your landing gear. But a good pilot makes sure he has 3-green before touching down! If all goes well it will cut your throttle right over the threshold, touchdown, and turn on max braking.


## Installation

Detailed installation instructions are now on its own file (see the [In a Hurry](#in-a-hurry) section) and on the distribution file.

### Attributions
This plugin is a heavily modified version of "Pilot Assistant" by Crzyrndm (<https://github.com/Crzyrndm/Pilot-Assistant>). At least half (if not more) of the code is his. Many thanks as to him, as this would never have been possible without it.

In addition, Kramer drew heavily on algorithms for calculating great circle routes from <http://www.movable-type.co.uk/scripts/latlong.html>. Many thanks for that information.

### License
This work is licensed under the [CC BY-NC-SA 4.0](https://creatLICENSE):

+ You are free to:
	- Share : copy and redistribute the material in any medium or format
	- Adapt : remix, transform, and build upon the material for any purpose, even commercially.
+ Under the following terms:
	- Attribution : You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in a ny reasonable manner, but not in any way that suggests the licensor endorses you or your use.
	- ShareAlike : If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

This work is a derivative of "Kramax Autopiot" by Kramer that was distributed under the same license., that is a derivative of "Pilot Assistant" by Crzyrndm that was also distributed under the very same license. 

Please note the copyrights and trademarks in [NOTICE](./NOTICE)


## UPSTREAM

* [Crzyrndm](https://forum.kerbalspaceprogram.com/index.php?/profile/92871-crzyrndm/): (Origin, not a fork)
	+ [Forum](https://forum.kerbalspaceprogram.com/index.php?/topic/90252-13-pilot-assistant-atmospheric-piloting-aids-1132-may-28/&) 
	+ [GitHub](https://github.com/Crzyrndm/Pilot-Assistant)
* [Kramer](https://forum.kerbalspaceprogram.com/index.php?/profile/151907-kramer/): ROOT
	+ [Forum](https://forum.kerbalspaceprogram.com/index.php?/topic/122258-104-kramax-autopilot-course-guidance-and-auto-land-for-spaceplanes-v02/)	 
	+ [GitHub](https://github.com/Kramax/KramaxAutoPilot))
* [LGG](https://forum.kerbalspaceprogram.com/index.php?/profile/129964-linuxgurugamer/): PARENT
	+ [Forum](https://forum.kerbalspaceprogram.com/index.php?/topic/150846-141-kramax-autopilot-continued-course-guidance-and-auto-land-for-spaceplanes/)
	+ [SpaceDock](https://spacedock.info/mod/1019/Kramax%20Autopilot%20Continued)
	+ [GitHub](https://github.com/linuxgurugamer/KramaxAutoPilot)
