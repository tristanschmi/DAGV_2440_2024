import maya.cmds as cmds
import re

def create_controls_for_joints():
    # Get the selected joint objects
    selected_joints = cmds.ls(selection=True, type="joint")
    
    if not selected_joints:
        cmds.warning("No joints selected. Please select one or more joints.")
        return

    for joint in selected_joints:
        # Generate the control and group names
        base_name = re.sub(r'(_Jnt|_Geo)$', '', joint)  # Remove any suffix if present
        ctrl_name = f"{base_name}_Ctrl"
        grp_name = f"{ctrl_name}_Grp"

        # Create a NURBS circle as the control
        control = cmds.circle(name=ctrl_name, normal=(1, 0, 0), radius=1)[0]

        # Query the joint's transformation (translation and rotation)
        translation = cmds.xform(joint, query=True, worldSpace=True, translation=True)
        rotation = cmds.xform(joint, query=True, worldSpace=True, rotation=True)

        # Move and rotate the control to match the joint's transformation
        cmds.xform(control, worldSpace=True, translation=translation)
        cmds.xform(control, worldSpace=True, rotation=rotation)

        # Create a parent group for the control
        control_group = cmds.group(empty=True, name=grp_name)
        
        # Set the group’s transformation to match the joint
        cmds.xform(control_group, worldSpace=True, translation=translation)
        cmds.xform(control_group, worldSpace=True, rotation=rotation)

        # Parent the control under the group
        cmds.parent(control, control_group)

        # Freeze transformations on the control to zero them out
        cmds.makeIdentity(control, apply=True, translate=True, rotate=True, scale=True)

   

# Run the function to create controls for selected joints
create_controls_for_joints()



