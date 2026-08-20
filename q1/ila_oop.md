# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
**Explanation:** Encapsulation, the process of keeping related data and functions together inside an object can be applied in the scenario by keeping a product's information, such as its **name**, **price** and **quantity**. The methods, **update_stock()** or **change_price()**, can be used to directly modify the product's data without having to directly access the product's information. This is helpful because it keeps related data and actions together, preventing incorrect changes in the inventory.

### 2. Abstraction
**Explanation:** Abstraction, the process of hiding complicated details, and showing only the important parts that are needed can be applied in the scenario by hinding the complex information in functions such as **sell_product()** wherein you only show that you sell the item, not the automatic decrease in inventory, etc. This helps to make the system easier to use since it hides unnecessary details the user does not need to know.

### 3. Inheritance
**Explanation:**Inheritance, the process that allows one class to recieve the properties of another class, this can be applied in the scenario by the different products, such as *foods*, and *drinks* inheriting the common characteristics of being a **product**(name, price, and quantity). This helps because instead of rewriting new features for a new type of product you just reuse and "inherit" the features of the **product class**.

### 4. Polymorphism
**Explanation:**Polymorphism, the process that allows the same method to behave differently depending on the object that is using it. This can be applied in the scenario through **display_info**, wherein it can show the **expiration date** for *food items* while showing **container size** for *drink items*. This helps because we from a singular method we can make it useful to many different objects even though it is the same method.

## Reflection
*Among the four pillars of Object-Oriented Programming, which do you think would be most useful in improving the sari-sari store inventory system? Explain your answer*

Among the four pillars of Object-Oriented Programming, I think that Abstraction would be the most useful since it allows complicated processes, such as calculating sales, checking inventory, and updating stock to be hidden behind simple methods like **sell_products()**. I think this especially because running a sari sari store should be simple, and easy, and this was the most helpful between the four to achieve that