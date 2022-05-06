from __future__ import annotations

import base64
import json
import os
import typing

from . import spec


def load_ipynb(path: str) -> spec.Notebook:
    with open(path, 'r') as f:
        content = json.load(f)
    return typing.cast(spec.Notebook, content)


def extract_notebook_images(
    path_or_content: str | spec.Notebook,
    output_dir: str | None = None,
    verbose: bool = True,
) -> None:

    # load notebook
    if isinstance(path_or_content, str):
        path = path_or_content
        content = load_ipynb(path=path)
    elif isinstance(path_or_content, dict):
        content = path_or_content

    # extract images
    for c, cell in enumerate(content['cells']):
        extract_cell_images(
            cell=cell,
            cell_index=c,
            output_dir=output_dir,
            verbose=verbose,
        )


def extract_cell_images(
    cell: spec.NotebookCell,
    cell_index: int | None = None,
    output_dir: str | None = None,
    filename: str | None = None,
    verbose: bool = True,
) -> None:

    if output_dir is None:
        output_dir = './'

    for output_index, output in enumerate(cell.get('outputs', [])):

        execution_count = cell.get('execution_count', '-')

        # compute filename
        if filename is None:
            if cell_index is None:
                filename_tokens = []
            else:
                filename_tokens = [str(cell_index)]
            filename_tokens.append(str(execution_count))
            filename_tokens.append(str(output_index))
            filename = '__'.join(filename_tokens)

        for datatype, data in output.get('data', {}).items():

            if datatype == 'image/png':

                # save png images

                path = os.path.join(output_dir, filename + '.png')
                bytes_data = base64.b64decode(data)

                if verbose:
                    print('saving', path)
                with open(path, 'wb') as f:
                    f.write(bytes_data)

            elif datatype == 'image/svg+xml':

                # save svg images

                path = os.path.join(output_dir, filename + '.svg')
                plaintext_data = ''.join(data)

                if verbose:
                    print('saving', path)
                with open(path, 'w') as f:
                    f.write(plaintext_data)

            else:

                # ignore other output types

                pass

