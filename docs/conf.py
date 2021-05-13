# -*- coding: utf-8 -*-
#
# Jira Python Client documentation build configuration file, created by
# sphinx-quickstart on Thu May  3 17:01:50 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys

import sphinx_rtd_theme

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath(".."))
from jira import __version__  # noqa

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = "2.2.0"

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode", "sphinx.ext.intersphinx"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.7", None),
    # until https://github.com/psf/requests/issues/5212 is addressed
    # "requests": ("http://docs.python-requests.org/en/latest/", None),
    "requests": ("https://requests.kennethreitz.org/en/master/", None),
    "requests-oauthlib": ("https://requests-oauthlib.readthedocs.io/en/latest/", None),
    "ipython": ("https://ipython.readthedocs.io/en/stable/", None),
    "pip": ("https://pip.readthedocs.io/en/stable/", None),
}

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}

nitpick_ignore = [
    ("py:class", "Any"),
    ("py:class", "Attachment"),
    ("py:class", "Board"),
    ("py:class", "BufferedReader"),
    ("py:class", "Component"),
    ("py:class", "CustomFieldOption"),
    ("py:class", "Customer"),
    ("py:class", "Dashboard"),
    ("py:class", "Dict"),
    ("py:class", "Filter"),
    ("py:class", "Issue._IssueFields"),
    ("py:class", "IssueLinkType"),
    ("py:class", "IssueType"),
    ("py:class", "Iterable"),
    ("py:class", "List"),
    ("py:class", "NoReturn"),
    ("py:class", "Optional"),
    ("py:class", "Project"),
    ("py:class", "Resolution"),
    ("py:class", "Resource"),
    ("py:class", "Response"),
    ("py:class", "ResultList"),
    ("py:class", "ServiceDesk"),
    ("py:class", "Sprint"),
    ("py:class", "Status"),
    ("py:class", "StatusCategory"),
    ("py:class", "Tuple"),
    ("py:class", "Union"),
    ("py:class", "User"),
    ("py:class", "Version"),
    ("py:class", "Votes"),
    ("py:class", "diy"),
    ("py:class", "integer"),
    ("py:class", "jira.client.ResultList"),
    ("py:class", "jira.resources.Resource"),
    ("py:class", "jira.resources.Sprint"),
    ("py:class", "jira.resources.Watchers"),
    ("py:class", "kanban"),
    ("py:class", "project"),
    ("py:class", "scrum"),
    ("py:class", "user"),
    ("py:meth", "Resource.delete"),
    ("py:meth", "Resource.update"),
    ("py:mod", "filemagic"),
    ("py:mod", "ipython"),
    ("py:mod", "pip"),
    ("py:mod", "requests-kerberos"),
    ("py:mod", "requests-oauthlib"),
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = u"jira-python"
copyright = u"2012, Atlassian Pty Ltd."

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = __version__
# The full version, including alpha/beta/rc tags.
release = __version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
today = "1"
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = "%b %d, %Y"

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
html_use_opensearch = ""

# This is the file name suffix for HTML files (e.g. ".xhtml").
html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = "jirapythondoc"


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {"papersize": "a4paper", "pointsize": "10pt"}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    (
        "index",
        "jirapython.tex",
        u"jira-python Documentation",
        u"Atlassian Pty Ltd.",
        "manual",
    )
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ("index", "jirapython", u"jira-python Documentation", [u"Atlassian Pty Ltd."], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "jirapython",
        u"jira-python Documentation",
        u"Atlassian Pty Ltd.",
        "jirapython",
        "One line description of project.",
        "Miscellaneous",
    )
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'
