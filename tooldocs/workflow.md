# Hiking map workflow

A workflow to generate a GeoPDF (or GeoTIFF) hiking map for your next hike.

TODO: FINISH

## Prerequisites

* *QMapShack* (or other tool to draw map)
* *QLandkarte GT*
* *GIMP* (or other image editor)
* *GDAL*

## Step 1: make map file

Use QMapShack to create a map of your desire.
 
* OSM Topo is a good base map
* Load any GPS traces you want to highlight (or add a manual track)
* Create GPX file to store page area
* Add *Area* rectangle roughly where you want the map page to be
* Edit *Area* rectangle so it is coloured black and remove pattern
* Save/Close GPX (as MAPNAME.gpx)
* Open GPX in text editor and correct area points so they are a rectangle

```xml
   <ql:point lon="145.23923825" lat="-37.36175603"/>
   <ql:point lon="145.23923825" lat="-37.41775931"/>
   <ql:point lon="145.28910051" lat="-37.41775931"/>
   <ql:point lon="145.28910051" lat="-37.36175603"/>
```

* Save/close GPX
* Open GPX in QMapShack again
* Load tiles
  * Zoom to desired level (300m or 500m are good)
  * Pan so all map tiles are loaded
* Save(Print) Map Screenshot
  * Select area roughly near rectangle
  * Zoom to 30m level
  * Correct corners so the handle box just touches map rectangle
  * Zoom back to desired level (300m/500m)
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

TODO: make this into a python tool

* Open MAPNAME.png
* Save as MAPNAME.xcf
* Expand Canvas (40px for 300m, 90px 500m) and expand layers
* Fill white header and footer
* Add title and footer text
* Add elevation plot into a blank area of map
* Export as MAPNAME.png

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


