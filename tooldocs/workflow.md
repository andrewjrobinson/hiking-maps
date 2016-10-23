# Hiking map workflow

A workflow to generate a GeoPDF (or GeoTIFF) hiking map for your next hike.

TODO: FINISH

## Prerequisites

* *QMapShack* (or other tool to draw map)
* *QLandkarte GT*
* *GDAL*

## Step 1: make map file

Use QMapShack to create a map of your desire.
 
* OSM Topo is a good base map
* Load any GPS traces you want to highlight (or add a manual track)
  * For manual tracks add elevation information (DEM) and it will add them to your points
  * Save track in GPX file
* Add top-left and bottom-right corners of map area as waypoints (name the 
  bottom-right ' ', i.e. a space character)
* Load tiles
  * Zoom to desired level (300m or 500m are good)
  * Pan so all map tiles are loaded
* Save(Print) Map Screenshot
  * Select area roughly near top-right to bottom-left
  * Zoom to desired level (again if you changed it for above)
  * Correct corners so the handle box aligns with waypoint centre
  * Click save icon (top right of screenshot rectangle
  * Write to MAPNAME_raw.png
  
## Step 2: Generate Elevation plot

Optional:

* Make GPX file
  * Add GPS trace (or manual track) to Area GPX file
  * Save
* Run *gen-elevation-plot MAPNAME.gpx*

## Step 3: Combine map pieces

Using GIMP add elevation and map name / other details

TODO: make options as cmdline args

* Edit *addheaderfooter.py* file (settings at top)
* Run *addheaderfooter.py*

## Step 4: Geo-reference image

Use QLandkarte GT to georef image file

* [Map > Edit/Create Map]
* Convert a Tiff into GeoTiff ...
* Input file: MAPNAME.png
* Output file: MAPNAME.tif
* Add 3 Refs 
  * at 3 corners of Area rectangle
  * Copy Coord from MAPNAME.gpx file
* Start process

## Step 5: Convert to GeoPDF

Use GDAL tool to convert to PDF format

* Run *gdal_translate -of PDF MAPNAME.tif MAPNAME.pdf*

## Step 6: Test Georef

You can test it if you are at location (not likely) by loading it into *PDF maps* app on you smartphone.

Otherwise:

* Run *gdalbuildvrt MAPNAME.vrt MAPNAME.pdf* (or MAPNAME.tif)
* Copy MAPNAME.vrt and MAPNAME.pdf to QMapShack's map directory
* Reload Maps
* Activate MAPNAME
* Check it lines up where it should be


