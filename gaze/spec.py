from __future__ import annotations

import typing

from typing_extensions import TypedDict


class Notebook(TypedDict):
    cells: typing.Sequence[NotebookCell]
    metadata: typing.Mapping[str, typing.Any]
    nbformat: int
    nbformat_minor: int


class NotebookCell(TypedDict, total=False):
    cell_type: str
    execution_count: int
    id: str
    metadata: typing.Mapping
    outputs: typing.Sequence[NotebookCellOutput]
    source: typing.Sequence[str]


class NotebookCellOutput(TypedDict):
    name: str
    output_type: str
    text: str
    data: typing.Mapping[str, typing.Any]
    metadata: typing.Any
    execution_count: int

