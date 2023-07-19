# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "GuayaHack"
copyright = "2023, Jayson Salazar Rodriguez"
author = "La comunidad GuayaHack"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "ablog",
    "sphinx_togglebutton",
    "sphinx_copybutton",
    "myst_parser",
    "sphinx_design",
    "sphinxext.rediraffe",
    "sphinxext.opengraph",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**/template*"]

language = "es"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "main@GuayaHack"
html_logo = "_static/logo.png"
html_favicon = "_static/logo.png"
html_theme = "sphinx_book_theme"
html_static_path = ["_static"]

html_theme_options = {
    #    "": "",
    "announcement": "Las últimas noticias y cambios en GuayaHack los encuentran en # #Noticias 🔔",

}

html_context = {"default_mode": "dark"}

html_sidebars = {
    "**": [
        "navbar-logo.html",
        "sbt-sidebar-nav.html",
        "search-field.html",
    ]
}

html_css_files = ["custom.css"]

html_sidebars = {
    "**": [
        "navbar-logo.html",
        # "newsletter.html",
        "icon-links.html",
        "sbt-sidebar-nav.html",
        "ablog/postcard.html",
        "search-field.html",
        "ablog/categories.html",
        "ablog/tagcloud.html",
        "ablog/archives.html",
    ],
}


###############################################################################
# ablog
###############################################################################

blog_baseurl = "https://guayahack.co"
blog_feed_archives = True
blog_path = "posts"
blog_title = "GuayaHack"
blog_baseurl = "https://guayahack.co"
blog_feed_subtitle = "@main"
blog_feed_fulltext = False
# blog_post_pattern = "blog/*/*"
# post_redirect_refresh = 1
# post_auto_image = 0
# post_auto_excerpt = 0


myst_enable_extensions = [
    "amsmath",
    #    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

autosectionlabel_prefix_document = True


