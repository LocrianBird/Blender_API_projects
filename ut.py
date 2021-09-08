import bpy

#Selecting objects by name
def select(objName):
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[objName].select_set(True)
    
#Activating objects by name
def activate(objName):
    bpy.context.view_layer.objects.active = bpy.data.objects[objName]
    

class Sel:
    """Function Class for operating on SELECTED objects"""
    
    #Differential
    def translate(v):
        bpy.ops.transform.translate(value=v, constraint_axis=(True, True, True))
    
    def scale(v):
        bpy.ops.transform.resize(value=v, constraint_axis=(True, True, True))
        
    def rotate_x(v):
        bpy.ops.transform.rotate(value=v, orient_axis='X')
        
    def rotate_y(v):
        bpy.ops.transform.rotate(value=v, orient_axis='Y')
        
    def rotate_z(v):
        bpy.ops.transform.rotate(value=v, orient_axis='Z')
    
    
class Act:
    """Functio Class for operating on ACTIVE objects"""
    
    #Declarative
    def location(v):
        bpy.context.object.location = v
    
    def scale(v):
        bpy.context.object.scale = v
        
    def rotation(v):
        bpy.context.object.rotation_euler = v
    
    def rename(objName):
        bpy.context.object.name = objName
        
        
class Spec:
    """Function Class for operating on SPECIFIED objects"""
    
    #Declarative
    def scale(objName, v):
        bpy.data.objects[objName].scale = v

    def location(objName, v):
        bpy.data.objects[objName].location = v
    
    def rotation(objName, v):
        bpy.data.objects[objName].rotation_euler = v
        

class Create:
    """Function Class for CREATING objects"""
    
    def cube(objName):
        bpy.ops.mesh.primitive_cube_add(size=0.5, location=(0,0,0))
        Act.rename(objName)
        
    def sphere(objName):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5, location=(0,0,0))
        Act.rename(objName)
        
    def cone(objName):
        bpy.ops.mesh.primitive_cone_add(radius1=0.5, location=(0,0,0))
        Act.rename(objName)
        

#Delete an object by name
def delete(objName):
    select(objName)
    bpy.ops.object.delete(use_global=False)
        
#Delete all objects
def delete_all():
    if (len(bpy.data.objects) != 0):
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.delete(use_global=False)
        
#Function for entering Edit Mode with no vertices selected (or Object Mode)
def mode(mode_name):
    bpy.ops.object.mode_set(mode=mode_name)
    if mode_name == 'EDIT':
        bpy.ops.mesh.select_all(action='DESELECT')


        
if __name__ == "__main__":
    
    #Create a cube
    Create.cube('PerfectCube')
    
    Sel.translate((0,1,2))
    Sel.scale((1,1,2))
    Sel.scale((0.5,1,1))
    
    Sel.rotate_x(3.1415/8)
    Sel.rotate_x(3.1415/7)
    
    Sel.rotate_z(3.1415/3)
    
    #Create a cone
    Create.cone('PointyCone')
    
    Act.location((-2,-2,0))
    Spec.scale('PointyCone', (1.5,2.5,2))
    
    #Create a sphere
    Create.sphere('SmoothSphere')
    
    Spec.location('SmoothSphere', (2,0,0))
    Act.rotation((0,0,3.1415/3))
    Act.scale((1,3,1))
    