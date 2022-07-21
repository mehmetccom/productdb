### Introduction to Product Database Web Application ###

ProductDB is a web application that is for management
of a small product database.

It has categories feature that the system organizes products
under categories.

Currently, it has product add, update and delete features.

It may be used to manage a small and may be medium product inventory
and can be extended for other purposes like inventory and delivery
management, web based shopping cart or for similar applications.

You can access the product database web application with below link:

[Product Database Application](http://20.0.8.181:5000/)

### Main Design Philosophy ###

Main philosophy behinde the application design for this project is that keeping
its design as simple as possible to demonstrate various technologies like
Python, Flask, Ubuntu Linux, Docker, Jenkins and MS Azure.

Those are comprehensive and very capable tools in their own context. So that
keeping the app side as understandable as possible is the main philosophy.

### MoSCoW - Method Project Features ###

I have used MoSCoW technique to define feature set of the project.

Please refer to MoSCoW.md file in this folder for full details.

Here its link also below

[MoSCoW File](https://github.com/mehmetccom/productdb/blob/main/MoSCoW.md)

### Database Design ###

The web application records product data into MySQL database in two
tables; product and category. Product table keeps products while
category table keeping product category information.

![Database Design](/images/db-design-20-06-2022.png)

### Web Application Architecture ###

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

### System Architecture ###

I run this application on Ubuntu Linux 20.04 on MS Azure that any Python 3,
Flask and MySQL installed linux system would be capable to run the application.

The system runs on a Docker container that one can utilize this design by taking
this application here. This way, developer does not have to install modules, libraries,
tools and all those same things one by one for each install like development
and production computer.

You can see the holistic view of the system in the below hand depicted image.

![Holistic View](/images/holistic-view-21-07-2022.jpg)

Let me briefly explain how CI/CD works;

* Developer commits and pushes changes to GitHub
* As soon as a commit happens, a GitHub webhook executes and it does an HTTP post to Jenkins server
* Jenkins server starts the corresponding pipeline when it gets triggered by GitHub webhook
* Jenkins pipeline executes the first stage
* First stage in the pipeline automatically gets source code from GitHub (Declarative Checkout SCM)
* Then stages Test, Undeploy, Docker Image Build and Deploy gets executed automatically
* Docker Daemon on Ubuntu Linux runs the Python Flask web application
* Python Flask web application servers on port 5000 to users' web browsers


### CI/CD with Jenkins ###

Docker image is being created by Jenkins by a pipeline that it gets the source
code of the application from GitHub. Then it runs tests and then it creates the
docker images.

Final stage of Jenkins pipeline is running the application in Docker container.

![Jenkins Pipeline](/images/jenkins-pipeline-21-07-2022.png)

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

### Product Database Web Application Screenshots ###

Below screenshot is a composite of three screenshot of the application
that it displays product listing, add new product and update a product.

![Product Database Screenshot](/images/product-db-screenshot-whole.png)

### Microsoft Azure Ubuntu Linux 20.04 Server Virtual Machine ###

You can see the ubuntu linux server virtual machine on MS Azure in below
screenshot. It is MS Azure dashboard.

Please note that the marked public IP section of the server that you can
access the product database web application with below link:

[Product Database Application](http://20.0.8.181:5000/)

![Linux Server VM on MS Azure](/images/ms-azure-dashboard-my-linux-server-vm-21-07-2022.png)

### Important Security Notes & TODO ###

* Please do not use it on production without a careful investigation of the codebase
* Database username, password and MySQL connection URI is hard in the codebase. So that
it is a risky in terms of cyber security. Please use docker -e or --env-file argument
with an environment file that you can store those values instead of using them
hard coded in app.py file.

Here you can find more information about -e and --env-file arguments of docker command
line utility.

[Docker -e and --env-file parameters](https://stackoverflow.com/questions/30494050/how-do-i-pass-environment-variables-to-docker-containers)

### Notes About Testing The Application ###

I have used Python's default unit testing framework and flask_testing of Flask
web application framework.

Here you can check out the details of Python's unittest:

[Python Unittest](https://docs.python.org/3/library/unittest.html)

The purpose of using unittest instead of popular unit testing framework Pytest is
that I wanted to keep testing as simple as possible.

Here you can check out Pytest for further information.

[Pytest](https://www.pytest.org)

I think I achieved my purpose that Jenkins pipeline stops
when any test fails so that no new deployment if a test fails.

There is always room for improvement that I can write more and better
tests using Pytest in future versions of this application.

### Areas To Improve ###

I think there is always room to improve your craft.

This web application is a proof of concept that demonstrates

Web Development with Python Flask, MySQL HTML and CSS on Docker, Ubuntu
and MS Azure.

**Some areas to improve;**

* Docker Swarm facility may be used to make it auto-scaling application
* Docker Compose may be used to automate Docker related things
* Hard coded folder and file names can be made variable
* Similarly, hard coded username, password and database connection URI may be variable
* [Nginx](https://nginx.org/) web server can be used along with [Gunicorn](https://gunicorn.org/) instead of Flask web server
