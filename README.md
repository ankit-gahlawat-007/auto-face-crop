# auto-face-crop

This code auto detects face and crops it. <br>
It was a pre-requisite for passing face image (a square image of L x L dimensions) for Audio2Head: https://github.com/wangsuzhen/Audio2Head

It contains the following steps: <br>
(Steps 1 and 2 can be skipped based on the requirements.)

**Step 1: Set white background for the image** <br>
Reference: https://github.com/danielgatis/rembg

**Step 2: Make the image square, by using white background** <br>

**Step 3: Crop the image with detected face as face_percent of the total output image** <br>
Reference: https://github.com/leblancfg/autocrop

It outputs a 500 x 500 dimension image by default. It can be changed by adding suitable parameters to the Cropper class.

