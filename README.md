# What Hot Corner is?
Hot corner is a functionality that replicates Win+Tab in windows. Some linux distributions it have natively so I tried to reproduce it in windows.

# How it works?
It simply launches the Win+Tab shortcut when the mouse enters to the area chosen in the position-corner.txt.

# Installation
To install the required libraries to run project use the next command.

~~~
pip install -r requirements.txt`
~~~

You can find a released stable version in compiled-executable folder. or in the [releases page](https://github.com/AlbertMontagutCasero/python-hot-corner-windows/releases/).

#### Configuration
First you need to know the coordinates of your monitor. I recommend my project [mouse position tracker](https://github.com/AlbertMontagutCasero/mouse-position-tracker) so you can see your cursor position and find the right coordinates.
Once you know the coordinates you need to write it in the `position-corner.txt` using the next format. 
~~~
left_x_1 , top_y_1 ; right_x_2 , bottom_y_2
~~~

You can add multiple corners! one for each line, this is really useful if you have multiple screens.


This means if my screen top left corner is on 0, 0 and I want to detect when my mouse is between 0, 0 and 10, 10 I should configure position-corner.txt as `0, 0; 10 , 10`
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
Example: `0 , 0` is top corner coordinate, the `10 , 10` is the offset top corner coordinate.

Example2: 
For a screen with 1920x1080px of resolution.The bottom right corner having a 10 pixels offset in x and y axis
would be `1910 , 1070 ; 1920 , 1080`

Example3:
For a screen with 1920x1080px of resolution.The top right corner having a 20 pixels offset in x and y axis
would be `1900 , 0; 1920 , 20`

