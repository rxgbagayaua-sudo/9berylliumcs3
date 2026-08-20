# Computational Thinking Exercise

## Smart School Canteen Queue

**Name:** Rafael Xianrolf G. Bagayaua

**Section:** 9-Beryllium

**Last Name:** Bagayaua

**Date:** 20/08/26

## Step 1: Identifying the Big Problem

### Main Problem
    The PSHS school canteen has an inefficient ordering and payment process causing problems such as long lines, and crowding during lunch breaks.

## Step 2: Identifying the Sub-Problems

    1. Students take too long to decide what they want to order.
    2. The cashier has to manually compute the total cost of the orders.
    3. The canteen lacks a system to track whethe food items are running out.
    4. There is only a limited amount of space to hold the students, making it crowded during lunch time.

## Step 3: Appply Computational Thinking Skills

1.**Students take too long to decide what they want to order.**
**|Abstraction|**
    Create a menu that has all the necessary information such as food name, price, and availabilty. So that even before students get to the cashier they have already decided. Abstraction is applied here by removing distractions such as long desriptions, pictures, and brands of the ingredients, while focusing only on the needed information such as the name, price, and availabity.

2.**Manual cost computation**
**|Algorithm Design|**
    Create a program that automatically adds the prices of all selected items the student wants to buy. Algorithm design is applied because you are creating a step by step guide to help in calculating the prices, costs, and change that the cashier needs, making the process more efficient.

3.**Stock tracking system**
**|Pattern Recognition|**
    Track the number of each item sold, then use that data to identify which foods sell quickly, and are about to run out, alongside adjust the amount of stock to buy based on demand. Pattern recognition is used. Pattern Recognition is applied here since it looks at repeated trends to get data that the canteen can use to predict which items need to be restocked more often.

4.**Managing the canteen space**
**|Decomposition|**
    Divide the crowd into seperate areas, such as for payment waiting, and getting the food. Furthermore we can go deeper into the problem by creating different schedules for lunch breaks so that it is not every student in the canteen at the same time. Decomposition is applied here because the sub-problem is broken down into even smaller parts that can be solved seperately such as where ther students order, pay, wait for food, pick them up, eat, and when different groups of students have their lunch breaks.

## Step 4: Algorithmic Solution

### Sub-Problem Number 2 - The cashier has to manually compute the total cost of the orders.

### Pseudocode

Start

Set total = 0

Ask customer for a food item
Get the price of the food item
Add the price to the total

Ask if customer wants another item

If yes
    Repeat the food selection, price identification, and price addition steps.
Else
    Display total cost

Ask for the amount paid

Calculate the change
Change = amount paid - total

Display change

End



