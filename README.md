# lego-nxt-cube-solver


https://user-images.githubusercontent.com/45503370/184534183-e9cf61b4-5684-4821-80d5-0fa76c5122c4.mp4


### Design 

I designed the machine in Bricklink Studio and built it over the course of three months in Summer 2022. I wanted to make a 6-axis robot but did not have time to add Lego colour sensors, so I used a logistic regression model to analyze the cube state. 

<img src="Readme%20imgs/rubiks_cube_animation.gif" alt="Design in Studio" width="300"/>

<br />

### Features
- Webcam scanner to automatically detect the colours of cube given pictures of the sides, regardless of lighting conditions. After experimenting with neural networks and colour ranges, I trained a robust logistic regression on cubes in varying environments to identify the cube state (96% accuracy). 

    <img src="Readme%20imgs/take_pics_example.png" alt="Design in Studio" width="300"/>

- Kociemba algorithm to find the quickest solution, given a cube state. Average of 19 moves per solution. 

- Accurate-ish turning of the sides to excecute the solution. This was a challenge because bluetooth connections are less accurate than usb and Mindstorms NXT was released in 2006. 

<br />

### Notes

My main inspiration was [SquidCuber](https://github.com/efrantar/squidcuber). I got help from: 
- [schodet](https://github.com/schodet/nxt-python)'s nxt python controller
- [Wiston999](https://github.com/Wiston999/python-rubik)'s implementation of the Kociemba algorithm
- [kkoomen](https://github.com/kkoomen/qbr)'s helper functions
- [rutujapadgilwar06](https://github.com/rutujapadgilwar06/rubik-s-cube-solver)'s webcam scanning grid

The Studio model can be found on Bricklink [here](https://www.bricklink.com/v3/studio/design.page?idModel=352079). 