#openPose 18 keypoints https://blog.csdn.net/ssyy5233225/article/details/105265488

openPose16={0:"Nose",
            1:"Neck",
            2:"RShoulder",
            3:"RElbow",
            4:"RWrist",
            5:"LShoulder",
            6:"LElbow",
            7:"LWrist",
            8:"RHip",
            9:"RKnee",
            10:"RAnkle",
            11:"LHip",
            12:"LKnee",
            13:"LAnkle",
            14:"REye",
            15:"LEye",
            16:"REar",
            17:"LEar"}

                            #hm36
openPose25={0: "Nose",     #15
            1:"Neck",      #13
            2:"RShoulder", #25
            3:"RElbow",    #26
            4:"RWrist",    #27
            5:"LShoulder", #17
            6:"LElbow",    #18
            7:"LWrist",    #19
            8:"MidHip",    #0
            9:"RHip",      #1
            10:"RKnee",    #2
            11:"RAnkle",   #3
            12:"LHip",     #6
            13:"LKnee",    #7
            14:"LAnkle",   #8
            15:"REye",
            16:"LEye",
            17:"REar",
            18:"LEar",
            19:"LBigToe",
            20:"LSmallToe",
            21:"LHeel",
            22:"RBigToe",
            23:"RSmallToe",
            24:"RHeel"}

# Stacked Hourglass produces 16 joints. These are the names.
SH_NAMES = ['']*16     #openpose25
SH_NAMES[0]  = 'RFoot' #11
SH_NAMES[1]  = 'RKnee' #10
SH_NAMES[2]  = 'RHip'  #9
SH_NAMES[3]  = 'LHip'  #12
SH_NAMES[4]  = 'LKnee' #13
SH_NAMES[5]  = 'LFoot' #14
SH_NAMES[6]  = 'Hip'   #8
SH_NAMES[7]  = 'Spine' #无
SH_NAMES[8]  = 'Thorax'#1
SH_NAMES[9]  = 'Head'  #0
SH_NAMES[10] = 'RWrist'#4
SH_NAMES[11] = 'RElbow'#3
SH_NAMES[12] = 'RShoulder'#2
SH_NAMES[13] = 'LShoulder'#5
SH_NAMES[14] = 'LElbow'#6
SH_NAMES[15] = 'LWrist'#7


# Joints in H3.6M -- data has 32 joints, but only 17 that move; these are the indices.
H36M_NAMES = ['']*32
H36M_NAMES[0]  = 'Hip' # 8
H36M_NAMES[1]  = 'RHip'# 9
H36M_NAMES[2]  = 'RKnee'#10
H36M_NAMES[3]  = 'RFoot'#11
H36M_NAMES[6]  = 'LHip' #12
H36M_NAMES[7]  = 'LKnee'#13
H36M_NAMES[8]  = 'LFoot'#14
H36M_NAMES[12] = 'Spine'#无
H36M_NAMES[13] = 'Thorax'#1
H36M_NAMES[14] = 'Neck/Nose'#0
H36M_NAMES[15] = 'Head'#无
H36M_NAMES[17] = 'LShoulder'#5
H36M_NAMES[18] = 'LElbow'#6
H36M_NAMES[19] = 'LWrist'#7
H36M_NAMES[25] = 'RShoulder'#2
H36M_NAMES[26] = 'RElbow'#6
H36M_NAMES[27] = 'RWrist'#4