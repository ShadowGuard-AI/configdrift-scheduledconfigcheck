"""Individually coded drawing program for this repository and this piece only."""
import math, random
from PIL import Image, ImageDraw, ImageFont
FD="/tmp/fonts17"
def F(n,s): return ImageFont.truetype(f"{FD}/{n}.ttf", s)
def fit(d,t,n,mw,st=60):
    s=st
    while s>10:
        f=F(n,s)
        if d.textlength(t,font=f)<=mw: return f
        s-=2
    return F(n,s)

def badge(cx,cy,r):
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=(176,140,62),outline=(110,84,30),width=4)
    d.ellipse([cx-r+10,cy-r+10,cx+r-10,cy+r-10],fill=(38,62,110))
    d.ellipse([cx-26,cy-26,cx+26,cy+26],outline=(240,240,240),width=5); d.ellipse([cx-5,cy-5,cx+5,cy+5],fill=(240,240,240))
    for sgn in (-1,1): d.polygon([(cx+sgn*20,cy-8),(cx+sgn*58,cy-24),(cx+sgn*54,cy+2),(cx+sgn*20,cy+6)],fill=(240,240,240))

im=Image.new("RGB",(1600,520),(240,234,218)); d=ImageDraw.Draw(im)
d.rectangle([0,330,1600,520],fill=(52,96,74))
for i in range(9):
    x=90+i*110; d.line([(x,70),(x,120)],fill=(60,58,54),width=5); d.ellipse([x-8,120,x+8,142],outline=(176,140,62),width=4)
d.rectangle([180,180,760,320],fill=(248,246,238),outline=(38,62,110),width=3); d.line([(470,180),(470,320)],fill=(128,132,138),width=2)
for yy in range(205,310,24): d.line([(200,yy),(450,yy)],fill=(170,180,200),width=2)
d.ellipse([1180,180,1310,310],outline=(178,44,44),width=8)
badge(920,130,62)
d.rectangle([800,205,1045,262],fill=(250,248,240),outline=(38,62,110),width=3)
t="configdrift-scheduledconfigcheck"; d.text((922,233),t,font=fit(d,t,"BigShouldersInline",235,20),fill=(38,62,110),anchor="mm")
im.save("banner.png"); print("banner drawn: morning office, badge card pinned above counter")
