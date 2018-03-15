# Iris Recognition

I build an `Iris-Recognition system`, implemented on both Matlab and Python languages.
#### Keyword: Iris Recognition, Computer Vision, Image Processing, Daugman


Table of contents
=================
- [Iris Recognition](#iris-recognition)
- [Table of contents](#table-of-contents)
- [I.Introduction](#iintroduction)
- [II.Description](#iidescription)
- [III.Prerequisites](#iiiprerequisites)
- [IV.Folder structure](#ivfolder-structure)
- [V.MATLAB implementation](#vmatlab-implementation)
- [VI.Python implementation](#vipython-implementation)
- [VII.Result](#viiresult)


I.Introduction
==============
* In the last summer 2017, I met my teacher in the course Digital Signal Processing. He recommended me Biometrics topic. Since there, I have started exploring about Biometrics, such as Fingerprint, Iris, Face.
* I searched on the Internet and found out an open-source Iris Recognition model, which written on Matlab. Thanks to the author of this open-source code, I can build up my own system. [Here is information about the author](http://www.peterkovesi.com/studentprojects/libor/sourcecode.html):\
``
Libor Masek, Peter Kovesi. MATLAB Source Code for a Biometric Identification System Based on Iris Patterns. The School of Computer Science and Software Engineering, The University of Western Australia. 2003.
``
* Based on this available functions, I have modified, connected, and designed my individual system on Matlab. Subsequently, I have also converted Matlab version into Python one.
* My contribution is creating a GUI so that user can use this as a convenient software. Moreover, in my modified system, I utilized hardware to boost the runtime performance to make is faster, comparing to the original version.
* The testing experiment shows that these two forms had fairly equal accuracy. In addition, because of the C++ platform, Matlab implementation seems faster a little bit than Python.


II.Description
==============


III.Prerequisites
=================
* Because I write the GUI using App designer, and only update versions of Matlab (from R2016a) have this feature. Therefore, to be able to run code, your Matlab version must be R0216a or higher.


IV.Folder structure
===================
.
+-- CASIA-database
|   +-- 001_1_1.jpg
|   +-- ...
|   +-- 108_2_4.jpg
|
+-- matlab
|   +-- fnc
|       +-- addcircle.m
|       +-- ...
|   +-- template-database
|       +-- 1.mat
|       +-- ...
|   +-- Iris-Recognition-GUI.mlapp


V.MATLAB implementation
=======================


VI.Python implementation
========================


VII.Result
==========
Hardware board:
<img src="pictures/Hardware-board.jpg" alt="Drawing" style="width: 700px;"/>

Hardware board connected to home electric network:
<img src="pictures/Connect-to-electric-network.jpg" alt="Drawing" style="width: 700px;"/>

Mode test (Test handy and automatic modes):  
https://youtu.be/6kZmtNLPiIU

Alarm tests (On and Off alarm):  
https://youtu.be/Bq2uVIg-Ajc  
https://youtu.be/PRSb5gKpI5M  
