import maya.cmds as cmds

def set_override_color(color):
    """
    Changes the override color of the shape node(s) of the selected object(s) in Maya.
    
    :param color: An integer (0-31) or a string representing the color name.
    """

    # Dictionary mapping color names to their respective index values
    color_map = {
        'light gray': 1,
        'black': 2,
        'dark gray': 3,
        'ash gray': 4,
        'crimson': 5,
        'dark blue': 6,
        'blue': 7,
        'dark green': 8,
        'purple': 9,
        'pink': 10,
        'orange': 11,
        'brown': 12,
        'dark red': 13,
        'red': 14,
        'green': 15,
        'navy': 16,
        'white': 17,
        'yellow': 18,
        'sky blue': 19,
        'lime green': 20,
        'light pink': 21,
        'light orange': 22,
        'light yellow': 23,
        'grass green': 24,
        'flesh': 25,
        'gold': 26,
        'neon green': 27,
        'turquoise': 28,
        'aquamarine': 29,
        'ocean blue': 30,
        'magenta': 31,
        'dark pink':32,

        # Add other color mappings as needed
    }

    # Convert string color to its respective integer value if necessary
    if isinstance(color, str):
        color = color_map.get(color.lower())
        if color is None:
            raise ValueError("Invalid color name. Please provide a valid color name or an integer between 0 and 31.")
    
    # Ensure color is within valid range
    if not (0 <= color <= 31):
        raise ValueError("Color value must be an integer between 0 and 31.")
    
    # Get selected objects
    selection = cmds.ls(selection=True)

    if not selection:
        print("No objects selected.")
        return

    for obj in selection:
        # List all shape nodes for each transform
        shape_nodes = cmds.listRelatives(obj, shapes=True, fullPath=True) or []

        for shape in shape_nodes:
            # Enable override settings
            cmds.setAttr(f"{shape}.overrideEnabled", True)
            cmds.setAttr(f"{shape}.overrideColor", color)

# Example usage: Change the override color to red
set_override_color('green')

# Or using a specific numeric value:
# set_override_color(13)
