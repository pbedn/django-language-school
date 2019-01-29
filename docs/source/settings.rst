Settings
************************
Notes on specific settings

Email server
===================

Integration with Sendgrid SMTP Relay. Use `setup guide <https://app.sendgrid.com/guide/integrate/langs/smtp>`_,
it will require to create api key
and give you values to update .env settings file

.. code-block:: bash

    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_HOST_USER = 'apikey'
    EMAIL_HOST_PASSWORD = '<long-api-token>'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
