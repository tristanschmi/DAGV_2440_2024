import maya.cmds as cmds

class SequentialRenamerUI:
    def __init__(self):
        self.window = "sequentialRenamerWindow"
        self.text_field = None

    def create(self):
        # Check if the window already exists; if so, delete it.
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window)

        # Create a new window
        self.window = cmds.window(self.window, title="Sequential Renamer", widthHeight=(300, 100))

        # Create a layout for window contents
        cmds.columnLayout(adjustableColumn=True)
        
        # Create a text field for user input
        self.text_field = cmds.textField(placeholderText="Enter template, e.g., 'L_Leg_##_Ctrl'")
        
        # Create a button that triggers renaming process
        cmds.button(label="Rename Selected Objects", command=self.rename_objects)

        # Show the window
        cmds.showWindow(self.window)

    def rename_objects(self, *args):
        # Get the text from the text field
        name_template = cmds.textField(self.text_field, query=True, text=True)
        
        # Call the rename function
        rename_selected_objects(name_template)

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

# Example: Creating an instance of the UI
renamer_ui = SequentialRenamerUI()
renamer_ui.create()
