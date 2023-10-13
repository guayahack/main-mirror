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
    "sphinx_sitemap",
    "sphinxext.rediraffe",
    "sphinxext.opengraph",
    "sphinx.ext.intersphinx",
    # "sphinx.ext.autosectionlabel", #not needed, we use myst_parser's implicit anchors
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**/template*"]

language = "es"
# sitemap_locales = ['en', 'es', 'de']
sitemap_locales = [None]
sitemap_url_scheme = "{link}"
# locale_dirs = ['en', 'es', 'de']

suppress_warnings = [
    "myst.domains",
    "myst.strikethrough",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_baseurl = "https://guayahack.co/"  # el backslash al final es muy importante! sphinx-sitemap genera links dañado
html_title = "HackerSpace y Grupo de estudio"
html_logo = "_static/logo.png"
html_favicon = "_static/favicon.png"
html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_extra_path = ["extra"]


html_theme_options = {
    #    "": "",
    "announcement": "Las últimas noticias y cambios en GuayaHack los encuentran en #Noticias 🔔",
    "analytics": {"google_analytics_id": "G-2VR9YCCEEM"},
    "icon_links": [
        #        {
        #            "name": "LinkedIn",
        #            "url": "https://linkedin.com/in/guayahack",
        #            "icon": "fa-brands fa-linkedin",
        #        },
        {
            "name": "GitLab",
            "url": "https://gitlab.com/guayahack",
            "icon": "fa-brands fa-gitlab",
        },
        {
            "name": "Mastodon",
            "url": "https://mastodon.social/@guayahack",
            "icon": "fa-brands fa-mastodon",
            "attributes": {"rel": "me"},
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/guayahack",
            "icon": "fa-brands fa-twitter",
        },
        {
            "name": "Facebook",
            "url": "https://facebook.com/guayahack",
            "icon": "fa-brands fa-facebook",
        },
        {
            "name": "Instagram",
            "url": "https://instagram.com/guayahack",
            "icon": "fa-brands fa-instagram",
        },
        {
            "name": "YouTube",
            "url": "https://youtube.com/@guayahack",
            "icon": "fa-brands fa-youtube",
        },
        {
            "name": "Twitch",
            "url": "https://twitch.com/guayahack",
            "icon": "fa-brands fa-twitch",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/guayahack",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Flickr",
            "url": "https://flickr.com/photos/guayahack",
            "icon": "fa-brands fa-flickr",
        },
        #        {
        #            "name": "TikTok",
        #            "url": "https://tiktok.com/@guayahack",
        #            "icon": "fa-brands fa-tiktok",
        #        },
        {
            "name": "Blog RSS feed",
            "url": "https://guayahack.co/blog/atom.xml",
            "icon": "fa-solid fa-rss",
        },
        {
            "name": "E-mail",
            "url": "mailto:info@guayahack.co",
            "icon": "fa-solid fa-envelope",
        },
        {
            "name": "SoundCloud",
            "url": "https://soundcloud.com/guayahack",
            "icon": "fa-brands fa-soundcloud",
        },
        {
            "name": "Spotify",
            "url": "https://open.spotify.com/show/3kOyt5SllRStz6uSuoX3HZ",
            "icon": "fa-brands fa-spotify",
        },
    ],
}

html_context = {"default_mode": "dark"}

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

blog_baseurl = "https://guayahack.co/"
blog_feed_archives = True
blog_path = "posts"
blog_title = "GuayaHack"
blog_feed_subtitle = "@main"
blog_feed_fulltext = False
# blog_post_pattern = "blog/*/*"
# post_redirect_refresh = 1
# post_auto_image = 0
# post_auto_excerpt = 0

blog_default_author = "GuayaHack"
blog_authors = {
    "GuayaHack": ("GuayaHack", "https://guayahack.co"),
}

# https://myst-parser.readthedocs.io/en/latest/syntax/cross-referencing.html#implicit-targets
myst_heading_anchors = 6

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

myst_substitutions = {
    "bulletlocco": '<span style="font-size:  1.8em;">🇨🇴</span>',
    "bulletlangen": '<span style="font-size: 1.8em;">🇬🇧</span>',
    "bulletlanges": '<span style="font-size: 1.8em;">🇪🇸</span>',
    "bulletpack": '<span style="font-size: 2em;">📦</span>',
    "bulletinfo": '<span style="font-size: 1.5em;">ℹ️</span>',
    "bulletcheck": '<span style="font-size:1.5em;">✅</span>',
    "bulletfail": '<span style="font-size: 2em;">⛔</span>',
    "bulletwarn": '<span style="font-size: 1.6em;">⚠️</span>',
    "bulletstar": '<span style="font-size: 2em;">⭐️</span>',
    "bulletkeys": '<span style="font-size: 1.5em;">⬅️➡️</span>',
}

autosectionlabel_prefix_document = True

###############################################################################
# extension sphinxext.rediraffe
###############################################################################

rediraffe_branch = "master"
rediraffe_redirects = "rediraffe_redirects.txt"

###############################################################################
# extension sphinxext.opengraph
###############################################################################

ogp_site_url = "https://guayahack.co"
ogp_site_name = "GuayaHack — HackerSpace y grupo de estudio"
ogp_image = "_static/logo-black.png"
ogp_use_first_image = True
ogp_description_length = 50
ogp_enable_meta_description = True
ogp_custom_meta_tags = []
ogp_social_cards = {
    "image": "_static/logo-black.png",
}
