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