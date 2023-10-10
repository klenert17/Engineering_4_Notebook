# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Crash Avoidence Assignment](#crash_avoidence_assignment)
* [Launch Pad Assignment](#launch_pad_assignment)
* [Raspberry Pi LED Blink](#Raspberry_Pi_LED_Blink)
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Onshape_Assignment_Template](#onshape_assignment_template)
* [FEA_Assignment](#FEA_Part_1)
&nbsp;


## FEA_Part_1 

### Assignment Description
For this assignement we were partnered up and required to make the strongest beam we could with any prior knowledge. They would then be tested as we add weight to a bucket. The bucket had to hang 180mm away from the base and it had to weight a maximum of 13 grams.  

### Part Link 

[Link to OnShape Document](https://cvilleschools.onshape.com/documents/8b325fcbf1fc9ced667a46ad/w/244fda1d4dd423e6920295c5/e/da5820986e36d6e64f72469d?renderMode=0&uiState=651c4898682dbd1154ff7054)

### Part Image

![Beam Starter + Holder (1)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/e544fb58-9bc6-48a1-bf78-4421a7003cab)
![Beam Starter + Holder](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/6d120254-8b42-4404-98a4-d1a67529a0ab)


### Reflection

When starting this assignment we had the idea to make a I beam because it seemed to be the strongest, however we realized that there would be a lot of overhang and the beam would not be able to print. So we pivoted our idea and realized that triangles are the strongest shape. We made a long triangular prism with supporting beams inside. It matched the requirement for 180mm but it was too heavy. WE had to make the walls a lot thinner and cut out a lot of holes so it would be 13 grams. Overall this assignment was fun and a good way to get back into CAD and we can't wait to see how well it works.

## FEA_Part_2/3

### Assignment Description
We learned how to do a simulation on Onshape called FEA which shows the weakest and strongest parts of a desgin when force is applied. 

### Part Link 

[Link to OnShape Document](https://cvilleschools.onshape.com/documents/8b325fcbf1fc9ced667a46ad/w/244fda1d4dd423e6920295c5/e/da5820986e36d6e64f72469d?renderMode=0&uiState=651c4898682dbd1154ff7054)

### Part Image
![Assembly 1 (1)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/39202830-fd05-4bbc-83b5-1d62d99b433c)
![Assembly 1 (2)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/4f51f6cd-e556-4d24-a891-ead528de8e5b)
![Assembly 1](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/25e762aa-cc76-4c3b-a7d2-02801b0c0838)
![Assembly 1 (3)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/f193720c-f05c-4be0-8003-15ed7fc8370f)


### Reflection

Our design is very good with most of the stress being at the point that connects to the base. The structural beams inside where very helpful to support the fore. We just need to reinforce the points of the triangle that are close to the base so it doesn't snap. 

## FEA_Part_4

### Part Link 

[Link to OnShape Document](https://cvilleschools.onshape.com/documents/8b325fcbf1fc9ced667a46ad/w/244fda1d4dd423e6920295c5/e/da5820986e36d6e64f72469d?renderMode=0&uiState=651c4898682dbd1154ff7054)

### Part Image

![Assembly 1 (5)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/6edb8424-2db6-4bd4-a8f1-5fa8272c07fb)
![Assembly 1 (9)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/d17533c0-c10e-4da3-bf17-ea3c5950bb66)
![Assembly 1 (10)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/3d8094fd-4755-4261-8f7d-98da82d39743)
![Assembly 1 (8)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/8eacc8b7-5bf5-438b-a693-ea49dab8aee9)

### Reflection

To improve our beam we added more support to the walls closest the the holder, so it wouldn't break as easily. We also thickend some of the walls were there was the most yellow. But to take away the added weight we cut out more holes. 

## Crash Avoidence Assignment

### Part 1

#### Assignment description

For this assignment we had to wire up an accelerometer that returns acceleration values for the x, y, and z axes to the serial monito.r

#### Evidence

![ezgif com-optimize (3)](https://github.com/klenert17/Engineering_4_Notebook/assets/71406905/f4ae19f4-74f9-424e-a258-90f53105b524)

#### Wiring

![image](https://github.com/klenert17/Engineering_4_Notebook/assets/71406905/96c132ff-4466-4c7d-9543-b9177e54afaf)

#### Code

[CODE CODE CODE](https://github.com/klenert17/Engineering_4_Notebook/blob/main/raspberry-pi/CrashAvoidence1.py)

#### Reflection

This assignment was simple in wiring and a little harder to code. Once I understood what the gyro lines meant, I realized I can choose which axis it prints, making it much easier. f commands were also very helpful to learn.

### Part 2

#### Assignment description

For this assignment we had to make a warning light turn on if the breadboard is tilted at 90 degrees, and make it run on a battery, not connected to the computer.

#### Evidence

![My Project (2)](https://github.com/klenert17/Engineering_4_Notebook/assets/71406905/7ff06b49-610a-468e-99c9-b7572b5f45b9)

#### Wiring

![image](https://github.com/klenert17/Engineering_4_Notebook/assets/71406905/57c87275-acc1-43eb-bcbe-8ee2b327d60f)

#### Code

[PLEASE CLICK HERE PLEASE PLEASE PLEASE](https://github.com/klenert17/Engineering_4_Notebook/blob/main/raspberry-pi/CrashAvoidence2.py)

#### Reflection

This assignment allowed me to make a lot of progress, because it is no longer computer connected. The x commands that determine the angle of the ship were really cool to learn, but hard to understand. To figure out what 90 degrees was on each x side, I printed the number when the board was on its side, and saw that it was at 9 and -9. I then used the "or" statement and the "<" and ">" to make a area where the LED is not on, and once it surpasses the limits, the LED will turn on. 

### Part 3

#### Assignment description

For this assignment we had to add an onboard OLED screen to print live angular velocity values.

#### Evidence

![My Project (3)](https://github.com/klenert17/Engineering_4_Notebook/assets/71406905/c40a1bdc-23a9-4f49-9fdd-7838c3d60493)

#### Wiring

![image](https://github.com/klenert17/Engineering_4_Notebook/assets/71406905/d960e6b2-217e-4e2e-82ce-d96bd07d9aa3)

#### Code

[BIG BOY CODE](https://github.com/klenert17/Engineering_4_Notebook/blob/main/raspberry-pi/CrashAvoidence3.py0)

#### Reflection

The hardest part of this assignment was figuring out how to work with the OLED. learning the "\n" to break lines on the screen was super helpful. Setting up the board was pretty simple, I just needed to make sure all my SDA and SCL pins were connected in the same pin. I really enjoyed this assignment.

### Part 4

#### Assignment description


#### Evidence


#### Wiring


#### Code


#### Reflection



&nbsp;

## Launch Pad Assignment

### Part 1

#### Assignment description

Make the serial moniter count down from 10 and print launch

#### Evidence

![ezgif com-crop (1)](https://github.com/klenert17/Engineering_4_Notebook/assets/71406905/e4922663-b1d7-457c-87c2-d31b0cb214b5)

#### Wiring

No wiring for this assignment

#### Code

[CLICK HERE 4 CODE](https://github.com/klenert17/Engineering_4_Notebook/blob/main/raspberry-pi/LaunchCountown.py)

#### Reflection

This assignment was relativly easy because it was just hooking up the Pico to the comuter and having it print numbers. It took some time to think about how to make it count down rather than forward, but after some research and realizing I could move by negative incramates, it was pretty easy.

### Part 2

#### Assignment description

Make the countdown blink red every second it goes down and stay green after it launches using LEDs

#### Evidence

![ezgif com-optimize](https://github.com/klenert17/Engineering_4_Notebook/assets/71406905/59b4ba66-742c-4a9d-b2ac-b6c637dc2eb7)

#### Wiring

![image](https://github.com/klenert17/Engineering_4_Notebook/assets/71406905/31ae51fc-8f18-4f9b-8ff9-383184daac3b)

#### Code

[CODE CLICK HERE PLEASE PLEASER PLEAS](https://github.com/klenert17/Engineering_4_Notebook/blob/main/raspberry-pi/LED_Countdown.py)

#### Reflection

The hardest part of this assignment was the wiring. I have never wired a pico beofre and it was frustrating to not be able to see the number of which pin everything is going into all the time. After looking at the referance photo for the pins, I was able to wire it much easier. It was just two leds and two resistors, going into ground. 

### Part 3

#### Assignment description

Make the countodwn start after a button is pressed, with the LEDs lightingup for every second and holding green after liftoff

#### Evidence

![ezgif com-optimize (1)](https://github.com/klenert17/Engineering_4_Notebook/assets/71406905/340b06ce-6f8c-4992-b69a-3e9cdcde5520)

#### Wiring

![image](https://github.com/klenert17/Engineering_4_Notebook/assets/71406905/8fce6806-1e59-4c56-a567-d3cc3ac466c1)

#### Code

[PLEASE CLICK HERE FOR CODE PLEASE PLE$ASE PLEASE PLEASE](https://github.com/klenert17/Engineering_4_Notebook/blob/main/raspberry-pi/Countdown_Button.py)

#### Reflection

The code with this assignment was difficult because I had to remember how to use a button. After looking up some simple code and some of my old code, I was able to cobine parts to the previous part of this assignment and make it work. For wiring, I just connected the button to ground and to another GP pin.

### Part 4

#### Assignment description

We had to attach a servo to the pico, and make it urn 180 sgrees afet launch/10 seconds. 

#### Evidence

![ezgif com-optimize (2)](https://github.com/klenert17/Engineering_4_Notebook/assets/71406905/e4495764-404a-486d-9914-4a249cbba51c)

#### Wiring

![image](https://github.com/klenert17/Engineering_4_Notebook/assets/71406905/f838f153-a9e8-4978-8355-b40a95da6e21)

#### Code

[FINISHED CODE PLEASE CLICK PLEASE ITS GOOD I SAWR PLEASE PLEASE PLEASE](https://github.com/klenert17/Engineering_4_Notebook/blob/main/raspberry-pi/LaunchPad4.py)

#### Reflection

This assignment overall was pretty easy once I got back in the swing of coding. Wiring the servo was simple, and putting the code with it can pretty quickly. I had some trouble keeping track of which pins were which but I know I will get more used to it with practice.

&nbsp;

## Raspberry_Pi_LED_Blink

### Assignment Description

For this assignment we had to make the LED on the PI board turn on and off indefinetly. This was to get us used to working with the PI for the first time.

### Evidence 

![ezgif com-crop](https://github.com/klenert17/Engineering_4_Notebook/assets/71406905/f51fbd5b-524c-4dca-a3d4-da197d11b2f6)



### Code

[CODE HERE CLICK HERE!!!!!!](https://github.com/klenert17/Engineering_4_Notebook/blob/main/raspberry-pi/LED_blink.py)

### Reflection

Most of this assignment was setting up VS Code to work with the Raspberry Pi, and setting it up for a new year. As this was the first code assignment of the year, I was a little bit rusty but this code was very easy. It really wasn't any different from any other LED Blink Assignment I had dome previously, and it was even easier because there was no wiring. Putting #type: ignore at the top was a really helpful piece of information because the red code lines are so annoying

&nbsp;


## Raspberry_Pi_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence 

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

### Code
Give me a link to your code. [Something like this](https://github.com/millerm22/Engineering_4_Notebook/blob/main/Raspberry_Pi/hello_world.py). Don't make me hunt through your folders, give me a nice link to click to take me there! Remember to **COMMENT YOUR CODE** if you want full credit. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test


Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link

https://github.com/klenert17/Engineering_4_Notebook/blob/main/raspberry-pi/test.py

### Test Image

![zTXK9METB](https://github.com/klenert17/Engineering_4_Notebook/assets/71406905/2daf0cf4-3b75-4e1a-bfd5-c2787fb1a22e)

### Test GIF

![giphy](https://github.com/klenert17/Engineering_4_Notebook/assets/71406905/927df334-27e8-4c34-a122-2d8e73eb7b03)

