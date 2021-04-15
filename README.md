# Major
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Problem Statement - 
Information is available in many printed books.
Only people with sight can take advantage of this information.
People who are visually impaired cannot read the information from this type of media.
There are many ways for these people to grasp the information.
Some of which are Braille script, e-readers, etc.
These ways have proved over the years to be expensive.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Solution/Objective - 
To create a system - 
In such a way that  it serves as a interface between a blind person and a computer.  
In which Ascii characters are converted to braille for the reader to interpret. 
OCR involves the detection of text content on images and translation of the images to encoded text that the computer can easily understand. 
Which is made such that the characters from a text are sensed or input from computer and  a refreshable braille display that essentially take a text file and displayed the contents in the form of braille. 
Therefore, in order for the person to read any printed book with ease we have developed a system which is cost efficient and easy to use.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# FLOW -


/Braille_code.ino - is the code for the arduino uno

/Text_Recognition/cnn_model/train.py is the cnn model which is trained on MNIST data set

/Text_Recognition/cnn_model/digit_classifier.h5 is the trained model that you can directly use without having to train the model

/Text_Recognition/main.py is the code for the pygame window. The left hand size of the pygame window will take input and the right hand side will display the output. 
                          Use right click to clear the screen.
                          The output is also stored as text in /Text_Recognition.
                          
/Braille/src is the main code in which you need to run the file /Braille/src/StegnographyInText.java

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
