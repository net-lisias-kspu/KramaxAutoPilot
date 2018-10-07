# Source:
#   https://forum.kerbalspaceprogram.com/index.php?/topic/157544-python-kramax-flight-plan-filer/&
#   by Aerostar Research

flightplan = ""

# nav database
waypoints = {
"MAXKY":"""    WayPoint
        {
            Vertical = true
            lat = -0.0485981
            lon = -82.25
            alt = 12000
            name = MAXKY
        }
        """,
"HIKEY":"""    WayPoint
        {
            Vertical = true
            lat = -0.0485981
            lon = -81.25
            alt = 10000
            name = HIKEY
        }
        """,
"LOKEY":"""     WayPoint
        {
        Vertical = true
            lat = -0.0485981
            lon = -79.25
            alt = 6500
            name = LOKEY
        }
        """,
"KSC 09 APP":"""    WayPoint
        {
                Vertical = true
                IAF = true
                lat = -0.0485981
                lon = -77.25
                alt = 2500
                name = KSC 09 IAF
        }
        WayPoint
        {
                Vertical = true
                FAF = true
                lat = -0.0485981
                lon = -76.1
                alt = 1000
                name = KSC 09 FAF
        }
        WayPoint
        {
                Vertical = true
                RW = true
                lat = -0.0485981
                lon = -74.7359549847328
                alt = 97
                name = KSC RW09 FLARE
        }
        WayPoint
        {
                Vertical = true
                Stop = true
                lat = -0.050185
                lon = -74.4947394
                alt = 67
                name = KSC RW09 STOP
        }
        """,
"KSC 27 APP":"""    WayPoint
        {
                Vertical = true
                IAF = true
                lat = -0.0582111
                lon = -71.75
                alt = 2500
                name = KSC 27 IAF
        }
        WayPoint
        {
                Vertical = true
                FAF = true
                lat = -0.0582111
                lon = -73.25
                alt = 1000
                name = KSC 27 FAF
        }
        WayPoint
        {
                Vertical = true
                RW = true
                lat = -0.050185
                lon = -74.47
                alt = 110
                name = KSC RW27 FLARE
        }
        WayPoint
        {
                Vertical = true
                Stop = true
                lat = -0.0485981
                lon = -74.73595
                alt = 67
                name = KSC RW27 STOP
        }
        """,
"WP_EAST":"""    WayPoint
        {
                Vertical = true
                lat = -0.050185
                lon = -73.2137677633588
                alt = 3000
                name = WP_EAST
        }
        """,
"WP_NORTH":"""    WayPoint
        {
                Vertical = true
                lat = 1.6
                lon = -73.2
                alt = 5000
                name = WP_NORTH
        }
        """,
"WP_WEST":"""    WayPoint
        {
                Vertical = true
                lat = -0.0485981
                lon = -84.5
                alt = 10000
                name = WP_WEST
        }   				
        """,
"WP_NW":"""    WayPoint
        {
                Vertical = true
                lat = 1.0
                lon = -84.5
                alt = 10000
                name = WP_NW
        }   		
        """,
"BONZO":"""    WayPoint
        {
                Vertical = true
                lat = 1.404013473282443
                lon = -76.8763631832061
                alt = 5000
                name = BONZO
        }
        """,
"ISLAND 09 APP":"""    WayPoint
        {
                Vertical = true
                IAF = true
                lat = -1.5173
                lon = -74
                alt = 2000
                name = ISLAND IAF
        }
        WayPoint
        {
                Vertical = true
                FAF = true
                lat = -1.52938
                lon = -73
                alt = 1000
                name = ISLAND FAF
        }
        WayPoint
        {
                Vertical = true
                RW = true
                lat = -1.5173
                lon = -71.975
                alt = 150
                name = ISLAND RW
        }
        WayPoint
        {
                Vertical = true
                Stop = true
                lat = -1.51598
                lon = -71.85241
                alt = 132
                name = ISLAND RW STOP
        }
        """,
"KIS":"""    WayPoint
        {
            Vertical = false
            lat = -1.52
            lon = -71.9""",
"DONUT":"""    WayPoint
        {
            Vertical = true
            lat = -2.0
            lon = -74.8
            alt = 10000
            name = DONUT
        }
        """,
"CAMEL":"""    WayPoint
        {
            Vertical = true
            lat = -2.0
            lon = -70.75
            alt = 5000
            name = CAMEL
        }
        """,
"THRED":"""    WayPoint
        {
            Vertical = true
            lat = -0.2
            lon = -70.75
            alt = 3500
            name = THRED
        }
        """,
"AVA":"""    WayPoint
        {
            Vertical = false
            lat = 8
            lon = -68.5
            name = Avia City VOR
        }
        """,
"HEN":"""    WayPoint
        {
            Vertical = false
            lat = 6.5
            lon = -62
            name = Hennen Island VOR
        }
        """,
"LUS":"""    WayPoint
        {
            Vertical = false
            lat = 2.166
            lon = 26.621
            name = Lushlands VOR
        }
        """,
"GRN":"""    WayPoint
        {
            Vertical = false
            lat = -3.49
            lon = -179.093
            name = Green Coast VOR
        }
        """,
"JJY":"""    WayPoint
        {
            Vertical = false
            lat = 19.652
            lon = -126.479
            name = Jeb's Junkyard VOR
        }
        """,
"STR":"""    WayPoint
        {
            Vertical = false
            lat = -53.82
            lon = -162.1
            name = StrutCo VOR
        }
        """,
"DCE":"""    WayPoint
        {
            Vertical = false
            lat = -17.82
            lon = 166.43
            name = Dinkelstein VOR
        }
        """,
"CAN":"""    WayPoint
        {
            Vertical = false
            lat = 11.32
            lon = -87.69
            name = Sean's Cannery VOR
        }
        """,
"INC":"""    WayPoint
        {
            Vertical = false
            lat = 35.43
            lon = -98.91
            name = Ionic VOR
        }
        """,
"ROK":"""    WayPoint
        {
            Vertical = false
            lat = -50.49
            lon = 170.58
            name = Rokia VOR
        }
        """,
"WOW":"""    WayPoint
        {
            Vertical = false
            lat = 69.93
            lon = -87.69
            name = WinterOwl VOR
        }
        """,
"KBD":"""    WayPoint
        {
            Vertical = false
            lat = 11.32
            lon = -19.04
            name = Kerbodyne VOR
        }
        """,

}
print("""Welcome to Flight Plan Stringer-Together v.1!
This script types out the waypoint definitions for you when you give it a string of comma-separated waypoint names.""")

wpcount = int(input("How many waypoints are in the flight plan? (Approaches are stored as a single waypoint.) >>> "))
counter = 0
# inputter loop
while(counter < wpcount):
    flightplan = flightplan + waypoints[input("name of waypoint to add >>> ")]
    counter += 1

# plan metadata receiver
fpname = input("Flight Plan Name >>> ")
fpdesc = input("Flight Plan Description >>> ")

# final assembly
print("""here is your flight plan!
Just paste it into FlightPlans.cfg under Kerbin{}!""")
print("""
FlightPlan
{
    planet = Kerbin
    name = """ + fpname + """
    description = """ + fpdesc + """
    WayPoints
    {
    """ + flightplan)
print("""    }
}""")
print("I hate Python. Manually remove the empty line and the weird indents. Not gonna fix it. :P")
input("Thanks for using this app! ENTER to exit")
