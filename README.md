# What Hot Corner is?
Hot corner is a functionality that replicates Win+Tab in windows. Some linux distributions it have natively so i tryed to repoduce in windows.

# How it works?
It simply launches the shortcut Win+Tab when the mouse hovers the area choosen in the position-corner.txt.

# Installation
To install the required libraries to run project use the next command

pip install -r example-requirements.txt

You can find a released stable version in compiled-executable folder.

#### Configuration
All you need to know is where your screen corner is located and write it in the `position-corner.txt`  
the file is read as `x , y ; offset_x, offset_y`.

This means if my screen top left corner is on 0, 0 and I want to detect when my mouse is between 10, 10, and 0, 0 I should configure position-corner.txt as `0, 0; 10 , 10`
~~~
0,0---10----------------------------------
| MT  |                                  |
10----10,10                              |
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |
------------------------------------------
*MT = Mouse inside are triggers event.
~~~
Example: 0,0 is top corner, the 10, 10 is the offset.
