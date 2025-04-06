"""
This module registers the view provided in this package
"""
from ase.utils.plugins import ExternalViewer
VIEWER_ENTRYPOINT = ExternalViewer(
    desc="Visualization using weas-widget",
    module="ase_weas_widget.viewer"
)

