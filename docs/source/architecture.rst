Architecture choices
************************
Notes on technology choices.

Language School is a simple CRUD application with PostgreSQL database.

Hosting
=========
It will be mainly used by language school administration office, therefore
it is enough to host it on single server with few workers as it has limited number of users.
Therefore is no need for load balanceer or separate servers for db, static files etc.

I have a staging environment setup on digital ocean Ubuntu 18.04 server.
More notes are in my blog post `LINK <https://pbedn.github.io/post/2019-best-django-hosting/>`_

Backend framework
===================
Django vs Flask: for typical CRUD application Django as a batteries included
framework wins easily.

CSS framework
===================
Bootstrap 4 vs Bulma: First tried Bulma as it looks cleaner and more fresh,
but with better community and tutorials old school css framework wins.

And why not separate frontend application in React or Vue.js. Well there is no need
as django templates work fine for my simple case. Response from server is very fast
so for user experience it is most important.

Continuous Integration
=======================
I have previous experience with CircleCI service. They use yaml configuration files
and provide service for free in open source projects. I can create workflows
to test, send results to other services for example Codecov (code coverage) and deploy.

Continuous Delivery
===================
Currently I am using CircleCI workflow that activates bash script. But I recognize this solution
as temporary, and in future will use Ansible configuration tool for provisioning and deploy.

Email server
===================

Options
--------

1. Increased privacy and configuration:
When increased privacy is required, good option is to setup own email server.
This is easy currently with open source software like *mailinabox*,
which gathers necessary components and presents one-click email appliance.
However maintenance is time consuming and we have additional cost of hosting email server.

2. Specific requirements:
If only outgoing emails are needed, one option is to setup only Mail Transfer Agent (MTA)
such as Postfix. ..

3. Effortless setup:
Another option is to use online mail service from Google, Microsoft etc.

4. Hosted email delivery services
In case of need for transactional emails, some options are sendgrid, mailgun etc.

Choice
----------------
I need to only to send email to users on account creation, password reset and with
invoices. For that option 2 and 4 could be good. I decide with sendgrid hosted email service
because the number of emails should not pass the free tier