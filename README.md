# lego-nxt-cube-solver

<img src="Readme%20imgs/final_solve.gif" alt="Final Solve" width="600"/>


### Design 

I designed the machine in Bricklink Studio and built/programmed it over the course of three months in Summer 2022. I wanted to make a 6-axis robot but did not have time to add Lego colour sensors, so I used the webcam to take photos of the sides and a logistic regression model to analyze the cube state. 

<img src="Readme%20imgs/bricklink_animation.gif" alt="Design in Studio" width="400"/>

<br />

### Features
- Webcam scanner to automatically detect the colours of cube given pictures of the sides, regardless of lighting conditions. After experimenting with neural networks and colour ranges, I trained a robust logistic regression on cubes in varying environments to identify the cube state (96% accuracy). 

    <img src="Readme%20imgs/take_pics_example.png" alt="Scanning green side" width="300"/>

- Kociemba algorithm to find the quickest solution, given a cube state. Average of 19 moves per solution. 

- Accurate-ish turning of the sides to excecute the solution. This was a challenge because turning over bluetooth instead of usb is way less accurate. There is also no official framework to control Mindstorms NXT from Python. I hot-glued a round brick to the center piece of the cube to enable turning. 

    <img src="Readme%20imgs/gluing_centers.gif" alt="Gluing the center to lego piece" width="200"/>
    <img src="Readme%20imgs/all_centers.gif" alt="All glued centers" width="200"/>

<br />

### Notes

My main inspiration was [SquidCuber](https://github.com/efrantar/squidcuber). I got help from: 
- [schodet](https://github.com/schodet/nxt-python)'s nxt python controller
- [Wiston999](https://github.com/Wiston999/python-rubik)'s implementation of the Kociemba algorithm
- [kkoomen](https://github.com/kkoomen/qbr)'s helper functions
- [rutujapadgilwar06](https://github.com/rutujapadgilwar06/rubik-s-cube-solver)'s webcam scanning grid

### Files/Video
The Studio 2.0 model file is listed above as `rubiks cube solver.io`. 

I made a [YouTube video](https://youtu.be/l03atw1TRHM). 
