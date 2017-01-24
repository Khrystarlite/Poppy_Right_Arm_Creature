
def config():
    conf ={}
    conf['controllers'] = {}
    conf['controllers']['upper_body_controler'] = {
        'port': '/dev/ttyUSB0',     # For Linux
        #'port': '/dev/tty.usbserial-AI03QEN0', # For OSX
        'sync_read': False,
        'attached_motors': ['arms'],
        'protocol': 1,
    }
    conf['motorgroups']={}
    conf['motorgroups'] = {
        'arms': ['right_arm'],
        'right_arm': ['r_shoulder_x', 'r_shoulder_y', 'r_arm_z','r_elbow_y']
    }
    conf['motors'] = {}
    conf['motors']['r_shoulder_y'] = {
        'id': 51,
        'type': 'MX-28',
        'orientation': 'indirect',
        'offset': 0.0,
        'angle_limit': (-50, 170),
    }
    conf['motors']['r_shoulder_x'] = {
        'id': 52,
        'type': 'MX-28',
        'orientation': 'indirect',
        'offset': 0.0,
        'angle_limit': (-90, 0),
    }
    conf['motors']['r_arm_z'] = {
        'id': 53,
        'type': 'MX-28',
        'orientation': 'indirect',
        'offset': 0.0,
        'angle_limit': (-20, 95),
    }
    conf['motors']['r_elbow_y'] = {
        'id': 54,
        'type': 'MX-28',
        'orientation': 'indirect',
        'offset': 0.0,
        'angle_limit': (0, 130),
    }

    return conf


