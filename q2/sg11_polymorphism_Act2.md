### Activity 2 - Duck Typing

1. Answer the following questions:
a. What is duck typing, as explained in the video?
    Duck typing is a form of polymorphism that allows objects from different classes to be used in the same way, given that they have the required methods and attributes.

b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
    The Car class needs the speak() method and the alive attribute, just like Dog, and Cat classes. This allows it to work in the same loop without inheriting from the Animal Class.

2. Create the Python code that:
a. Creates three classes: Car, Boat, and Drone with a method move().

    move() in the Car class prints "The car drives on the road."

    move() in the Boat class prints "The boat sails on water."

    move() in the Drone class prints "The drone flies in the sky."

b. Has a function named start_trip(vehicle), with a parameter vehicle, that simply calls the
move() method: vehicle.move().

c. Creates one object of each class.

d. Calls the start_trip() method for each object.

[View Python Source](sg11_polymorphism_Act2.py)

3. How does the code in 2.2 demonstrate polymorphism?
    The code shows the application of polymorphism since Car, Boat, and Drone classes all have the same move() method, but it perfroms a different output depending on the class. Furthermore it shows polymorphism without inheritance since the start_trip() method can call the method on any of the objects without the use of inheritance.