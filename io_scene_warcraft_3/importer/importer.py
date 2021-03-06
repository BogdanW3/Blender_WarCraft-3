from io_scene_warcraft_3.importer.create_armature_actions import create_armature_actions
from io_scene_warcraft_3.importer.create_armature_object import create_armature_object
from io_scene_warcraft_3.importer.create_mesh_objects import create_mesh_objects
from io_scene_warcraft_3.importer.create_material import create_material
from io_scene_warcraft_3.importer.create_object_actions import create_object_actions


def load_warcraft_3_model(model, importProperties):

    bpyMaterials = create_material(model, importProperties.set_team_color)
    bpyObjects = create_mesh_objects(model, bpyMaterials)
    armatureObject = create_armature_object(model, bpyObjects, importProperties.bone_size)
    create_armature_actions(armatureObject, model, importProperties.frame_time)
    create_object_actions(model, bpyObjects, importProperties.frame_time)
