SAML
====

Interface
---------

For SAML automations, it is possible to define a custom function for handling the "User Logged In" event. This function will be called when the user logs in using SAML.

User Logged In
~~~~~~~~~~~~~~

You can implement your own *handle* function to handle the "User Logged In" event for SAML. By default the following function is used:

.. autofunction:: fair_wizard.automation.saml.handle_saml_user_logged_in

Your *handle* function must have the same signature, i.e. accept :py:class:`SamlUserLoggedInEvent` as the argument and return :py:type:`UserLoginResponse`.


Model
-----

.. automodule:: fair_wizard.automation.saml.model
    :members:


Helpers
-------

This module contains additional helper functions to use SAML models.

.. automodule:: fair_wizard.automation.saml.helpers
    :members:

