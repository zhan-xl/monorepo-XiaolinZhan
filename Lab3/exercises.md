# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is Object an abstract or a concrete class? Explain why:
	- Object is a concrete class. Becasue an object contains information and it is initiated to represent something, whereas abstract class is normaly used as a templete for other class.
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- This method is called when the instance of the class is about to be delete. By inplement this method to ensure that the instance is properly decounstructed.
1. What class does Texture inherit from?
	- Image class.
1. What methods and attributes does the Texture class inherit from 'Image'? 
	- Attributes: width, height, colorChannels, pixels;
	- Methods: getWidth, getHeight, getPixelColorR, getPixels, setPixelsToRandomValue.
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- I think the Texture class has a 'is-a' relationship with Image. The Image class can have multiple children like Textrue class to be shown on the screen.
1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- Because the texture class passes it's constructor to the super class(Image)

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

  - Singleton in Python is not thread safe. Becasue it uses _instance as a flag for the existency. So one thread could read None when the order thread already created the instence but not yet change the flag.
  
