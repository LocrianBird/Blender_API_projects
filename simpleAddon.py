bl_info = {
"name": "Simple Add-on",
"author": "MaggieLee",
"location": "View3D > Tools > Simple Addon",
"version": (1, 0, 0),
"blender": (2, 93, 4),
"description": "Starting point for new add-ons.",
"wiki_url": "http://example.com",
"category": "Development"
}

import bpy


class SimpleOperator(bpy.types.Operator):
    bl_idname = "object.simple_operator"
    bl_label = "Print an Encouraging Message"
    
    def execute(self, context):
        print("\n\n####################################################")
        print("# Add-on and Simple Operator executed successfully!")
        print("# " + context.scene.encouraging_message)
        print("####################################################")
        return {'FINISHED'}
    
    @classmethod
    def register(cls):
        print("Registered class: %s " % cls.bl_label)
        
        #Register properties related to the class
        bpy.types.Scene.encouraging_message = bpy.props.StringProperty(
            name="",
            description="Message to print to user",
            default="Have a nice day!")
        
    @classmethod
    def unregister(cls):
         print("Unregistered class: %s " % cls.bl_label)
         
         #Delete parameters related to the class
         del bpy.types.Scene.encouraging_message

class SimplePanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "SimpleAddon"
    bl_label = "Call Simple Operator"
    bl_context = "objectmode"
    
    def draw(self, context):
        self.layout.operator("object.simple_operator",
            text="Print Encouraging Message")
        self.layout.prop(context.scene, 'encouraging_message')

    @classmethod
    def register(cls):
        print("Registered class: %s " % cls.bl_label)
        
    @classmethod
    def unregister(cls):
        print("Unregistered class: %s " % cls.bl_label)
    
def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(SimplePanel)
    print("%s registration complete\n" % bl_info.get('name'))
    
def unregister():
    bpy.utils.unregister_class(__name__)
    print("%s unregister complete\n" % bl_info.get('name'))
    

if __name__ == "__main__":
    try:
        unregister()
    except Exception as e:
        #Catch failure to unregister explicitly
        print(e)
        pass
    
    register()    
        