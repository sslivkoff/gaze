from __future__ import annotations

import os

import jinja2

from . import notebook_utils


def get_template_path(name):
    gaze_dir = os.path.dirname(os.path.realpath(__file__))
    template_dir = os.path.join(gaze_dir, 'templates')
    template_path = os.path.join(template_dir, name + 'html')
    if not os.path.isfile(template_path):
        raise Exception('template does not exist')
    return template_path


def notebook_to_page(notebook, output_dir=None):

    if output_dir is None:
        output_dir = os.path.realpath('./.gaze')

    image_paths = notebook_utils.extract_notebook_images(
        notebook=notebook,
        output_dir=output_dir,
    )

    render_page(image_paths=image_paths)


def render_page(image_paths):
    print('rendering page with', len(image_paths), 'images')

    # template_path = get_template_path('base')

    env = jinja2.Environment(
        loader=jinja2.PackageLoader('gaze'),
        autoescape=jinja2.select_autoescape(),
    )
    template = env.get_template('figure_gallery.html')
    content = template.render()
    print(content)
