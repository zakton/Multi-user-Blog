# Multiuser Blog

Based on Mele Django by Example 2 Chapter 1

Objective: to make it multi-user.

------------------------------------

To Do:

004 Seggregate Login for subscribers. Login for authors.


------------------------------------

Done

001 - Create form to create a blog.
... make it complete, view, create, edit, delete.

002 - Allow blogger as a user to create a blog
  a. Introduce OwnerPostMixin ... Done
  c. Create author1, Restrict for create, update, delete
      - Create login, logout etc.
  d. Manage (dashboard) screen for Authors
  002e Clean up separating views for public and authors.

003 Two classes of blog: public and restricted. Subscriber can view subscribed posts. (url: blog/subscribed).
