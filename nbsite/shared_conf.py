# -*- coding: utf-8 -*-

import os

from nbsite import nbbuild

def setup(app):
    try:
        from nbsite.paramdoc import param_formatter
        app.connect('autodoc-process-docstring', param_formatter)
    except ImportError:
        print('no param_formatter (no param?)')

    nbbuild.setup(app)

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.inheritance_diagram'
]

inheritance_graph_attrs = dict(rankdir="LR", size='"12.0, 12.0"', fontsize=18)

default_edge_attrs = {
    'arrowsize': 1.0,
    'style': '"setlinewidth(0.5)"',
}

source_suffix = '.rst'
master_doc = 'index'
pygments_style = 'sphinx'
exclude_patterns = ['_build']
html_static_path = [os.path.abspath(os.path.join(os.path.dirname(__file__),'_shared_static'))]

html_context = {
    'js_includes': ['nbsite.js', 'require.js'],
    'css_includes': ['nbsite.css'] 
}
