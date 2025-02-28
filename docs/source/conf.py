# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'STIMP'
copyright = "2025, Fan Zhang"
author = 'Fan Zhang'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

html_static_path = ["_static"]

def setup(app):
    app.add_css_file("my_theme.css")

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
# html_theme = 'piccolo_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
bibtex_bibfiles = ["refs.bib"]
bibtex_bibliography_header = ".. rubric:: References"
