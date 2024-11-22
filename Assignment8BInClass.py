import maya.cmds as cmds

def create_control():
    sels = cmds.ls(sl=True)
    
    for sel in sels:
        sel_position = cmds.xform(sel, q=True, ws=True, translation=True)
        sel_rotation = cmds.xform(sel, q=True, ws=True, rotation=True)

        new_ctrl = cmds.circle(center = (0,0,0), normal = (1,0,0), sweep = 360, radius = 1, d = 3, ut = False, tol = 0.01, s = 8, ch = True)[0]
        cmds.xform(new_ctrl, ws = True, translation = sel_position)
        cmds.xform(new_ctrl, ws = True, rotation = sel_rotation)

        new_group = cmds.group(empty = True, world = True)
        cmds.xform(new_group, ws = True, translation = sel_position)
        cmds.xform(new_group, ws = True, rotation = sel_rotation)

        cmds.parent(new_ctrl, new_group)

        name,temp_var, suffix = sel.rpartition('_')
        if suffix.lower() not in ['jnt', 'geo', 'grp']:
            name = sel

        new_ctrl = cmds.rename(new_ctrl, '%s_Ctrl' % name)
        new_group = cmds.rename(new_group, '%s_Grp' % new_ctrl)

        #sel.rpartition('_')
        #name = temp_list[0]
        #temp_var = temp_list[1]
        #suffix = temp_list[2]

create_control()