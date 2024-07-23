# generated by datamodel-codegen:
#   filename:  modular.yaml
#   timestamp: 1985-10-26T08:21:00+00:00

from __future__ import annotations

from typing import List, NotRequired, TypedDict

from .. import Id, Optional


class Tea(TypedDict):
    flavour: NotRequired[str]
    id: NotRequired[Id]
    self: NotRequired[Tea]
    optional: NotRequired[List[Optional]]


class TeaClone(TypedDict):
    flavour: NotRequired[str]
    id: NotRequired[Id]
    self: NotRequired[Tea]
    optional: NotRequired[List[Optional]]


ListModel = List[Tea]