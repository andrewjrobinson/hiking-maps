'''
Created on 16 Oct 2016
@author: Andrew Robinson
'''


from PIL import ImageFont, ImageDraw
from PIL import Image

# TODO: make settings into commandline args
# TODO: generate Elevation graph within
# TODO: justify&wrap INTRO text
# TODO: Add statistics box
# TODO: position elevation graph and stats box
# TODO: gen/add QR code to header (right)

# # Settings
# HEADER="Masons Falls Circuit - Kinglake National Park"
# INTRO=(
#     "15.9km loop track via Masons Falls.",
#     )
# CREDITS=(
#      ('Map data:', 'OSMTopo'),
#      ('Track data:', 'https://www.trailhiking.com.au/masons-falls-circuit/')
#     )
# AUTHOR="by Andrew Robinson"
# HEADER_HEIGHT=0
# FOOTER_HEIGHT=0
# INTRO_LINESPACING=2
# MAP_MARGIN=3
# INFILENAME="MasonFallsCircuit-KinglakeNP.png"
# ELEVFILENAME="MasonsFallsCircuit_elev.png"
# OUTFILENAME="MasonFallsCircuit-KinglakeNP_mu.png"

# Settings
HEADER="Cape Schanck and Bushranger Bay"
INTRO=(
    "12.9km return track via Cape Schanck and Bushranger Bay",
    )
CREDITS=(
     ('Map data:', 'OSMTopo'),
     ('Track data:', 'https://www.trailhiking.com.au/bushranger-bay-cape-schanck/')
    )
AUTHOR="by Andrew Robinson"
HEADER_HEIGHT=0
FOOTER_HEIGHT=0
INTRO_LINESPACING=2
MAP_MARGIN=3
INFILENAME="CapeSchanck.png"
ELEVFILENAME="BushrangerBayandCapeSchanck_elev.png"
OUTFILENAME="CapeSchanckandBushrangerBay_mu.png"

# position of elevation
# TL      TR
# LT      RT
#
# LB      RB
# BL      BR
ELEVPOSITION="BR"


def placeImage(dstimg, srcimg, offset, position, bordercolour, borderwidth):
    '''Places srcimg on destimg at position within offset (rectangle)
    
    @param dstimg: PIL image to receive the srcimg
    @param srcimg: PIL image to place on destimg
    @param offset: (L,T,R,B)
    @param position: TL, TR, BL, or BR
    '''
    
    # calculate position of image and border
    POS=[offset[0],offset[1]]
    BOFF=[0,0,borderwidth-1,borderwidth-1]
    if 'R' in position:
        POS[0]=offset[2]-srcimg.size[0]
        BOFF[0]=-borderwidth
        BOFF[2]=-1
    if 'B' in position:
        POS[1]=offset[3]-srcimg.size[1]
        BOFF[1]=-borderwidth
        BOFF[3]=-1
    POS.append(POS[0]+srcimg.size[0])
    POS.append(POS[1]+srcimg.size[1])
    
    # border rectangle
    rectpos = [x + y for x, y in zip(POS, BOFF)]
    draw.rectangle(rectpos, 
                   fill=(127,127,127,255))
    
    # paste img
    dstimg.paste(srcimg, POS)



fontheading = ImageFont.truetype("Arial_Bold_Italic.ttf", 30)
fontintro = ImageFont.truetype("Arial_Italic.ttf", 14)

fontauthor = ImageFont.truetype("Arial_Bold_Italic.ttf", 20)

# load image
srcimg = Image.open(INFILENAME)

# Auto size
draw = ImageDraw.Draw(srcimg)
if FOOTER_HEIGHT == 0:
    FOOTER_HEIGHT = draw.textsize(AUTHOR, fontauthor)[1] + 10
if HEADER_HEIGHT == 0:
    HEADER_HEIGHT = draw.textsize(HEADER, fontheading)[1]+20
    HEADER_HEIGHT += (draw.textsize(INTRO[0], fontintro)[1])*len(INTRO)+len(INTRO)*INTRO_LINESPACING
    

# expand canvas
oldw,oldh = srcimg.size
neww = oldw+MAP_MARGIN+MAP_MARGIN
newh = oldh+HEADER_HEIGHT+FOOTER_HEIGHT+MAP_MARGIN+MAP_MARGIN
dstimg = Image.new('RGBA', (neww,newh), color=(0,0,0,255))
MAP_POS=(MAP_MARGIN,
         HEADER_HEIGHT+MAP_MARGIN,
         MAP_MARGIN+oldw,
         HEADER_HEIGHT+MAP_MARGIN+oldh)
dstimg.paste(srcimg, MAP_POS)

draw = ImageDraw.Draw(dstimg)

# header/footer white
draw.rectangle([0,0,neww-1, HEADER_HEIGHT-1], fill=(255,255,255,255))
draw.rectangle([0,newh-FOOTER_HEIGHT,neww-1, newh-1], fill=(255,255,255,255))

## header text ##
yoff = 7
draw.text((10, yoff), HEADER, font=fontheading, fill=(0,0,0,255))
yoff += draw.textsize(HEADER, fontheading)[1] + 10
for txt in INTRO:
    draw.text((10, yoff), txt, font=fontintro, fill=(48,48,48,255))
    yoff += draw.textsize(INTRO[0], fontintro)[1] + INTRO_LINESPACING
    

## footer text ##
fontbold = ImageFont.truetype("Arial_Bold_Italic.ttf", 16)
fontitalic = ImageFont.truetype("Arial_Italic.ttf", 16)

# credits
xoff = 10
th=draw.textsize(CREDITS[0][0], fontbold)[1]
yoff = newh-(th+(FOOTER_HEIGHT-th)/2)
for btext, ntext in CREDITS:
    draw.text((xoff, yoff), btext, font=fontbold, fill=(48,48,48,255))
    xoff += draw.textsize(btext, fontbold)[0] + 5
    draw.text((xoff, yoff), ntext, font=fontitalic, fill=(48,48,48,255))
    xoff += draw.textsize(ntext, fontitalic)[0] + 15

# author
fontbold = ImageFont.truetype("Arial_Bold_Italic.ttf", 20)
tw, th = draw.textsize(AUTHOR, fontbold)
draw.text((neww-tw-10, 
           newh-(th+(FOOTER_HEIGHT-th)/2)), 
          AUTHOR, 
          font=fontbold, 
          fill=(48,48,48,255))

## Elevation ##
# resize
elevimg = Image.open(ELEVFILENAME)
sz = oldw/2, oldw/5
elevimg.thumbnail(sz)
ew, eh=elevimg.size

# # black rectangle
# draw.rectangle([MAP_MARGIN,
#                 HEADER_HEIGHT+MAP_MARGIN,
#                 ew+MAP_MARGIN+MAP_MARGIN-1, 
#                 HEADER_HEIGHT+eh+MAP_MARGIN+MAP_MARGIN-1], 
#                fill=(127,127,127,255))
# 
# # place
# dstimg.paste(elevimg, (MAP_MARGIN,
#                       HEADER_HEIGHT+MAP_MARGIN,
#                       MAP_MARGIN+ew,
#                       HEADER_HEIGHT+MAP_MARGIN+eh))
placeImage(dstimg, elevimg, MAP_POS, ELEVPOSITION, (127,127,127,255), MAP_MARGIN)

# Output file
dstimg.save(OUTFILENAME, "PNG")
dstimg.show()

