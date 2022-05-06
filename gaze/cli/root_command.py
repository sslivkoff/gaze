from __future__ import annotations

import toolcli
import tooltime

import gaze


def get_command_spec() -> toolcli.CommandSpec:
    return {
        'f': gaze_command,
        'args': [
            {'name': 'target', 'help': 'path to python script or .ipynb notebook'},
            {'name': '--every', 'help': 'rerun periodically'},
        ],
    }


def gaze_command(target, every):

    if every is None:
        pass

    else:
        pass

