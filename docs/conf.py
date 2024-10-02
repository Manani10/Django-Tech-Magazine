import os
import sys
import django

# Add the path to the project (adjust if necessary)
sys.path.insert(0, os.path.abspath('..'))

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'tech_magazine.settings'
django.setup()

# -- Project information ------------------------------------------------------
project = 'tech'
copyright = '2024, sinethemba'
author = 'sinethemba'
release = '00.00.01'

# -- General configuration ---------------------------------------------------
# Enable extensions for autodoc and viewcode
extensions = [
    'sphinx.ext.autodoc',  # Automatically include docstrings
    'sphinx.ext.viewcode',  # Link to source code
]

# Template and pattern exclusions
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# Set the HTML theme for the documentation
html_theme = 'sphinx_rtd_theme'

# Path for static files (images, custom CSS)
html_static_path = ['_static']
