#!/usr/bin/env python

from geopy.distance import vincenty
import matplotlib.pyplot as plt
import gpxpy.parser as parser

import sys, os

if len(sys.argv) != 2:
	print "Usage: gen-elevation-plot GPXFILE"
	sys.exit(1)

infile=sys.argv[1]
outfile=os.path.basename(os.path.splitext(infile)[0]) + "_elev.png"

gpx_file = open(infile, 'r' )

gpx_parser = parser.GPXParser( gpx_file )
gpx_parser.parse()
gpx_file.close()

gpx = gpx_parser.gpx


x=[]
y=[]
for track in gpx.tracks:
	lastpoint = None
	dist = 0.0
	for segment in track.segments:
		for point in segment.points:
			p = (point.latitude, point.longitude)
			if lastpoint is not None:
				dist += vincenty(lastpoint, p).meters
			lastpoint = p
			x.append(dist/1000)
			y.append(point.elevation)

plt.figure(figsize=(18,4.8), dpi=100)
plt.plot(x,y)
plt.ylabel('elevation (m)')
plt.xlabel('distance (km)')
#plt.show()
plt.savefig(outfile, bbox_inches='tight')

				

