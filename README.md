# OctaCon
The Octal Music Convertor - turning text and pictures into music 🎵

## Table of Contents
- [Installation](#installation)
- [Python Dependancies](#python-dependancies)
- [Basic Usage](#basic-usage)
- [Theory](#theory)

## Installation
1. Clone the repository:
```bash
 gh repo clone sachindias/OctaCon
```

## Python Dependancies
| Package |
|----------|
| numpy |
| pillow |
| mido |

## Basic Usage

### TextaCon



### PictaCon

## Theory
The basic concept behind OctaCon is to convert text and pictures to music using octal (see https://en.wikipedia.org/wiki/Octal). 
This is particularly beneficial for music as octal is a base-8 numerical system and many scales have 8 notes (from root note to octave). 

As the exact implementation is different for converting text to music (TextaCon) and converting pictures to music (PictaCon) we will run through these separately below. 
The main difference concerns how we get from text or pictures to octal in the first place.

### TextaCon
The process follows the flowchart and is described below:

<img src="OctaCon/SUPPORTING_FILES/TextaCon_flowchart.png" alt="TextaCon Flowchart" style="width:50%;" />

1. We need to start with some text, the word MUSIC in this case.
2. Next, we decompose this into the individual letters.
3. Each symbol, number or letter has a unique Unicode (https://home.unicode.org) number associated with it. 
This is written as "U+" followed by the number in hexadecimal (https://en.wikipedia.org/wiki/Hexadecimal). 
For example the letter M is U+004D. 
4. Ignoring the "U+" part, we can convert the hexadecimal (base-16 numerical system) number for each letter into octal (base-8 numerical system).
For M this gives 115 in octal.
5. Now we need an 8 note scale, for simplicity we will use C Major (C, D, E, F, G, A, B, C)
6. Numbering each note in the scale from 0 to 7, we can turn out octal numbers into notes. 
Taking the example of M again, D = 1 and A = 5, meaning our notes are DDA. 
7. Once this has been done for each character, we have our final list of notes. Here we have:

    DDA DEA DEF DDD DCF

8. This can now be played on an instrument or using MIDI.



### PictaCon
The process follows the flowchart and is described below:

<img src="OctaCon/SUPPORTING_FILES/PictaCon_flowchart.png" alt="PictaCon Flowchart" style="width:50%;" />

1. We need to start with a picture, 4 coloured pixel in this case.
2. Next, we decompose this into the individual pixels, going left → right and top → bottom.
3. Colours can be described with RGB values, with red, green and blue on 3 separate 0 - 255 scales. 
For example, the colour white has values of 255 on each of these 3 scales. 
We can write the values of these scales in hexadecimal, which gives us FF for white.
Stringing these together and adding a "#" we can create a unique code for each colour. 
As white is FF for each scale, we get #<span style="color: red;">FF</span><span style="color: green;">FF</span><span style="color: blue;">FF</span>.
4. Ignoring the "#", we can convert the hexadecimal number into octal.
5. Follow steps 5 - 8 for TextaCon. 


