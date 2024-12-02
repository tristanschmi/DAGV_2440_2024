import maya.cmds as cmds

def rename_selected_objects(name_template):
   
    # Get current selection
    selected_objects = cmds.ls(selection=True)

    # Determine the number of hash symbols for zero-padding
    hash_count = name_template.count('#')

    if not selected_objects:
        print("No objects selected.")
        return
    
    if hash_count > 0:
        # Partition the template around the first occurrence of '#'
        before_hash, _, after_hash = name_template.partition('#' * hash_count)

        for index, obj in enumerate(selected_objects):
            # Use zfill for padding zeros based on the count of '#'
            number_str = str(index + 1).zfill(hash_count)
            
            # Form the new name using replace and partition results
            new_name = before_hash + number_str + after_hash.replace('#' * hash_count, '', 1)
            
            # Rename the object in the Maya scene
            cmds.rename(obj, new_name)

# Example usage
if __name__ == "__main__":
    template = "Arm_##_Jnt"
    rename_selected_objects(template)

