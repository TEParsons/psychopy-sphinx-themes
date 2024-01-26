"""Sphinx psychopy themes."""
from pathlib import Path

def setup(app):
    """Setup the PsychoPy sphinx themes."""
    # add_html_theme is new in Sphinx 1.6+
    if hasattr(app, 'add_html_theme'):
        # add psychopy core theme
        app.add_html_theme('psychopy', (Path(__file__).parent / 'psychopy').absolute())
        # add psychopy plugin theme
        app.add_html_theme('psychopy_plugin', (Path(__file__).parent / 'psychopy_plugin').absolute())
