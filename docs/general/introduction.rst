Introduction
============

This **FAIR Wizard Integration SDK** is a Python library that provides a set of tools for integrating with the FAIR Wizard platform. The SDK is designed to be used in Python applications that need to interact with the FAIR Wizard platform programmatically.

Currently, the SDK provides the following features:

* **Automation API**: automated workflows for user authentication and authorization via :doc:`OpenID </api/automation/openid>` and :doc:`SAML </api/automation/saml>`.

Automations
-----------

You can read more about setting Automations within the FAIR Wizard Guide.

This SDK serves for reference how to implement the automations in Python, what is expected, and how to test them. Keep in mind, that while you just need to comply with described interface (typically, supply a function based on a specification), you can add any additional logic you need including more functions, classes, variables, and so on. It is possible to use Python standard library only. Any code violating the FAIR Wizard platform policies may be removed.

Compatibility Matrix
--------------------

+------------------------------+----------------------+
| FAIR Wizard Integration SDK  | FAIR Wizard          |
+==============================+======================+
| 0.1.0                        | 4.12.0 (and higher)  |
+------------------------------+----------------------+
