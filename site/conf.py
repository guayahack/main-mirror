# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "GuayaHack"
copyright = "2023, Jayson Salazar Rodriguez"
author = "Jayson Salazar Rodriguez"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_togglebutton",
    "sphinx_copybutton",
    "myst_nb",
    "sphinx_design",
    "sphinxext.rediraffe",
    "sphinxext.opengraph",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "es"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ["_static"]
html_theme_options = {
    "": "",
}
