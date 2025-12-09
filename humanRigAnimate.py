import bpy

sides = ['R', 'L']
#sides = ['R']

armatures = ['metarig']
limbs = {
    'shoulder.SIDE' : {
        0: [ ['shoulder.ctrl.SIDE', 'X',  0.2] ],
        1: [ ['shoulder.ctrl.SIDE', 'Y', -1] ],
        2: [ ['shoulder.ctrl.SIDE', 'Z', 0.2] ]
    },
    'breast.SIDE' : {
        0: [ ['shoulder.ctrl.SIDE', 'X',  0.2] ],
        1: [ ['shoulder.ctrl.SIDE', 'Y', 0.1] ],
        2: [ ['shoulder.ctrl.SIDE', 'Z', 0.2] ]
    },
    'arm.ctrl.SIDE' : {
        0: [ ['hand.ctrl.SIDE', 'X', -1] ],
        1: [ ['hand.ctrl.SIDE', 'Y', -1] ],
        2: [ ['hand.ctrl.SIDE', 'Z', 1] ]
    },
    'hand.SIDE' : {
        0: [ ['hand.ctrl.SIDE', 'X', -1] ],
        2: [ ['hand.ctrl.SIDE', 'Y', -1] ]
    },
    'forearm.SIDE' : {
        1: [ ['hand.ctrl.SIDE', 'Z', -0.2] ]
    },
    'leg.ctrl.SIDE' : {
        0: [ ['foot.ctrl.SIDE', 'X', -1] ],
        1: [ ['foot.ctrl.SIDE', 'Y', -1] ],
        2: [ ['foot.ctrl.SIDE', 'Z', 1] ]
    },
    'foot.SIDE' : {
        0: [ ['foot.ctrl.SIDE', 'X', -1] ],
        1: [ ['foot.ctrl.SIDE', 'Y', 1] ],
        2: [ ['foot.ctrl.SIDE', 'Z', -1] ]
    },
    'toe.SIDE' : {
        0: [ ['toe.ctrl.SIDE', 'X', 1] ]
    },
    'shin.SIDE' : {
        2: [ ['foot.ctrl.SIDE', 'Z', 0.2] ]
    },
    'thumb.SIDE' : {
        2: [ ['fingers.ctrl.SIDE', 'Z', 0.8] ]
    },
    'thumb.0.SIDE' : {
        0: [ ['thumb.ctrl.SIDE', 'X', 0.1] ]
    },
    'thumb.1.SIDE' : {
        0: [ ['thumb.ctrl.SIDE', 'X', 0.8] ]
    },
    'thumb.2.SIDE' : {
        0: [ ['thumb.ctrl.SIDE', 'X', 2] ]
    },
    'index.SIDE' : {
        2: [ ['fingers.ctrl.SIDE', 'Y', 0.8] ]
    },
    'index.0.SIDE' : {
        0: [ ['index.ctrl.SIDE', 'X', 1.8] ]
    },
    'index.1.SIDE' : {
        0: [ ['index.ctrl.SIDE', 'X', 1.6] ]
    },
    'index.2.SIDE' : {
        0: [ ['index.ctrl.SIDE', 'X', 2.2] ]
    },
    'middle.SIDE' : {
        2: [ ['fingers.ctrl.SIDE', 'Y', 0.2] ]
    },
    'middle.0.SIDE' : {
        0: [ ['middle.ctrl.SIDE', 'X', 1.8] ]
    },
    'middle.1.SIDE' : {
        0: [ ['middle.ctrl.SIDE', 'X', 1.6] ]
    },
    'middle.2.SIDE' : {
        0: [ ['middle.ctrl.SIDE', 'X', 2.2] ]
    },
    'ring.SIDE' : {
        2: [ ['fingers.ctrl.SIDE', 'Y', -0.6] ]
    },
    'ring.0.SIDE' : {
        0: [ ['ring.ctrl.SIDE', 'X', 1.8] ]
    },
    'ring.1.SIDE' : {
        0: [ ['ring.ctrl.SIDE', 'X', 1.6] ]
    },
    'ring.2.SIDE' : {
        0: [ ['ring.ctrl.SIDE', 'X', 2.2] ]
    },
    'pinky.SIDE' : {
        2: [ ['fingers.ctrl.SIDE', 'Y', -0.8] ]
    },
    'pinky.0.SIDE' : {
        0: [ ['pinky.ctrl.SIDE', 'X', 1.8] ]
    },
    'pinky.1.SIDE' : {
        0: [ ['pinky.ctrl.SIDE', 'X', 1.6] ]
    },
    'pinky.2.SIDE' : {
        0: [ ['pinky.ctrl.SIDE', 'X', 2.2] ]
    }
}
torso = {
    'spine.1' : {
        0: [ ['pelvis.ctrl', 'X', 0.7] ],
        1: [ ['pelvis.ctrl', 'Y', 0.7] ],
        2: [ ['pelvis.ctrl', 'Z', 0.7] ]
    },
    'spine.2' : {
        0: [ ['pelvis.ctrl', 'X', 0.8] ],
        1: [ ['pelvis.ctrl', 'Y', 0.8] ],
        2: [ ['pelvis.ctrl', 'Z', 0.8] ]
    },
    'spine.3' : {
        0: [ ['pelvis.ctrl', 'X', 0.9] ],
        1: [ ['pelvis.ctrl', 'Y', 0.9] ],
        2: [ ['pelvis.ctrl', 'Z', 0.9] ]
    },
    'spine.4' : {
        0: [ ['chest.ctrl', 'X', 0.8], ['pelvis.ctrl', 'X',  0.4] ],
        1: [ ['chest.ctrl', 'Y', 0.8], ['pelvis.ctrl', 'Y',  0.4] ],
        2: [ ['chest.ctrl', 'Z', 0.8], ['pelvis.ctrl', 'Z',  0.4] ]
    },
    #neck
    'spine.5' : {
        0: [ ['neck.ctrl', 'X', 0.7], ['chest.ctrl', 'X', 0.3] ],
        1: [ ['neck.ctrl', 'Y', 0.7], ['chest.ctrl', 'Y', 0.3] ],
        2: [ ['neck.ctrl', 'Z', 0.7], ['chest.ctrl', 'Z', 0.3] ]
    },
    'spine.6' : {
        0: [ ['neck.ctrl', 'X',  0.7] ],
        1: [ ['neck.ctrl', 'Y', 0.7] ],
        2: [ ['neck.ctrl', 'Z', 0.7] ]
    },
    #head
    'spine.7' : {
        0: [ ['head.ctrl', 'X', 1] ],
        1: [ ['head.ctrl', 'Y', 1] ],
        2: [ ['head.ctrl', 'Z', 1] ]
    }
}

#bone constraints
bonesConstr = {
    'forearm.SIDE': {
        'IK': {
            'subtarget': 'arm.ctrl.SIDE', 'pole_subtarget': 'elbow.pole.SIDE', 'chain_count': 2
        }
    },
    'elbow.pole.SIDE' : {
        'COPY_LOCATION': {
            'subtarget': 'hand.ctrl.SIDE', 'target_space': 'LOCAL_WITH_PARENT', 'owner_space': 'WORLD', 'invert_x': True, 'invert_y': True, 'use_offset': True
        }
    },
    'shin.SIDE': {
        'IK': {
            'subtarget': 'leg.ctrl.SIDE', 'pole_subtarget': 'knee.pole.SIDE', 'chain_count': 2
        }
    },
    'knee.pole.SIDE' : {
        'COPY_LOCATION': {
            'subtarget': 'foot.ctrl.SIDE', 'target_space': 'LOCAL_WITH_PARENT', 'owner_space': 'WORLD', 'invert_x': True, 'invert_y': True, 'use_z': False, 'use_offset': True
        }
    },
    'thumb.ctrl.SIDE' : {
        'COPY_ROTATION': {
            'subtarget': 'fingers.ctrl.SIDE', 'mix_mode': 'ADD', 'target_space': 'LOCAL', 'owner_space': 'LOCAL', 'use_y': False, 'use_z': False
        }
    },
    'index.ctrl.SIDE' : {
        'COPY_ROTATION': {
            'subtarget': 'fingers.ctrl.SIDE', 'mix_mode': 'ADD', 'target_space': 'LOCAL', 'owner_space': 'LOCAL', 'use_y': False, 'use_z': False
        }
    },
    'middle.ctrl.SIDE' : {
        'COPY_ROTATION': {
            'subtarget': 'fingers.ctrl.SIDE', 'mix_mode': 'ADD', 'target_space': 'LOCAL', 'owner_space': 'LOCAL', 'use_y': False, 'use_z': False
        }
    },
    'ring.ctrl.SIDE' : {
        'COPY_ROTATION': {
            'subtarget': 'fingers.ctrl.SIDE', 'mix_mode': 'ADD', 'target_space': 'LOCAL', 'owner_space': 'LOCAL', 'use_y': False, 'use_z': False
        }
    },
    'pinky.ctrl.SIDE' : {
        'COPY_ROTATION': {
            'subtarget': 'fingers.ctrl.SIDE', 'mix_mode': 'ADD', 'target_space': 'LOCAL', 'owner_space': 'LOCAL', 'use_y': False, 'use_z': False
        }
    },
    'fingers.ctrl.SIDE' : {
        'LIMIT_ROTATION': {
            'euler_order': 'XYZ', 'use_limit_x': False, 'min_x': 0, 'max_x': 0, 'owner_space': 'LOCAL'
        }
    }

}               
def boneDrivers(armature, items, sides=['R']):
    for side in sides:
        for kObj, vObj in items.items():
            kObj = kObj.replace('SIDE', side)
            driven = armature.pose.bones[kObj]
            driven.rotation_mode = 'XYZ'
            for kAttr, vAttr in vObj.items():
                driver = driven.driver_add('rotation_euler', kAttr).driver
                driver.type = 'SCRIPTED'
                driver.expression = 'var'
                for v in vAttr:
                    var = driver.variables.new()
                    var.type = 'TRANSFORMS'
                    vSide = v[0].replace('SIDE', side)
                    target = var.targets[0]
                    target.id = armature
                    target.bone_target = vSide
                    target.transform_type = f'ROT_{v[1]}'
                    target.transform_space = 'LOCAL_SPACE'
                    driver.expression += f' * {v[2]}'    

def boneConstraints(armature, items, sides=['R']):    
    for side in sides:
        for kBone, vConstraints in items.items():
            kBone = kBone.replace('SIDE', side)
            bone = armature.pose.bones.get(kBone)
            for cK, cV in vConstraints.items():
                constr = bone.constraints.new(cK)
                if 'LIMIT' not in cK:
                    constr.target = armature
                
                for modK, modV in cV.items():
                    if modK == 'subtarget':
                        modV = modV.replace('SIDE', side)
                    if modK == 'pole_subtarget':
                        constr.pole_target = armature
                        modV = modV.replace('SIDE', side)
  
                    setattr(constr, modK, modV)


for a in armatures:
    armature = bpy.data.objects[a]
    if armature.animation_data and armature.animation_data.drivers:
        # Get a list of drivers (iterate over a copy to avoid issues during removal)
        drivers_to_remove = list(armature.animation_data.drivers)
        for driver in drivers_to_remove:
            # Remove the driver using its data_path
            armature.driver_remove(driver.data_path)  
    boneDrivers(armature, torso)
    boneDrivers(armature, limbs, sides)
    
    
for a in armatures:
    armature = bpy.data.objects[a]                             
    bones = armature.pose.bones
    for bone in bones:
        if bone.constraints:
            constraints = list(bone.constraints)
            for c in constraints:
                bone.constraints.remove(c)
    boneConstraints(armature, bonesConstr, sides)

