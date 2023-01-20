# Inventory Manager :shaved_ice:

Tech stack 
Frontend - HTML, CSS
Backend - Python
Framework - Django
Databse - Sqlite 3
Hosting - Heroku

It is a simple inventory manager where employees can update the inventory everytime they borrow/use a tool. You can view the stock of every item. It also
permits you to remove an item, add a new item and purchase multiple items at a single time.

## How to guide -

Access link - https://guarded-plains-11100.herokuapp.com/
It is deployed on Heroku (Paas) so you can use the app by simply clicking on the above link or copy paste in your
browser

### Borrowing 
Once on home page enter the quanity you want to buy, click buy and it will take you to a purchase confirmation page
and update the quantity in store database.

### Inventory
In the navbar section you can click "Products" to view the inventory.

### Add new item
Scroll down to the section which says "Let's add a new tool to our store." and fill in the form. You can add url of
the image you want to attribute to item, Name of tool and quantity. Finally click "add to list" and you should be able 
to see newly added item on home page.


### purchase multiple items
Go to the section which says assorted order. It lets you select 3 items from dropdown menu and the individual quantities.
It will again take you to order confirmation page and update the inventory.


## Future ideas
1. As you can see right now login is not required, I would want to implement a user signup and login feature. So that one 
can track history.
2. Move the deployment from Heroku to AWS.

