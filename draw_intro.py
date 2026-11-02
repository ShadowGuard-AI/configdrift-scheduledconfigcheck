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

im=Image.new("RGB",(1600,900),(214,196,160)); d=ImageDraw.Draw(im)
d.rectangle([0,520,1600,900],fill=(52,96,74)); d.rectangle([0,520,1600,545],fill=(226,214,180))
d.rectangle([1120,90,1420,470],outline=(128,132,138),width=8); d.rectangle([1130,100,1410,460],fill=(226,230,228))
for i in range(7):
    x=120+i*130; d.line([(x+17,190),(x+17,238)],fill=(176,140,62),width=6); d.ellipse([x+8,238,x+26,258],outline=(176,140,62),width=4)
d.rectangle([420,330,900,500],fill=(200,60,50),outline=(120,90,60),width=4); d.ellipse([650,318,674,342],fill=(176,140,62))
d.rectangle([150,580,700,760],fill=(232,226,208),outline=(38,62,110),width=4); d.line([(150,668),(700,668)],fill=(178,44,44),width=3)
d.ellipse([1080,600,1260,700],outline=(128,132,138),width=10)
im.save("intro-banner.png"); print("intro drawn: office before opening, card back only, no lettering")
