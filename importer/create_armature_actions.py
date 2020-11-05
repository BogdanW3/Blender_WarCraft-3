import bpy
import mathutils

import constants


def create_armature_actions(armatureObject, model, frameTime):
    nodes = model.nodes
    sequences = model.sequences
    action = bpy.data.actions.new(name='#UNANIMATED')
    add_sequence_to_armature('#UNANIMATED', armatureObject)
    for node in nodes:
        boneName = node.node.name
        dataPath = 'pose.bones["' + boneName + '"]'
        locationFcurveX = action.fcurves.new(dataPath + '.location', 0, boneName)
        locationFcurveY = action.fcurves.new(dataPath + '.location', 1, boneName)
        locationFcurveZ = action.fcurves.new(dataPath + '.location', 2, boneName)
        locationFcurveX.keyframe_points.insert(0.0, 0.0)
        locationFcurveY.keyframe_points.insert(0.0, 0.0)
        locationFcurveZ.keyframe_points.insert(0.0, 0.0)
        rotationFcurveX = action.fcurves.new(dataPath + '.rotation_euler', 0, boneName)
        rotationFcurveY = action.fcurves.new(dataPath + '.rotation_euler', 1, boneName)
        rotationFcurveZ = action.fcurves.new(dataPath + '.rotation_euler', 2, boneName)
        rotationFcurveX.keyframe_points.insert(0.0, 0.0)
        rotationFcurveY.keyframe_points.insert(0.0, 0.0)
        rotationFcurveZ.keyframe_points.insert(0.0, 0.0)
        scaleFcurveX = action.fcurves.new(dataPath + '.scale', 0, boneName)
        scaleFcurveY = action.fcurves.new(dataPath + '.scale', 1, boneName)
        scaleFcurveZ = action.fcurves.new(dataPath + '.scale', 2, boneName)
        scaleFcurveX.keyframe_points.insert(0.0, 1.0)
        scaleFcurveY.keyframe_points.insert(0.0, 1.0)
        scaleFcurveZ.keyframe_points.insert(0.0, 1.0)
    for sequence in sequences:
        intervalStart = sequence.interval_start
        intervalEnd = sequence.interval_end
        action = bpy.data.actions.new(name=sequence.name)
        add_sequence_to_armature(sequence.name, armatureObject)
        for node in nodes:
            boneName = node.node.name
            dataPath = 'pose.bones["' + boneName + '"]'
            translations = node.node.translations
            rotations = node.node.rotations
            scalings = node.node.scalings
            if translations:
                locationFcurveX = None
                locationFcurveY = None
                locationFcurveZ = None
                interpolationType = constants.INTERPOLATION_TYPE_NAMES[translations.interpolation_type]
                for index in range(translations.tracks_count):
                    time = translations.times[index]
                    translation = translations.values[index]
                    if intervalStart <= time and time <= intervalEnd:
                        if not locationFcurveX:
                            locationFcurveX = action.fcurves.new(dataPath + '.location', 0, boneName)
                        if not locationFcurveY:
                            locationFcurveY = action.fcurves.new(dataPath + '.location', 1, boneName)
                        if not locationFcurveZ:
                            locationFcurveZ = action.fcurves.new(dataPath + '.location', 2, boneName)
                        realTime = round((time - intervalStart) / frameTime, 0)
                        locationXKeyframe = locationFcurveX.keyframe_points.insert(realTime, translation[0])
                        locationYKeyframe = locationFcurveY.keyframe_points.insert(realTime, translation[1])
                        locationZKeyframe = locationFcurveZ.keyframe_points.insert(realTime, translation[2])
                        locationXKeyframe.interpolation = interpolationType
                        locationYKeyframe.interpolation = interpolationType
                        locationZKeyframe.interpolation = interpolationType
                if not locationFcurveX:
                    locationFcurveX = action.fcurves.new(dataPath + '.location', 0, boneName)
                    locationFcurveX.keyframe_points.insert(0.0, 0.0)
                if not locationFcurveY:
                    locationFcurveY = action.fcurves.new(dataPath + '.location', 1, boneName)
                    locationFcurveY.keyframe_points.insert(0.0, 0.0)
                if not locationFcurveZ:
                    locationFcurveZ = action.fcurves.new(dataPath + '.location', 2, boneName)
                    locationFcurveZ.keyframe_points.insert(0.0, 0.0)
            if rotations:
                rotationFcurveX = None
                rotationFcurveY = None
                rotationFcurveZ = None
                interpolationType = constants.INTERPOLATION_TYPE_NAMES[rotations.interpolation_type]
                for index in range(rotations.tracks_count):
                    time = rotations.times[index]
                    rotation = rotations.values[index]
                    if intervalStart <= time and time <= intervalEnd:
                        if not rotationFcurveX:
                            rotationFcurveX = action.fcurves.new(dataPath + '.rotation_euler', 0, boneName)
                        if not rotationFcurveY:
                            rotationFcurveY = action.fcurves.new(dataPath + '.rotation_euler', 1, boneName)
                        if not rotationFcurveZ:
                            rotationFcurveZ = action.fcurves.new(dataPath + '.rotation_euler', 2, boneName)
                        realTime = round((time - intervalStart) / frameTime, 0)
                        euler = mathutils.Quaternion(mathutils.Vector(rotation)).to_euler('XYZ')
                        rotationXKeyframe = rotationFcurveX.keyframe_points.insert(realTime, euler[0])
                        rotationYKeyframe = rotationFcurveY.keyframe_points.insert(realTime, euler[1])
                        rotationZKeyframe = rotationFcurveZ.keyframe_points.insert(realTime, euler[2])
                        rotationXKeyframe.interpolation = interpolationType
                        rotationYKeyframe.interpolation = interpolationType
                        rotationZKeyframe.interpolation = interpolationType
                if not rotationFcurveX:
                    rotationFcurveX = action.fcurves.new(dataPath + '.rotation_euler', 0, boneName)
                    rotationFcurveX.keyframe_points.insert(0.0, 0.0)
                if not rotationFcurveY:
                    rotationFcurveY = action.fcurves.new(dataPath + '.rotation_euler', 1, boneName)
                    rotationFcurveY.keyframe_points.insert(0.0, 0.0)
                if not rotationFcurveZ:
                    rotationFcurveZ = action.fcurves.new(dataPath + '.rotation_euler', 2, boneName)
                    rotationFcurveZ.keyframe_points.insert(0.0, 0.0)
            if scalings:
                scaleFcurveX = None
                scaleFcurveY = None
                scaleFcurveZ = None
                interpolationType = constants.INTERPOLATION_TYPE_NAMES[scalings.interpolation_type]
                for index in range(scalings.tracks_count):
                    time = scalings.times[index]
                    scale = scalings.values[index]
                    if intervalStart <= time and time <= intervalEnd:
                        if not scaleFcurveX:
                            scaleFcurveX = action.fcurves.new(dataPath + '.scale', 0, boneName)
                        if not scaleFcurveY:
                            scaleFcurveY = action.fcurves.new(dataPath + '.scale', 1, boneName)
                        if not scaleFcurveZ:
                            scaleFcurveZ = action.fcurves.new(dataPath + '.scale', 2, boneName)
                        realTime = round((time - intervalStart) / frameTime, 0)
                        scaleXKeyframe = scaleFcurveX.keyframe_points.insert(realTime, scale[0])
                        scaleYKeyframe = scaleFcurveY.keyframe_points.insert(realTime, scale[1])
                        scaleZKeyframe = scaleFcurveZ.keyframe_points.insert(realTime, scale[2])
                        scaleXKeyframe.interpolation = interpolationType
                        scaleYKeyframe.interpolation = interpolationType
                        scaleZKeyframe.interpolation = interpolationType
                if not scaleFcurveX:
                    scaleFcurveX = action.fcurves.new(dataPath + '.scale', 0, boneName)
                    scaleFcurveX.keyframe_points.insert(0.0, 1.0)
                if not scaleFcurveY:
                    scaleFcurveY = action.fcurves.new(dataPath + '.scale', 1, boneName)
                    scaleFcurveY.keyframe_points.insert(0.0, 1.0)
                if not scaleFcurveZ:
                    scaleFcurveZ = action.fcurves.new(dataPath + '.scale', 2, boneName)
                    scaleFcurveZ.keyframe_points.insert(0.0, 1.0)


def add_sequence_to_armature(sequenceName, armatureObject):
    warcraft3data = armatureObject.data.warcraft_3
    sequence = warcraft3data.sequencesList.add()
    sequence.name = sequenceName
