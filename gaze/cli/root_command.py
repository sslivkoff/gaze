from __future__ import annotations

import time

import toolcli
import tooltime

import gaze


def get_command_spec() -> toolcli.CommandSpec:
    return {
        'f': gaze_command,
        'args': [
            {'name': 'target', 'help': 'path to python script or jupyter notebook'},
            {'name': '--every', 'help': 'rerun periodically'},
        ],
    }


def gaze_command(target, every):

    if every is not None:

        print('running every', every, 'seconds')
        last = time.time()
        while True:
            gaze.notebook_to_page(target)
            now = time.time()
            if now < last + every:
                time.sleep()
            last = now

    else:
        gaze.notebook_to_page(target)

