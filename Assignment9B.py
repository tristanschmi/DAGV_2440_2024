import maya.cmds as cmds

def set_override_color(color):
    """
    Changes the override color of the shape node(s) of the selected object(s) in Maya.
    
    :param color: An integer (0-31) or a string representing the color name.
    """

    # Dictionary mapping color names to their respective index values
    color_map = {
        'light gray': 0,
        'black': 1,
        'dark gray': 2,
        'ash gray': 3,
        'crimson': 4,
        'dark blue': 5,
        'blue': 6,
        'dark green': 7,
        'purple': 8,
        'pink': 9,
        'orange': 10,
        'brown': 11,
        'dark red': 12,
        'red': 13,
        'green': 14,
        'navy': 15,
        'white': 16,
        'yellow': 17,
        'sky blue': 18,
        'lime green': 19,
        'light pink': 20,
        'light orange': 21,
        'light yellow': 22,
        'grass green': 23,
        'flesh': 24,
        'gold': 25,
        'neon green': 26,
        'turquoise': 27,
        'aquamarine': 28,
        'ocean blue': 29,
        'magenta': 30,
        'dark pink': 31,

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


set_override_color('red')

# Or using a specific numeric value:
# set_override_color(13)
