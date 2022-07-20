### Introduction to Product Database Web Application ###

ProductDB is a web application that is for management
of a small product database.

It has categories feature that the system organizes products
under categories.

Currently, it has product add, update and delete features.

It may be used to manage a small and may be medium product inventory
and can be extended for other purposes like inventory and delivery
management, web based shopping cart or for similar applications.

### Main Design Philosophy ###

Main philosophy behinde the application design for this project is that keeping
its design as simple as possible to demonstrate various technologies like
Python, Flask, Ubuntu Linux, Docker, Jenkins and MS Azure.

Those are comprehensive and very capable tools in their own context. So that
keeping the app side as understandable as possible is the main philosophy.

### System Architecture ###

The web application records product data into MySQL database in two
tables; product and category. Product table keeps products while
category table keeping product category information.

The backend utilizes Python Flask web application framework.

Flask is on purposely selected that it is lean and micro enough
to start this type of application with extendible potential.

The frontend interface utilizes AdminLTE template of Twitter's
Bootstrap framework, which is responsive that it makes this application
mobile friendly as well.

SQLAlchemy library helps for database management in the backend codebase
that developer of the application saves fair amount of time by not being 
having to implement essential database features.

So that developer may spend time on application specific features.

Another benefit of using SQLAlchemy is that it makes the application
by default more secure than hand-coded database application layer usage.

SQL Injection attacks is being prevented by design and by defualt this way.

I run this application on Ubuntu Linux 20.04 on MS Azure that any Python 3,
Flask and MySQL installed linux system would be capable to run the application.

The system runs on a Docker container that one can utilize this design by taking
this application here. This way, developer does not have to install modules, libraries,
tools and all those same things one by one for each install like development
and production computer.

Docker image is being created by Jenkins by a pipeline that it gets the source
code of the application from GitHub. Then it runs tests and then it creates the
docker images.

Final stage of Jenkins pipeline is running the application in Docker container.

### Project Management ###

I use Trello for project management that I organise task in three different
categories; To Do, Doing, Done.

I think category names explain themselves.

I may use Scrum or Kanban but I think those are for teams consisting at least
couple of people.

I worked on my own in this project. So that To Do, Doing and Done style project
management is enough for managing my own project.

I use Trello to keep track of those three categories. Trello is simple but very
capable free web based service for managing any type of project.

I use coloured labels that Trello provides as labels. Colors do not have
any logical meanings in my project. The reason I use coloured labels is for
making it easy to see.

Each label is a point of difficulty that level increase as I add new labels.

For example 5 labels means it is a difficult task to implement. 4 is difficult
again but less then 5. Again, 2 and 3 has medium difficulty.

1 label means it is an easy to implement task.

You may have an idea below screenshot of my Trello board.

![Product Database Trello Board](/images/my-trello-board-21-07-2022.png)

