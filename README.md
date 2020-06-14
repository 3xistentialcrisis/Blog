# Blog Today
Your Unique Personal Blogging Website
## Author

[Wanjiku Karanja](https://github.com/3xistentialcrisis/Blog)

# Description
This  is a flask application that allows users to:
1. Post Blogs
2. Edit Blogs
3. Delete Blogs
4. Subscribe to Blogs
5. Comment on Blogs  

Subscribed Users receive notification emails every time a new blog is posted.

## Live Link
[View Site](https://blogtoday.herokuapp.com)

## Screenshots
<img src="" width="900px" height="440px">

## User Story
This Website enables Users to:
1. View the blog posts on the site
2. Comment on blog posts
3. View the most recent blog posts
4. Receive an email alert when a new post is made by joining a subscription.
5. See random quotes on the site

This Website Enables Writers to:
1. Sign in to the blog.
2. Create a blog from the application.
3. Delete comments that I find insulting or degrading.
4. Update or delete blogs they have created.

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load Blog Today Webpage | **On page load** | View all Blogs, Signup or Login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to Login Page|
| Select Login | **Username** and **password** | Redirect to Homepage. You Can now view and/or subscribe to Blogs|
| Select comment button | **Comment** |Comment Form Displayed|
| Click on submit |  | Redirect to All Comments Page|
|Subscription | **Email Address**| Flash message "You are Successfully subscribed to Blog Today!"|

## Technology used

* [Python3.8](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)
* Postgres
* Pip
* Html and CSS (Bootstrap)

# Test Driven Development (TDD)
To test this application, run this commands in the terminal;

$ python3.8 manage.py test

# Known Bugs
There are no known bugs at the time of its creation.

# Code Beat
[![codebeat badge](https://codebeat.co/badges/61881488-2da3-4522-be01-0226f8d1a6c6)](https://codebeat.co/projects/github-com-3xistentialcrisis-blog-master)

# Contact Information 
To get more help email the Administrator at admin@pitch.com

# License
[![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/3xistentialcrisis/blog/blob/master/LICENSE)