from __future__ import annotations

import os

from gaze import notebook_utils


def get_command_spec():
    return {
        'f': extract_command,
        'help': 'extract images from notebook',
        'args': [
            {'name': 'notebook', 'help': 'path to notebook'},
            {'name': '--output-dir', 'help': 'path to output dir'},
        ]
    }


def extract_command(notebook, output_dir, verbose=True):

    # get output path
    if output_dir is None:
        output_dir = '.'
    output_dir = os.path.realpath(output_dir)
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    # extract images
    notebook_utils.extract_notebook_images(
        notebook,
        output_dir=output_dir,
        verbose=verbose,
    )
