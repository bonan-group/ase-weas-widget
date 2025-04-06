"""
Module for using weas_widget as an option to ase.visalize.view
"""

from weas_widget import WeasWidget

def preset_vesta(viewer):
    """
    modifier for display in a VESTA style
    1. Include bonded atoms
    2. Show atoms beyond the boundary
    3. Show polyhedra
    """
    viewer.avr.model_style = 2
    viewer.avr.boundary = [[-0.1, 1.1], [-0.1, 1.1], [-0.1, 1.1]]
    viewer.avr.show_bonded_atoms = True
    viewer.avr.color_type = "VESTA"

def preset_legend(viewer):
    viewer.avr.show_atom_legend = True

def preset_ball(viewer):
    viewer.avr.model_style = 0 

def preset_ball_stack(viewer):
    viewer.avr.model_style = 1 

def preset_polyhedra(viewer):
    viewer.avr.model_style = 2 

def preset_vesta_color(viewer):
    viewer.avr.color_type = "VESTA"

def preset_cp2k_color(viewer):
    viewer.avr.color_type = "CPK"

def preset_jmol_color(viewer):
    viewer.avr.color_type = "JMOL"


PRESETS = {
    'vesta': preset_vesta,
    'legend': preset_legend,
    'ball': preset_ball,
    'ball+stick': preset_ball_stack,
    'polyhedra': preset_polyhedra,
    'cp2k_color': preset_cp2k_color,
    'vesta_color': preset_vesta_color,
    'jmol_color': preset_jmol_color,
}

def view_weas(atoms, **kwargs):
    """View with weas-widget"""
    viewer_kwargs = kwargs.get('viewer_kwargs', {})
    viewer = WeasWidget(**viewer_kwargs)
    viewer.from_ase(atoms)

    # Apply modifier function
    if 'presets' in kwargs:
        presets = kwargs['presets']
        if isinstance(presets, str):
            if ',' in presets:
                presets = presets.split(',')
            else:
                presets = [presets]
        for preset in presets:
            func = PRESETS.get(preset)
            if func is not None:
                func(viewer)
            else:
                raise ValueError(f'Unknown modifier name {preset}')

    # Apply callback modifiers
    callback = kwargs.get('mods')
    if callback is not None:
        if not isinstance(callback, (tuple, list)):
            callback = [callback]
        for func in callback:
            func(viewer)
    return viewer