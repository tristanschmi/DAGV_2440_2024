import maya.cmds as cmds

class AssignColorUI:
    def __init__(self):
        self.window = "assignColorWindow"

    def create(self):
        # Check if the window already exists; if so, delete it.
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window)

        # Create a new window
        self.window = cmds.window(self.window, title="Assign Color", widthHeight=(1000, 1000))
        # Define color mapping
        self.color_map = {
            'light gray': (0.75, 0.75, 0.75),
            'black': (0, 0, 0),
            'dark gray': (0.3, 0.3, 0.3),
            'ash gray': (0.6, 0.6, 0.6),
            'crimson': (0.5, 0, 0),
            'dark blue': (0, 0, 0.5),
            'blue': (0, 0, 1),
            'dark green': (0, 0.5, 0),
            'purple': (0.5, 0, 0.5),
            'pink': (1, 0.75, 0.8),
            'orange': (1, 0.4, 0),
            'brown': (0.4, 0.2, 0),
            'dark red': (0.5, 0, 0),
            'red': (1, 0, 0),
            'green': (0, 1, 0),
            'navy': (0, 0, 0.25),
            'white': (1, 1, 1),
            'yellow': (1, 1, 0),
            'sky blue': (0.5, 0.8, 1),
            'lime green': (0.75, 1, 0),
            'light pink': (1, 0.5, 0.5),
            'light orange': (1, 0.65, 0.3),
            'light yellow': (1, 1, 0.5),
            'grass green': (0.5, 1, 0.5),
            'flesh': (1, 0.8, 0.7),
            'gold': (1, 0.85, 0.45),
            'neon green': (0.5, 1, 0),
            'turquoise': (0.3, 0.9, 0.9),
            'aquamarine': (0.5, 1, 0.83),
            'ocean blue': (0.3, 0.6, 1),
            'magenta': (1, 0, 0.5),
            'dark pink': (0.8, 0.4, 0.6)
        }

        # Create a layout for window contents
        cmds.columnLayout(adjustableColumn=True)

        # Create buttons for each color
        for color_name, rgb_value in self.color_map.items():
            cmds.button(label=color_name.capitalize(), backgroundColor=rgb_value, command=lambda x, col=color_name: self.set_color(col))

        # Show the window
        cmds.showWindow(self.window)

    def set_color(self, color_name):
        print(f"Setting color: {color_name}")
        set_override_color(color_name)

def set_override_color(color):
    color_map = {
        'light gray': 0, 'black': 1, 'dark gray': 2, 'ash gray': 3, 'crimson': 4, 'dark blue': 5,
        'blue': 6, 'dark green': 7, 'purple': 8, 'pink': 9, 'orange': 10, 'brown': 11, 'dark red': 12,
        'red': 13, 'green': 14, 'navy': 15, 'white': 16, 'yellow': 17, 'sky blue': 18, 'lime green': 19,
        'light pink': 20, 'light orange': 21, 'light yellow': 22, 'grass green': 23, 'flesh': 24,
        'gold': 25, 'neon green': 26, 'turquoise': 27, 'aquamarine': 28, 'ocean blue': 29, 'magenta': 30,
        'dark pink': 31
    }

    if isinstance(color, str):
        color = color_map.get(color.lower())
        if color is None:
            raise ValueError("Invalid color name. Please provide a valid color name or an integer between 0 and 31.")

    if not (0 <= color <= 31):
        raise ValueError("Color value must be an integer between 0 and 31.")

    selection = cmds.ls(selection=True)
    if not selection:
        print("No objects selected.")
        return

    for obj in selection:
        shape_nodes = cmds.listRelatives(obj, shapes=True, fullPath=True) or []
        for shape in shape_nodes:
            cmds.setAttr(f"{shape}.overrideEnabled", True)
            cmds.setAttr(f"{shape}.overrideColor", color)

# Example: Creating an instance of the UI
color_ui = AssignColorUI()
color_ui.create()
