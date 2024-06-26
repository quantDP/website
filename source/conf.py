# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'quantDP'
copyright = '2024, quantDP'
author = 'quantDP'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "notfound.extension",
    "sphinx_inline_tabs",
    "myst_parser",
    "sphinxext.opengraph",
    "sphinx_copybutton",
    "sphinx_design",
]

html_favicon = 'favicon.ico'

myst_enable_extensions = [
    "attrs_inline",
]

notfound_urls_prefix = None

notfound_context = {
    'title': 'Page not found',
    'body': "<h1>Page not found</h1>\n\nUnfortunately, we couldn't find the content you were looking for.",
}

html_extra_path = ["public"]

templates_path = ['_templates']
exclude_patterns = []

html_title = "quantDP"

html_theme_options = {
    # "announcement": "[put donation pitch here]",
    "footer_icons": [
        {
            "name": "X",
            "url": "https://twitter.com/quantDP_data",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 300 300.251" style="padding-left: 4px; padding-right: 4px;">
                    <path xmlns="http://www.w3.org/2000/svg" d="M178.57 127.15 290.27 0h-26.46l-97.03 110.38L89.34 0H0l117.13 166.93L0 300.25h26.46l102.4-116.59 81.8 116.59h89.34M36.01 19.54H76.66l187.13 262.13h-40.66"/>
                </svg>
            """,
            "class": "",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/quantDP",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16" style="padding-left: 4px; padding-right: 4px;">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
    "source_repository": "https://github.com/quantDP/website/",
    "source_branch": "master",
    "source_directory": "source/",
    "light_logo": "images/logo.svg",
    "dark_logo": "images/logo-white.svg",
    "sidebar_hide_name": True,
}

myst_html_meta = {
    "keywords": "Free, Market, Data, Stock, API, Historical, JSON",
    "property=og:locale": "en_US"
}

language = "en"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]