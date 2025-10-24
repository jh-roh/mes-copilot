import os
import sys

# 프로젝트 루트를 sys.path에 추가
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
project = 'MES Copilot'
author = 'MES Team'
release = '0.1.0'
language = 'ko'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output -------------------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Autodoc / Autosummary options ------------------------------------------
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'undoc-members': True,
    'show-inheritance': True,
}
autosummary_generate = True
autosummary_imported_members = True

# 타입 힌트 렌더링
typehints_fully_qualified = False
always_document_param_types = True
typehints_document_rtype = True