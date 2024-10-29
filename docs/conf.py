# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

project = 'FAIR Wizard Integration SDK'
copyright = '2024, Codevence Solutions'
author = 'Codevence Solutions'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinxcontrib.autodoc_pydantic',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autodoc_pydantic_model_show_json = True
autodoc_pydantic_settings_show_json = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

html_title = 'FAIR Wizard Integration SDK'
html_favicon = '_static/favicon.ico'
html_theme_options = {
    'light_logo': 'logo/logo-light-mode.svg',
    'dark_logo': 'logo/logo-dark-mode.svg',
    'light_css_variables': {
        'color-brand-primary': '#019AD6',
        'color-brand-content': '#019AD6',
        'sidebar-item-spacing-horizontal': '.75rem',
    },
    'dark_css_variables': {
        'color-brand-primary': '#019AD6',
        'color-brand-content': '#019AD6',
        'sidebar-item-spacing-horizontal': '.75rem',
    },
}
