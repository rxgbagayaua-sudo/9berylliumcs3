# SG4 - Understanding Classes and Objects
## **CLASS**: *Clubs*
## My class “*Clubs*” represents the different ALP clubs that have been active in PSHS-BRC.
## Properties
| Property | Data Type | Description |
|---|---|---|
|Name |String |This is the name of the Club|
|Adviser |String |The name and information of the Club Adviser |
|No. of Members |Integer |The number of Members |
|Active Status |Boolean  |Indicates if the club is active/open or not |
## Methods
| Method | Description |
|---|---|
|displayInfo() |Displays all the information about the club, Name, Adviser, Members, and its Status |
|displayContributions(name) |Displays the contributions of the given person/name for the club |
|scheduleActivity() |Adds an activity to the club schedule|
## Class Diagram
![Class Diagram](images/classDiagram.png)
## Design Explanation
### Why did you choose this class?
I chose this class because, I always have a hard time trying to pick Clubs during the start of the year. So I believe if we have a system that displays information, such as Adviser, previous members, and activities. I also think that this can be used to reestablish inactive or abandoned clubs, by showing said club's information, like previous name, and activities.
### Which property is the most important? Why?
For me the most important property would be the name, I believe this because the name of a club or organization carries everything it stands for, its values, its image, and its identity is all connected to the name it carries, so when you think of a club like Polaris, you immediately think of physics, or when you think of Pisay Harmonia, you think of the chorale, so that's why I believe that the name is the most important property.
### Which method is the most useful? Why?
The most important method would be displayinfo() since it displays all the necessary information you need to know about the club upon a single command. This method can display the name, adviser, list of members, activities, contributions to the school, and upcoming events led by the club. This can also be used to make it easier in deciding which club you are best suited for, and what club you are best aligned with based on those information.

## Design Revision

Changes from my previous design:
- I changed the method "scheduleActivity()" into "scheduleActivity(activity)" so that the method can accept a name to put into the schedule.

| Attribute | Data Type | Visibilty | Why Public/Private|
|---|---|---|---|
|Name|String |Public |The club's name is a general attribute of the respective ALPs which can be displayed freely |
|Adviser|String |Public |The club adviser is a general attribute of the respective ALPs which can be displayed freely |
|No. of Members |Integer |Private |The number of members a club has needs to be protected so that it will not accidentally get changed to an invalid numbers such as a negative number |
|Active Status |Boolean |Public |The active status is general information that members/ aspiring members may need to check |

## Updated Class Diagram

![Class Diagram](images/)