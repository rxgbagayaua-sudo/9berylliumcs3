# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)

## Existing Class
Class: Club
Description: Represents an ALP Club. Stores values such as name, adviser, number of members, and active status.

## New Related Class
Class: Member
Description: Represents a student that belongs to a club. Stores information such as name, grade level, and role in the club.

## Association
Relationship: Club has Members
Explanation: A club is associated with Members because it can contain, and manage multiple student members, with each member object representing an actual member of a specific club.

## Multiplicity
Multiplicity: 1 : 
Explanation: The multiplicity is 1 to 0..*  because 1 club can hold and manage zero or more members. This can be seen in a newly established club with zero members, and an old club with many members.

## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)

## Python Implementation
[View Python Source](classRelationships.py)

## Test Run
![Relationship Test Run](images/relationshipTestRun.png)

## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)

## Analysis
### What is the association between your two classes?
The association between my two classes is that a Club has Members. The Club class represents the organization, while each Member Object of the Member Class represents a student who is a part of the club.
### What multiplicity did you choose and why?
I chose 1 : 0..* multiplicity. Because one club can contain and manage zero or more members. This can be seen in a newly established club with zero members, and an old club with many members.
### How did you implement the relationship in Python?
I implemented the relationship using the members list inside the Club Class.The add_member method recieves a Member object, and then add that object to the list, allowing the club object to keep references of all the objects associated to it.
### Why did you store an object reference instead of copying its data?
I stored an object reference so that the club/class can access the actual members/objects instead of having a separate copy of its data.
### If your relationship uses many, why is a list appropriate?
A list is appropriate because one club can contain many members. Each item in the list is a reference to a separate Member object. This allows the program to look through the list whenever it needs access or displays the members of the club.