Architecture choices
************************
Notes on technology choices.

Backend framework
===================
Django

Frontend framework
===================
Bootstrap 4

Continuous Integration
===================
CircleCI

Continuous Delivery
===================
CircleCI with bash script

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