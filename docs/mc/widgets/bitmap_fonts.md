---
title: Bitmap Fonts
---

# Bitmap Fonts


You can create your own fonts for your machine using bitmap fonts. There
are several programs or online tools to create bitmap font descriptors.

## 1. Create an Image For Your Font

An example might look like this:

![image](/docs/mc/images/bitmap_font_example.png)

## 2. Map Your Characters in a Descriptor File

This file might look like this:

``` text
info face=font size= bold= italic= charset= unicode= stretchH= smooth= aa= padding=0,0,0,0 spacing=0,0 outline=0
common lineHeight=55 base=55 scaleW=40 scaleH=55 pages=1 packed=0
page id=0 file="bitmapFontBallySevenSegment4.png"
chars count=11
char id=48 x=0 y=0 width=40 height=55 xoffset=0 yoffset=0 xadvance=40 page=0 chnl=15
char id=49 x=0 y=55 width=40 height=55 xoffset=0 yoffset=0 xadvance=40 page=0 chnl=15
char id=50 x=0 y=110 width=40 height=55 xoffset=0 yoffset=0 xadvance=40 page=0 chnl=15
char id=51 x=0 y=165 width=40 height=55 xoffset=0 yoffset=0 xadvance=40 page=0 chnl=15
char id=52 x=0 y=220 width=40 height=55 xoffset=0 yoffset=0 xadvance=40 page=0 chnl=15
char id=53 x=0 y=275 width=40 height=55 xoffset=0 yoffset=0 xadvance=40 page=0 chnl=15
char id=54 x=0 y=330 width=40 height=55 xoffset=0 yoffset=0 xadvance=40 page=0 chnl=15
char id=55 x=0 y=385 width=40 height=55 xoffset=0 yoffset=0 xadvance=40 page=0 chnl=15
char id=56 x=0 y=440 width=40 height=55 xoffset=0 yoffset=0 xadvance=40 page=0 chnl=15
char id=57 x=0 y=495 width=40 height=55 xoffset=0 yoffset=0 xadvance=40 page=0 chnl=15
char id=32 x=0 y=550 width=40 height=55 xoffset=0 yoffset=0 xadvance=40 page=0 chnl=15
```

## 3. Put PNG File and Descriptor Into the bitmap_fonts Folder

![image](/docs/mc/images/bitmap_font_file_structure.png)

Some things to note:

* The file name of the image is defined in the .FNT file
* The ASCII code for each character is defined by a starting position
    (x, y for the upper left corner) and a width and height value.

## 4. Use the Font in Your Slide

You can use the font in your config:

``` mpf-mc-config
slides:
  slideBaseBackglass:
    widgets:
      - type: text
        text: (player1|score)
        font_name: bitmapFontBallySevenSegment4
        bitmap_font: true
```

Alternatively, you can also use bitmap fonts in
[widget styles](styles.md).
