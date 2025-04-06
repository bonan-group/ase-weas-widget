"""
Simple tests
"""


def test_import():
    """Test if the module can be imported"""
    import ase_weas_widget
    from ase_weas_widget.viewer import view_weas


def test_ase_registry():
    """Test viewing an structure"""
    from ase.build import bulk
    from ase.visualize import view
    atoms = bulk('Si', 'diamond', 5.4)
    view(atoms, viewer='weas')