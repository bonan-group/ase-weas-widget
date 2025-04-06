"""
Module for using weas_widget as an option to ase.visalize.view
"""

from weas_widget import WeasWidget

def view_weas(atoms, **kwargs):
    """View with weas-widget"""
    viewer = WeasWidget()
    viewer.from_ase(atoms)
    if 'callback' in kwargs:
        kwargs['callback'](viewer)
    return viewer