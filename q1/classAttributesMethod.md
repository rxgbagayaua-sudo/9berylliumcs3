# Class Attributes and Methods

## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)

## Design Revision
The major changes I did was adding the methods, updatemembers, and getmembers, and adding the attribute's visibility

## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
|Name |String |public |The club's name is a general attribute of the respective ALPs which can be displayed freely |
|Name of adviser |String |public |The club adviser is a general attribute of the respective ALPs which can be displayed freely |
|Number of Members|Integer |private |The number of members a club has needs to be protected so that it will not accidentally get changed to an invalid numbers such as a negative number |
|Active Status |Boolean |public |The active status is general information that members/ aspiring members may need to check |

## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)

## Python Implementation
[View Python Source](classImplementation.py)

## Test Run
![Test Run](images/classTestRun.png)

## Object Diagram
![Object Diagram](images/objectDiagram.png)

## Analysis
### Why did you make your chosen attribute private?
I made the number of members private becuase it should not be directly changed, because it can become an invalid number, such as a negative number. Making the attribute negative ensures that the number of members can only be changes through the proper methods of the class.
### Which method changes the state of your object?
THe method that changes the state of my object is add_member(), because it modifies the number of members in an object.
### How did your two objects demonstrate that instances are independent?
The two objects demonstrated independence since we see that using a method to change attributes of object 1 does not affect the attributes of object 2. Even though the object were created using the same class blueprint, each object can store their independent values.
### What is the difference between your class diagram and your object diagram?
The class diagram shows the general blueprint of the class, such as its attributes, data types, visibility, and methods. On the other hand, the object diagram shows the specific objects created using the class blueprint and displays the actual values stored in each object.
