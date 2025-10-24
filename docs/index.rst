MES Copilot API 문서
====================

FastAPI 기반 프로젝트의 API 문서입니다.

Routers
-------

패키지 전체를 재귀적으로 문서화합니다.

.. autosummary::
   :toctree: _autosummary
   :recursive:

   routers

빌드 방법 (Windows)
-------------------

다음 명령으로 문서를 빌드하고 열 수 있습니다::

   python -m sphinx -b html docs docs/_build/html
   start docs\\_build\\html\\index.html