# Multiuser Blog

Derived from: Mele Django by Example 2 Chapter 1

Objective: to make it multi-user. Completed.

Master: Multi-user Blog with Restricted Pages
Shortcomings:
- No auto registration for subscribers or Authors
- No payment for subscriptions to restricted materials

------------------------------------

To Do:

Priority: 1
- Make it part of your portfolio
- Bootstrap it
- Put it up in production
- Portfolio:
    - multi-user blog
    - Scrapy
    - Selenium
    - API

- Add stock table screen
- Add API to IB

- Auto Registration for subscribers
- Paid site (for registration)

- Other Projects
Priority: 2
- Scraping with Scrapy
- Scraping with Selenium
- Any other API project?

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

004 Seggregate Login for subscribers. Login for authors.
004a User Group shown on sidebar
004b Redirect authors to blog/manage/ ; subscribers to blog/subscribed/
