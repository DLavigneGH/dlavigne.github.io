from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QWidget


def clear_layout(layout):
    """Clear widgets from a layout."""
    if layout:
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()


def create_container_widget():
    """Create a container widget with top-aligned vertical layout"""
    container_widget = QWidget()
    container_layout = QVBoxLayout(container_widget)
    container_layout.setAlignment(Qt.AlignTop)
    return container_widget, container_layout
