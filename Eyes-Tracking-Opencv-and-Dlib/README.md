# Eyes Tracking Opencv python :eye: :eye:

## TODO

- [x] Eyes landmark Detection :eyes:
- [x] Blink Detector and Counter
- [x] Extracting Eyes using Masking Techniques
- [x] Threshold Eyes
- [x] Dividing Eye into Three Parts **Right Center Left**
- [x] Counting Black in Each part and Estimating The Position of Eye
- [x] Controlling RGB LED's Color With Eyes

## Installation

Steps are involved to run the code.

### Requirements are :

1. install Dlib

   #### For Windows

   - Inorder to install dilb on windows machines you need following: :smirk:

     - Visual Studio
     - Visual Studio Build Tools
     - Cmake

       for More Detail check out this Blog post. [here](https://medium.com/analytics-vidhya/how-to-install-dlib-library-for-python-in-windows-10-57348ba1117f)

   `pip install cmake `

   `pip install dlib`

   #### Linux or Mac OS

   - Just you need Cmake that all here on linux and Mac OS
   - install Dilb uisng Pip command

     `pip3 install cmake`

     `pip3 install dlib`

     for more details [see](https://www.pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/)

2. Install opencv-python
   `pip install opencv-python`
   for linux or Mac OS replace`pip` with `pip3` and you are good to go... :wink:

3. Download landmarks [Predictor](https://github.com/davisking/dlib-models/blob/master/shape_predictor_68_face_landmarks.dat.bz2)
   - Extract that file and put it into the **Predictor** folder or directory.