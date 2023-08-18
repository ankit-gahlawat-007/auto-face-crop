# auto-face-crop

<img width="1249" alt="auto-face-crop" src="https://github.com/ankit-gahlawat-007/auto-face-crop/assets/139246379/f851a416-18c1-42c3-a8ad-f48748b473b7">

--------------------------------------------------------------------------------

**auto-face-crop detects and crops the face with some additonal features** <br>
It was a pre-requisite for passing face image (a square image of L x L dimensions) for one of the project, so I uploaded the file here.  

It contains the following steps: <br>
(Steps 1 and 2 can be skipped based on the requirements.)

**Step 1: Set white background for the image** <br>
Reference: https://github.com/danielgatis/rembg

**Step 2: Make the image square, by using white background** <br>

**Step 3: Crop the image with detected face as face_percent of the total output image** <br>
Reference: https://github.com/leblancfg/autocrop

It outputs a 500 x 500 dimension image by default. It can be changed by adding suitable parameters to the Cropper class.



