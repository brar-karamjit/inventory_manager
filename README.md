# Candy Store :shaved_ice:

Tech stack 
Frontend - HTML, CSS
Backend - Python
Framework - Django
Databse - Sqlite 3
Hosting - Heroku

It is a simple candy store where users can purchase cnadies from. You can view the stock of every item. It also
permits you to remove an item, add a new item and purchase multiple items at a single time.

## How to guide -

Access link - https://guarded-plains-11100.herokuapp.com/
It is deployed on Heroku (Paas) so you can use the app by simply clicking on the above link or copy paste in your
browser

### Purchasing 
Once on home page enter the quanity you want to buy, click buy and it will take you to a purchase confirmation page
and update the quantity in store database.

### Purchasing
In the navbar section you can click "Products" to view the inventory.

### Add new item
Scroll down to the section which says "Let's add a new candy to our store." and fill in the form. You can add url of
the image you want to attribute to item, Name of candy and quantity. Finally click "add to list" and you should be able 
to see newly added item on home page.

### Remove an item
Scroll down to section with gift box as background, header of section should say "take the whole box home", simple select from
dropdown menu the item you want to remove and click "Take it home" buttom.

### purchase multiple items
Go to the section which says assorted order. It lets you select 3 items from dropdown menu and the individual quantities.
It will again take you to order confirmation page and update the inventory.


## Future ideas
1. As you can see right now login is not required, I would want to implement a user signup and login feature. So that one 
can track purchase history.
2. Move the deployment from Heroku to AWS.

