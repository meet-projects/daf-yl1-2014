Michele's feedback
---

Great job finishing your project! 

* The design is fantastic, and the colors fit really well together. 
* One problem with the interface in general is that your buttons are on top of each other, and sometimes their functionality is confusing. I press one button but actually get the function of a different button. 
* Good job with your `Button` class. However, you don't need to define methods like `setTextSize`, because in Python you can just set the text size by saying `OBJECT.textSize = 7` directly. 
* In your `draw` method in your `Button` class, you initialize pygame, and that's bad! When you initialize pygame, what you do is re-darw the entire screen. You basically only want to do this in the main method of your code. 
* I liked your use of a `click` method - awesome. 
* Your `Label` and `Button` classes are very similar - there probably should have been a subclass relationship: a `Button` is a subclass of `Label`, and it adds a few methods and variables to the `Label`. It would have saved you some code and some testing. 
* Good job using classes and subclasses in your `dafClasses` file. It looks great, and a good use of classes and subclasses. 
* Great use of global variables and booleans to keep track of which screen is shown and used. This also made extending your cart much easier - great job. 