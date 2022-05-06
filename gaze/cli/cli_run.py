from __future__ import annotations

import typing

import toolcli

import gaze


config = {
    'base_command': 'gaze',
    'description': 'create dashboards',
    'version': gaze.__version__,
    'include_debug_arg': True,
}

command_index = {
    (): 'gaze.cli.root_command',
    ('extract',): 'gaze.cli.subcommands.extract_command',
}


def run_cli(raw_command: str | None = None, **toolcli_kwargs: typing.Any):
    toolcli_kwargs = dict({'config': config}, **toolcli_kwargs)
    toolcli.run_cli(
        raw_command=raw_command,
        command_index=command_index,
        **toolcli_kwargs,
    )

