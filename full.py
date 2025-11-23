import bpy
import math
armature = bpy.data.objects['metarig']
if armature.animation_data and armature.animation_data.drivers:
        # Get a list of drivers (iterate over a copy to avoid issues during removal)
        drivers_to_remove = list(armature.animation_data.drivers)
        for driver in drivers_to_remove:
            # Remove the driver using its data_path
            armature.driver_remove(driver.data_path)
sides = ['R', 'L']
#sides = ['R']
limbs = {
    'shoulder.SIDE' : {
        'rotation_euler': {
            'type': 'SCRIPTED', 'expression': 'var', 'var_type': 'TRANSFORMS', 'transform_type': 'ROT_', 'transform_space': 'LOCAL_SPACE',
            'axis': {
                0: [ ['shoulder.ctrl.SIDE', 'X',  0.2] ],
                1: [ ['shoulder.ctrl.SIDE', 'Y', -1] ],
                2: [ ['shoulder.ctrl.SIDE', 'Z', 0.2] ]
            }
        }
    },
    'breast.SIDE' : {
        'rotation_euler': {
            'type': 'SCRIPTED', 'expression': 'var', 'var_type': 'TRANSFORMS', 'transform_type': 'ROT_', 'transform_space': 'LOCAL_SPACE',
            'axis': {
                0: [ ['shoulder.ctrl.SIDE', 'X',  0.2] ],
                1: [ ['shoulder.ctrl.SIDE', 'Y', 0.1] ],
                2: [ ['shoulder.ctrl.SIDE', 'Z', 0.2] ]
            }
        }
    },
    'arm.ctrl.SIDE' : {
        'rotation_euler': {
            'type': 'SCRIPTED', 'expression': 'var', 'var_type': 'TRANSFORMS', 'transform_type': 'ROT_', 'transform_space': 'WORLD_SPACE',
            'axis': {
                0: [ ['hand.ctrl.SIDE', 'X', -1] ]
            }
        }
    },
    'hand.SIDE' : {
        'rotation_euler': {
            'type': 'SCRIPTED', 'expression': 'var', 'var_type': 'TRANSFORMS', 'transform_type': 'ROT_', 'transform_space': 'LOCAL_SPACE',
            'axis': {
                0: [ ['hand.ctrl.SIDE', 'X', -1] ],
                2: [ ['hand.ctrl.SIDE', 'Y', -1] ]
            }
        }
    },
    'forearm.SIDE' : {
        'rotation_euler': {
            'type': 'SCRIPTED', 'expression': 'var', 'var_type': 'TRANSFORMS', 'transform_type': 'ROT_', 'transform_space': 'LOCAL_SPACE',
            'axis': {
                1: [ ['hand.ctrl.SIDE', 'Z', -0.2] ]
            }
        }
    },
    'leg.ctrl.SIDE' : {
        'rotation_euler': {
            'type': 'SCRIPTED', 'expression': 'var', 'var_type': 'TRANSFORMS', 'transform_type': 'ROT_', 'transform_space': 'WORLD_SPACE',
            'axis': {
                0: [ ['foot.ctrl.SIDE', 'X', -1] ]
            }
        }
    },
    'foot.SIDE' : {
        'rotation_euler': {
            'type': 'SCRIPTED', 'expression': 'var', 'var_type': 'TRANSFORMS', 'transform_type': 'ROT_', 'transform_space': 'LOCAL_SPACE',
            'axis': {
                0: [ ['foot.ctrl.SIDE', 'Z', -1] ],
                1: [ ['foot.ctrl.SIDE', 'Y', 1] ],
                2: [ ['foot.ctrl.SIDE', 'X', 1] ]
            }
        }
    },
    'toe.SIDE' : {
        'rotation_euler': {
            'type': 'SCRIPTED', 'expression': 'var', 'var_type': 'TRANSFORMS', 'transform_type': 'ROT_', 'transform_space': 'LOCAL_SPACE',
            'axis': {
                0: [ ['toe.ctrl.SIDE', 'X', 1] ]
            }
        }
    },
    'shin.SIDE' : {
        'rotation_euler': {
            'type': 'SCRIPTED', 'expression': 'var', 'var_type': 'TRANSFORMS', 'transform_type': 'ROT_', 'transform_space': 'LOCAL_SPACE',
            'axis': {
                2: [ ['foot.ctrl.SIDE', 'Z', 0.2] ]
            }
        }
    }
}
torso = {
    'spine.1' : {
        'rotation_euler': {
            'type': 'SCRIPTED', 'expression': 'var', 'var_type': 'TRANSFORMS', 'transform_type': 'ROT_', 'transform_space': 'LOCAL_SPACE',
            'axis': {
                0: [ ['pelvis.ctrl', 'X', 0.7] ],
                1: [ ['pelvis.ctrl', 'Y', 0.7] ],
                2: [ ['pelvis.ctrl', 'Z', 0.7] ]
            }
        }
    },
    'spine.2' : {
        'rotation_euler': {
            'type': 'SCRIPTED', 'expression': 'var', 'var_type': 'TRANSFORMS', 'transform_type': 'ROT_', 'transform_space': 'LOCAL_SPACE',
            'axis': {
                0: [ ['pelvis.ctrl', 'X', 0.8] ],
                1: [ ['pelvis.ctrl', 'Y', 0.8] ],
                2: [ ['pelvis.ctrl', 'Z', 0.8] ]
            }
        }
    },
    'spine.3' : {
        'rotation_euler': {
            'type': 'SCRIPTED', 'expression': 'var', 'var_type': 'TRANSFORMS', 'transform_type': 'ROT_', 'transform_space': 'LOCAL_SPACE',
            'axis': {
                0: [ ['pelvis.ctrl', 'X', 0.9] ],
                1: [ ['pelvis.ctrl', 'Y', 0.9] ],
                2: [ ['pelvis.ctrl', 'Z', 0.9] ]
            }
        }
    },
    'spine.4' : {
        'rotation_euler': {
            'type': 'SCRIPTED', 'expression': 'var', 'var_type': 'TRANSFORMS', 'transform_type': 'ROT_', 'transform_space': 'LOCAL_SPACE',
            'axis': {
                0: [ ['chest.ctrl', 'X', 0.8], ['pelvis.ctrl', 'X',  0.4] ],
                1: [ ['chest.ctrl', 'Y', 0.8], ['pelvis.ctrl', 'Y',  0.4] ],
                2: [ ['chest.ctrl', 'Z', 0.8], ['pelvis.ctrl', 'Z',  0.4] ]
            }
        }
    },
    #neck
    'spine.5' : {
        'rotation_euler': {
            'type': 'SCRIPTED', 'expression': 'var', 'var_type': 'TRANSFORMS', 'transform_type': 'ROT_', 'transform_space': 'LOCAL_SPACE',
            'axis': {
                0: [ ['neck.ctrl', 'X', 0.7], ['chest.ctrl', 'X', 0.3] ],
                1: [ ['neck.ctrl', 'Y', 0.7], ['chest.ctrl', 'Y', 0.3] ],
                2: [ ['neck.ctrl', 'Z', 0.7], ['chest.ctrl', 'Z', 0.3] ]
            }
        }
    },
    'spine.6' : {
        'rotation_euler': {
            'type': 'SCRIPTED', 'expression': 'var', 'var_type': 'TRANSFORMS', 'transform_type': 'ROT_', 'transform_space': 'LOCAL_SPACE',
            'axis': {
                0: [ ['neck.ctrl', 'X',  0.7] ],
                1: [ ['neck.ctrl', 'Y', 0.7] ],
                2: [ ['neck.ctrl', 'Z', 0.7] ]
            }
        }
    },
    #head
    'spine.7' : {
        'rotation_euler': {
            'type': 'SCRIPTED', 'expression': 'var', 'var_type': 'TRANSFORMS', 'transform_type': 'ROT_', 'transform_space': 'LOCAL_SPACE',
            'axis': {
                0: [ ['head.ctrl', 'X', 1] ],
                1: [ ['head.ctrl', 'Y', 1] ],
                2: [ ['head.ctrl', 'Z', 1] ]
            }
        }
    }
}
fingers = {
    'index': [1, 1.4, 2], 
    'middle': [1, 1.4, 2], 
    'ring': [1, 1.4, 2], 
    'pinky': [1, 1.4, 2], 
    'thumb': [-1, 1, 3]
}
def rigFingers(armature, objs):
    for side in sides:
        for k, v in objs.items():
            ctrl_name = f'{k}.ctrl.{side}'
            ctrl_bone = armature.pose.bones[ctrl_name]
            for i, val in enumerate(v):
                driven_name = f'{k}.{i}.{side}'
                driven_bone = armature.pose.bones[driven_name]
                driven_bone.rotation_mode = 'XYZ'

                driver = driven_bone.driver_add('rotation_euler', 0).driver
                driver.type = 'SCRIPTED'
                
                var = driver.variables.new()
                var.type = 'TRANSFORMS'
                target = var.targets[0]
                target.id = armature
                target.bone_target = ctrl_name
                target.transform_type = 'ROT_X'
                target.transform_space = 'LOCAL_SPACE'
                driver.expression = f'(var + ({var.name} * {v[i]})) * -1'   
def rigBody(armature, items):
    for kObj, vObj in items.items():
        driven = armature.pose.bones[kObj]
        driven.rotation_mode = 'XYZ'
        for kAttr, vAttr in vObj.items():
             for coord, objs in vAttr['axis'].items():
                driver = driven.driver_add(kAttr, coord).driver
                driver.type = vAttr['type']
                driver.expression = vAttr['expression']
                expressionAcum = 0
                for v in objs:
                    var = driver.variables.new()
                    var.type = vAttr['var_type']
                    target = var.targets[0]
                    target.id = armature
                    target.bone_target = v[0]
                    target.transform_type = f'{vAttr["transform_type"]}{v[1]}'
                    target.transform_space = vAttr['transform_space']
                    driver.expression += f' * {v[2]}'

def rigLimbs(armature, items):
    for side in sides:
        for kObj, vObj in items.items():
            kObj = kObj.replace('SIDE', side)
            driven = armature.pose.bones[kObj]
            driven.rotation_mode = 'XYZ'
            for kAttr, vAttr in vObj.items():
                for coord, objs in vAttr['axis'].items():
                    driver = driven.driver_add(kAttr, coord).driver
                    driver.type = vAttr['type']
                    driver.expression = vAttr['expression']
                    expressionAcum = 0
                    for v in objs:
                        var = driver.variables.new()
                        var.type = vAttr['var_type']
                        vSide = v[0].replace('SIDE', side)
                        target = var.targets[0]
                        target.id = armature
                        target.bone_target = vSide
                        target.transform_type = f'{vAttr["transform_type"]}{v[1]}'
                        target.transform_space = vAttr['transform_space']
                        driver.expression += f' * {v[2]}'


                    
rigBody(armature, torso)
rigLimbs(armature, limbs)
rigFingers(armature, fingers)