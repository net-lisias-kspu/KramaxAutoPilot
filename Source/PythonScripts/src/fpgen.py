#!/usr/bin/python
#
﻿# fpgen.py
# KSP/Kramax Autopilot flightplan generator
# (C) 2018 Scott Stone <ss8913@gmail.com>
#
# https://forum.kerbalspaceprogram.com/index.php?/topic/150846-141-kramax-autopilot-continued-course-guidance-and-auto-land-for-spaceplanes/&do=findComment&comment=3461311
#
# give this a runway threshhold lat/lon in decimal, plus a runway heading
# it will make an approach flightplan.  Defaults can be overridden on the
# commandline.
#
# haversine formulas courtesy of: https://www.movable-type.co.uk/scripts/latlong.html
# other trig formula courtesy of 11th grade math
#
# THIS VERSION IS FOR PYTHON 2.x
# IT WILL NOT WORK AS-IS IN PYTHON 3.x
# I hear if you put parens around all the print functions, it will.
#

import sys
import math
import argparse
import re

### DEFAULTS

# kerbals use metric, distances are in km
# distances are from the runway threshhold, total not incremental
_FAF_DISTANCE = 13
_IAF_DISTANCE = 23
_APP1_DISTANCE = 50
_APP2_DISTANCE = 100
_APP3_DISTANCE = 200
_FAF_ALTITUDE = -1
_IAF_ALTITUDE = -1
_APP1_ALTITUDE = 6500
_APP2_ALTITUDE = 10000
_APP3_ALTITUDE = 12000
# flare height in meters
_FLARE = 25
# glideslope in degrees
_GS = 4
# planetary radius in km, default is 600 for Kerbin
_PLANET = "Kerbin"
_RADIUS = 600.000
# fix names
fix_names = {
    'stop': 'STOP',
    'rwy': 'FLARE',
    'faf': 'FAF',
    'iaf': 'IAF',
    'app1': 'LOKEY',
    'app2': 'HIKEY',
    'app3': 'MAXKY'
}

# general options
SCRIPT_NAME = "fpgen"
SCRIPT_VERSION = "1.1.0"
SCRIPT_AUTHOR = "Scott Stone <ss8913@gmail.com>"
SCRIPT_COPYRIGHT = "(C) 2018 Scott Stone - distributed under BSD License"
DEBUG = 0
NEWLINEFORMAT = "unix"


### SUBROUTINES

def dbg(msg):
    if (DEBUG > 0):
        sys.stderr.write("DEBUG: %s\n" % (msg))


def log(msg):
    newline = "\n"
    if (NEWLINEFORMAT != "unix"):
        newline = "\r\n"
    sys.stdout.write("%s%s" % (msg, newline))


# this function does some of the work
# uses the law of sines to find the altitude based on the glideslope angle
# ( sin alpha / a ) == ( sin beta / b )
# or in practical terms:
# ( sin glideslope / altitude) == ( sin topangle / distance )
# sin glideslope == ( altitude * sin topangle ) / distance
# distance * sin glideslope == altitude * sin topangle
# (distance * sin glideslope) / sin topangle == altitude
def calculateAltitude(_dist, slopeAngle):
    # _dist is in km, we need m
    dist = (_dist * 1000)
    topAngle = float(180 - (90 + slopeAngle))
    altitude = ((float(dist) * math.sin(math.radians(slopeAngle))) / (math.sin(math.radians(topAngle))))
    return altitude


# radius given in km here
# lat/lon in signed decimal degrees
# returns a value in km
# TESTED: this function works properly
def haversineDistance(lat1, lon1, lat2, lon2, radius):
    dbg("haversineDistance received [%.4f / %.4f], [%.4f / %.4f], %.4f km radius" % (lat1, lon1, lat2, lon2, radius))
    R = (radius * 1000)
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    # get kilometers
    dkm = d / 1000.0
    return dkm


# this function does most of the work
def haversine(key, lat, lon, hdg, dist, appdata):
    # ad = float(float(dist) / float(appdata['radius']))
    radius1 = (float(appdata['radius']) * 1000)
    dist1 = (dist * 1000)
    # ad = math.radians(float(float(dist1) / float ( radius1 ) ) )
    ad = float(float(dist1) / float(radius1))
    lat1 = math.radians(float(lat))
    lon1 = math.radians(float(lon))
    hdg1 = math.radians(float(hdg))
    dbg("haversine function has %.4f/%.4f heading %.4f distance %.4f km" % (
        float(lat), float(lon), float(hdg), float(dist)))
    dbg("converted values %.8f/%.8f heading %.4f radians distance %.4f m, planetary radius %.4fm" % (
        lat1, lon1, hdg1, dist1, radius1))
    lat2 = math.asin((math.sin(lat1) * math.cos(ad)) + math.cos(lat1) * math.sin(ad) * math.cos(hdg1))
    lon2 = lon1 + math.atan2(math.sin(hdg1) * math.sin(ad) * math.cos(lat1),
                             math.cos(ad) - math.sin(lat1) * math.sin(lat2))
    rd = dict()
    rd['lat'] = math.degrees(lat2)
    rd['lon'] = math.degrees(lon2)
    rd['dist'] = dist
    rd['name'] = fix_names[key]
    # get altitudes from law of sines using glideslope for iaf to faf to runway else static
    altKey = "%s_altitude" % (key)
    if (int(appdata[altKey]) != -1):
        rd['alt'] = int(appdata[altKey])
    else:
        rd['alt'] = (calculateAltitude(dist, float(appdata['glideslope'])) +
                     int(appdata['rwy_altitude']))
    return rd


def logFlightPlan(appdata):
    log("KramaxAutoPilotPlans")
    log("{")
    log("    %s" % (appdata['planet']))
    log("    {")
    log("        FlightPlan")
    log("        {")
    log("            planet = %s" % (appdata['planet']))
    log("            name = %s" % (appdata['fpname']))
    log("            description = %s" % (appdata['fpdesc']))
    log("            WayPoints")
    log("            {")
    for k in ['app3', 'app2', 'app1', 'iaf', 'faf', 'rwy', 'stop']:
        log("                WayPoint")
        log("                {")
        log("                    Vertical = true")
        if (k == "iaf"):
            log("                    IAF = true")
        if (k == "faf"):
            log("                    FAF = true")
        if (k == "rwy"):
            log("                    RW = true")
        if (k == "stop"):
            log("                    Stop = true")
        log("                    lat = %.8f" % (appdata[k]['lat']))
        log("                    lon = %.8f" % (appdata[k]['lon']))
        log("                    alt = %d" % (appdata[k]['alt']))
        log("                    name = %s" % (fix_names[k]))
        log("                }")
    log("            }")
    log("        }")
    log("    }")
    log("}")


### MAIN EXECUTION

# dict to store our configuration values
approachData = dict()

# commandline args
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", help="Enable debugging", action="store_true")
parser.add_argument("-p", "--planet", help="Planet Name (dfl: %s)" % (_PLANET), default=_PLANET)
parser.add_argument("-g", "--glideslope", default=_GS, help="Specify glideslope in degrees, dfl %.2f" % (_GS))
parser.add_argument("-n", "--newlineformat", help="dos or unix newlines.  dfl: unix", default="unix")
parser.add_argument("--name", help="Flight Plan Name (required)")
parser.add_argument("--description", help="Flight Plan Description (required)")
parser.add_argument("--latitude", type=float, help="Specify rwy latitude (required)")
parser.add_argument("--longitude", type=float, help="Specify rwy longitude (required)")
parser.add_argument("--heading", type=float, help="Runway heading in degrees (required)")
parser.add_argument("-f", "--flare", type=int, default=_FLARE, help="Flare height in meters (dfl: %d)" % (_FLARE))
parser.add_argument("-r", "--radius", type=float, default=_RADIUS,
                    help="Planetary radius in km (dfl: %.2f)" % (_RADIUS))
parser.add_argument("--faf", default=_FAF_DISTANCE, help="FAF distance in km (dfl: %.2f)" % (_FAF_DISTANCE))
parser.add_argument("--iaf", default=_IAF_DISTANCE, help="IAF distance in km (dfl: %.2f)" % (_IAF_DISTANCE))
parser.add_argument("--app1", default=_APP1_DISTANCE, help="APP1 distance in km (dfl: %.2f)" % (_APP1_DISTANCE))
parser.add_argument("--app2", default=_APP2_DISTANCE, help="APP2 distance in km (dfl: %.2f)" % (_APP2_DISTANCE))
parser.add_argument("--app3", default=_APP3_DISTANCE, help="APP3 distance in km (dfl: %.2f)" % (_APP3_DISTANCE))
parser.add_argument("-a", "--altitude", type=int, help="Runway altitude in meters MSL (required)")
parser.add_argument("--fafalt", default=_FAF_ALTITUDE, help="FAF Altitude in m (dfl: %.2f)" % (_FAF_ALTITUDE))
parser.add_argument("--iafalt", default=_IAF_ALTITUDE, help="IAF Altitude in m (dfl: %.2f)" % (_IAF_ALTITUDE))
parser.add_argument("--app1alt", default=_APP1_ALTITUDE, help="APP1 Altitude in m (dfl: %.2f)" % (_APP1_ALTITUDE))
parser.add_argument("--app2alt", default=_APP2_ALTITUDE, help="APP2 Altitude in m (dfl: %.2f)" % (_APP2_ALTITUDE))
parser.add_argument("--app3alt", default=_APP3_ALTITUDE, help="APP3 Altitude in m (dfl: %.2f)" % (_APP3_ALTITUDE))
parser.add_argument("-D", "--distanceonly", help="Just calculate distance, X/Y,X/Y", action="store_true")
parser.add_argument("--dlat1", type=float, help="Distance calc latitude 1")
parser.add_argument("--dlon1", type=float, help="Distance calc longitude 1")
parser.add_argument("--dlat2", type=float, help="Distance calc latitude 2")
parser.add_argument("--dlon2", type=float, help="Distance calc longitude 2")

args = parser.parse_args()

if (args.debug):
    DEBUG = 1

if (args.distanceonly):
    dbg("distanceonly coords: [%.4f/%.4f %.4f/%.4f]" % (args.dlat1, args.dlon1, args.dlat2, args.dlon2))
    try:
        d = haversineDistance(args.dlat1, args.dlon1, args.dlat2, args.dlon2, float(args.radius))
        print "Distance is %.4f km" % (float(d))
    except:
        ea = sys.exc_info()
        log("ERROR: %s %s" % (ea[0], ea[1]))
        sys.exit(1)
    sys.exit(0)

if (
        (not args.latitude) or
        (not args.name) or
        (not args.description) or
        (not args.longitude) or
        (not args.heading) or
        (not args.altitude)):
    print "Name/Description/Lat/Lon/Heading/Altitude are required arguments.  Run with -h for help."
    sys.exit(1)

NEWLINEFORMAT = args.newlineformat
approachData['planet'] = args.planet
approachData['fpname'] = args.name
approachData['fpdesc'] = args.description
approachData['glideslope'] = args.glideslope or _GS
approachData['latitude'] = args.latitude
approachData['longitude'] = args.longitude
approachData['rwy_heading'] = args.heading
approachData['rwy_altitude'] = args.altitude + args.flare
approachData['stop_altitude'] = args.altitude
approachData['radius'] = args.radius
approachData['faf_distance'] = args.faf
approachData['iaf_distance'] = args.iaf
approachData['app1_distance'] = args.app1
approachData['app2_distance'] = args.app2
approachData['app3_distance'] = args.app3
approachData['faf_altitude'] = args.fafalt
approachData['iaf_altitude'] = args.iafalt
approachData['app1_altitude'] = args.app1alt
approachData['app2_altitude'] = args.app2alt
approachData['app3_altitude'] = args.app3alt

if (DEBUG > 0):
    print approachData

reverse_heading = (float(approachData['rwy_heading']) + 180) % 360
approachData['stop'] = haversine('stop',
                                 float(approachData['latitude']),
                                 float(approachData['longitude']),
                                 float(approachData['rwy_heading']),
                                 1.0,
                                 approachData)
approachData['rwy'] = haversine('rwy',
                                float(approachData['latitude']),
                                float(approachData['longitude']),
                                float(approachData['rwy_heading']),
                                0.0,
                                approachData)
approachData['faf'] = haversine('faf',
                                float(approachData['latitude']),
                                float(approachData['longitude']),
                                reverse_heading,
                                float(approachData['faf_distance']),
                                approachData)
approachData['iaf'] = haversine('iaf',
                                float(approachData['latitude']),
                                float(approachData['longitude']),
                                reverse_heading,
                                float(approachData['iaf_distance']),
                                approachData)
approachData['app1'] = haversine('app1',
                                 float(approachData['latitude']),
                                 float(approachData['longitude']),
                                 reverse_heading,
                                 float(approachData['app1_distance']),
                                 approachData)
approachData['app2'] = haversine('app2',
                                 float(approachData['latitude']),
                                 float(approachData['longitude']),
                                 reverse_heading,
                                 float(approachData['app2_distance']),
                                 approachData)
approachData['app3'] = haversine('app3',
                                 float(approachData['latitude']),
                                 float(approachData['longitude']),
                                 reverse_heading,
                                 float(approachData['app3_distance']),
                                 approachData)

if (DEBUG > 0):
    print approachData

    for k in ['app3', 'app2', 'app1', 'iaf', 'faf', 'rwy', 'stop']:
        print "%s ::" % (k)
        print "    Name :: %s" % (approachData[k]['name'])
        print "     Lat :: %.4f" % (float(approachData[k]['lat']))
        print "     Lon :: %.4f" % (float(approachData[k]['lon']))
        print "    Dist :: %.4f km" % (float(approachData[k]['dist']))
        print "     Alt :: %.4f m" % (float(approachData[k]['alt']))
        print ""

    hd = haversineDistance(float(approachData['app3']['lat']),
                           float(approachData['app3']['lon']),
                           float(approachData['stop']['lat']),
                           float(approachData['stop']['lon']),
                           float(approachData['radius']))
    print "Total flight plan length: %.4f km" % (hd / 1000.00)

    logFlightPlan(approachData)
    
