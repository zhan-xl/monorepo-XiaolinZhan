# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

Yes, in general the name of the function descripts what the function does.

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

List has order, and normally access the element by index. Dictionary does not keep order and access element by key.

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

Not really, the index has to within the size of the list.

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

It's convenient to store all data types without worrying about a type error. This could reduce program interrupted during run time. However, the disadventage is that when accessing the data, you would need to verify the data type before do anything, this leads to extra steps that slows down the program.

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

Yes the functions in request module are well named. They concisely describe what the function does. 

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

The prepare and send function also takes more than 5 arguments. 

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

**kwars stands for key arguments. This key word allows function to have arbitrary number of key word arguments. It's used when the function does not set a fix number of arguments. It can be bad because it's hard to document and make the function hard to understand. Also it causes mistake because the function does not know what key word will be used in advance. So it should only be used when necessary.

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

'None' is the default value for those arguments. You can set it to other value as well. Some arguments does not have a default value because the input matter or a default value would not make sense. Having a default value can reduce coding work when the default value is commonly used. Or you do not want people to change this value unless they intended to.
