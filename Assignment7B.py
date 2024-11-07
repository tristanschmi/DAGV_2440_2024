import maya.cmds as cmds

def create_parent_group():
    # Get the currently selected objects
    selected_objects = cmds.ls(selection=True)

    # Loop through each selected object
    for obj in selected_objects:
        # Query the translation and rotation values of the selected object
        translation = cmds.xform(obj, query=True, worldSpace=True, translation=True)
        rotation = cmds.xform(obj, query=True, worldSpace=True, rotation=True)
        
        # Create a new group at the origin
        group_name = obj + "_Grp"
        new_group = cmds.group(empty=True, name=group_name)
        
        # Set the new group's translation and rotation to match the selected object
        cmds.xform(new_group, worldSpace=True, translation=translation)
        cmds.xform(new_group, worldSpace=True, rotation=rotation)
        
        # Parent the selected object under the new group
        cmds.parent(obj, new_group)
        
        # Freeze transformations on the selected object to zero out transformations
        cmds.makeIdentity(obj, apply=True, translate=True, rotate=True, scale=True)

    print("Parent groups created and objects parented successfully.")

# Run the function to create the groups and parent selected objects
create_parent_group()
