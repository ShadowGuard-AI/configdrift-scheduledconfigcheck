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

im=Image.new("RGB",(900,700),(246,243,236)); d=ImageDraw.Draw(im)
badge(450,300,190)
t="configdrift-scheduledconfigcheck"; d.text((450,580),t,font=fit(d,t,"BigShouldersInline",820,46),fill=(38,62,110),anchor="mm")
im.save("logo.png"); print("logo drawn: riveted brass badge, winged wheel, no rider")
