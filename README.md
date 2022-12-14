<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://bitbucket.org/alimetry/r-d-gui/src/master/">
    <img src='./GUI_images/alimetry.png' alt="Logo" width="80" height="80">
  </a>

<h3 align="center">GUI Spatial labelling</h3>

  <p align="center">
This GUI allows Alimetry Spatial metrics team to labels the propagation of the stomach waves. 
    <br />
    <a href="https://alimetry.com"><strong>Explore the website ></strong></a>
    <br />
    <br />
    <!-- <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a> -->
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary> Table of Contents </summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#running-the-code">Running the code</a></li>
        <li><a href="#standalone-application">Standalone application</a></li>
      </ul>
    </li>
    <li><a href="#usage-of-the-GUI">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Main page][product-screenshot]

This project aims to create a standalone application for macOS to label the propagation of the stomach waves recorded by the Alimetry device. This application makes it very easy to label these videos and also facilitate the viewing of the videos. the data collected with the labeling of videos will allow to analyze and quantify the importance of the propagations of the waves of the stomach during a digestive disorder. This project is led by Alimetry's spatial metrics team.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/2048px-Visual_Studio_Code_1.35_icon.svg.png" alt="VS Code" width="20" height="20"></a> <a href="https://code.visualstudio.com"> Visual Studio Code </a>has been used a along this project to edit the code.
*   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png" alt="Python" width="20" height="20"></a>    This application has been developped in <a href="https://www.python.org/"> Python v3.10</a> using different libraries :
    
    * <a href="https://docs.python.org/3/library/tkinter.html#module-tkinter">tkinter</a> to develop a Python GUI with several widgets :
        * Tk
        * Frame
        * Label
        * Button 
        * OptionMenu
        * Entry
        * Text 
    * <a href="https://docs.python.org/3/library/tkinter.ttk.html#module-tkinter.ttk">tkinter.ttk</a> for a specific widget :
        * Progressbar
    * <a href=https://docs.python.org/3/library/dialog.html#module-tkinter.filedialog>tkinter.filedialog</a> to allow the user to specify a file to open or save.
    * <a href="https://pandas.pydata.org">Pandas</a> to collect data in arrays and export them in a .csv file.
    * <a href="https://docs.python.org/3/library/os.path.html">os.path</a> to process files from different places in the system.
    * <a href="https://pillow.readthedocs.io/en/stable/">PIL</a> to process images from numpy array (raw data) before displayimg them.
    * <a href="https://numpy.org">numpy</a> to save the raw data in arrays.
    * <a href="https://scipy.org">scipy</a> to interpolate the data.
    * <a href="https://docs.python.org/3/library/glob.html">glob</a> to find all the pathnames matching a specified pattern.
    * <a href="https://matplotlib.org">maplotlib</a> to color the frames of the video with Colormap.</p>
    * <a href="https://matplotlib.org">py2app</a> to create a standalone macOS application from a Python file.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This GUI can be used by running the code in a code editor or directly in your mac terminal if the code Python is in your working directory. 

Or you can also create a **standalone application** which will allow the GUI to be used on every macOS devices without needing to have Python installed on it.

### Prerequisites

The software needs the previous libraries to be installed in order to run properly. These librairies and their version are listed in the `requirements.txt` file. You can install all of them by writting the following command in your terminal.

* Requirements
  ```sh
  pip install -r requirements.txt
  ```

* avgWaveData8by8</p>
You need to put the numpy arrays 8by8 containing the raw data you want to label in the **avgWaveData8by8** folder. The name of the arrays should be 
**{case}.npy**

* perWinFrames </p>
This folder should contain the .png images of the case you need to label, the name of these images should be **{case}-{picture:02d}-{frame:02d}.png**

* perWinAnimations </p>
If you want to label the videos using the mp4 files, you need to put them in this folder under the name **{case}-{picture:02d}-animation4hz.mp4**

### Running the code

1. Download the latest version of <a href="https://www.python.org/downloads/">Python</a> (v3.10) 
2. Clone the repository in a chosen directory
   ```sh
   git clone https://Imer_310@bitbucket.org/alimetry/r-d-gui.git
   ```
3. Make sure the file `logo.png` and the folders `Instructions` and `avgWaveData8by8` are in the same directory as the code `GUI.py` before you execute it.

4. Execute the code `GUI.py` 
   ```py
   python3 GUI.py
   ```

5. Read the instructions to know how to use correctly the GUI. They are  included in one of the page of the GUI.


### Standalone application

You can also create a standalone macOS application of the GUI if you execute the code `setup.py` with the py2app Python setuptools command.  

1. Install py2app using this command in the terminal.
   ```py
   python3 pip install -U py2app
   ```
2. Make sure the file **logo.png** and the folders **Instructions** and **avgWaveData8by8** are in the same directory as the code `setup.py` before you execute it.

3. Clean up your build directories in your working directory
   ```py
   rm -rf build dist
   ```

4. Build the app in your working directory
   ```py
   python3 setup.py py2app
   ```

5. Find the app in the dist folder which has been created in your current directory and move this application to your Applications directory.

6. Use the app on your device or share it to other mac users. Each time a modification will be added in the code, the application will need to be rebuild to have this modification.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage of the GUI

To use correclty this application, please read the instructions contained in the pages of the GUI. These instructions will teach you how to label the videos and to use effectively the GUI with the keyboard shortcuts included. </p>
The code save automatically your labelling work in the csv file you are currently working in. So no need to save your work at the end and do not worry if something wrong like a crash or a bug happen on your computer.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Header 
    - [x] Logo and welcome page
- [x] 1-window design 
    - [x] Direction drop-down menu
    - [x] Stability drop-down menu
    - [x] Confidence drop-down menu
    - [x] Display .mp4 video
        - [x] Looping video
- [x] show data already filled in 
- [x] Progressbar at the top to switch between different time slots
- [x] Labelling instructions 
    - [x] V0
    - [x] V1
- [x] Start a new labelling work
    -[ ] Iterate name if a new one exists already
- [x] 3-window design (display previous and next video)
    - [x] Direction drop-down menu
    - [x] Satbility drop-down menu
    - [x] Comment section (optional)
    - [x] show data for previous and next picture if already filled in
    - [x] Display .png frames as video
- [x] Resume labelling 
    - [x] From a .csv file
    - [x] From a .xlxs file
- [x] GUI instructions 
    - [x] V0
- [x] Indicate cases and picture already treated
    - [x] Color of buttons in the progressbar
    - [x] Symbol next to a treated case 
        - [x] Improve speed by updating the list at every case
- [x] Display processed numpy arrays as frames of a video 
- [x] Decrease size of the application 
    - [x] Use raw array without processing 

See the [feedback](https://bitbucket.org/alimetry/r-d-gui/src/master/feedback.txt) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions of any sort will be **greatly appreciated**.

If you have a suggestion that would improve the code, please 
let me know by contacting me or any member of the Alimetry Spatial metrics member. Or you can directly fork the repository and create a pull request. 

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AddFeature`)
3. Commit your Changes (`git commit -m 'Add some new feature'`)
4. Push to the Branch (`git push origin feature/AddFeature`)
5. create a pull request

You can also simply write your suggestion in the `feedback.txt` file and we will see want we can do.
Thanks again!

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Remi Picard - remi.picard@alimetry.com

Project Link: [https://bitbucket.org/imer_310/](https://bitbucket.org/imer_310/)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[product-screenshot]: ./GUI_images/screenshot.png
[logo]: ./GUI_images/alimetry.png