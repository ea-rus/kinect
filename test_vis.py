#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys

if len(sys.argv)>1:
    #graphic mode
    import numpy as np
    from nite2 import *

    import time

    # Test code -- print head coordinates of users

    NiTE.initialize()

    tracker = UserTracker()
    tracker.create()

    def USER_MESSAGE(m):
        print m

    g_visibleUsers={}

    g_skeletonStates={}

    def updateUserState( user, ts):

            if user.isNew():
                    USER_MESSAGE("New")
            elif (user.isVisible() and not g_visibleUsers[user.getId()]):
                    USER_MESSAGE("Visible")
            elif (not user.isVisible() and g_visibleUsers[user.getId()]):
                    USER_MESSAGE("Out of Scene")
            elif (user.isLost()):
                    USER_MESSAGE("Lost")

            g_visibleUsers[user.getId()] = user.isVisible();


            #if (g_skeletonStates[user.getId()] != user.getSkeleton().getState()):
        
                    #switch(g_skeletonStates[user.getId()] = user.getSkeleton().getState())
                    #{
                    #case nite::SKELETON_NONE:
                            #USER_MESSAGE("Stopped tracking.")
                            #break;
                    #case nite::SKELETON_CALIBRATING:
                            #USER_MESSAGE("Calibrating...")
                            #break;
                    #case nite::SKELETON_TRACKED:
                            #USER_MESSAGE("Tracking!")
                            #break;
                    #case nite::SKELETON_CALIBRATION_ERROR_NOT_IN_POSE:
                    #case nite::SKELETON_CALIBRATION_ERROR_HANDS:
                    #case nite::SKELETON_CALIBRATION_ERROR_LEGS:
                    #case nite::SKELETON_CALIBRATION_ERROR_HEAD:
                    #case nite::SKELETON_CALIBRATION_ERROR_TORSO:
                            #USER_MESSAGE("Calibration Failed... :-|")
                            #break;
                    #}
            #}
    #}

    

    import numpy as np
    import matplotlib.pyplot as plt
    import mpl_toolkits.mplot3d.axes3d as p3
    import matplotlib.animation as animation
    import matplotlib
    matplotlib.pyplot.autoscale(enable=True, axis='both', tight=None)

    import random



    fig = plt.figure()
    ax = p3.Axes3D(fig)

    # Fifty lines of random 3-D lines
    data = [i for i in range(50)]

    # Creating fifty line objects.
    # NOTE: Can't pass empty arrays into 3d version of plot()


    # Setting the axes properties
    ax.set_xlim3d([-600, 100])
    ax.set_xlabel('X')

    ax.set_ylim3d([-1000, 1000])
    ax.set_ylabel('Y')

    ax.set_zlim3d([200, 3500])
    ax.set_zlabel('Z')

    ax.set_title('3D Test')

    # line, = ax.plot([0,10],[0,10], [0,10])


    def animate(i):
            
            lims=list(ax.get_xlim3d())+list(ax.get_ylim3d())+list(ax.get_zlim3d())
            
            lines=[]
            f = tracker.readFrame()
            users=f.getUsers()
            #print users
            for uid in users:               
                    
                    user = f.getUserById(uid)
                    uid=user.getId()
                    updateUserState(user, f.getTimestamp());
                    if user.isNew():
                            print("New user id %d !" % uid)
                            tracker.startSkeletonTracking(uid)
                    
                    elif user.getSkeleton().getState() == SkeletonState.SKELETON_TRACKED:
                        skel=user.getSkeleton()
                        #for atr in ['JOINT_HEAD',
 #'JOINT_LEFT_HAND','JOINT_RIGHT_HAND',
#'JOINT_TORSO',
#'JOINT_LEFT_FOOT','JOINT_RIGHT_FOOT']:
                            #joint=skel.getJoint(getattr(JointType,atr))
                            #pos=joint.getPosition()
                            
                            #lims=[ min(pos[0], lims[0]),  max(pos[0], lims[1]),
                                   #min(pos[1], lims[2]),  max(pos[1], lims[3]),
                                   #min(pos[2], lims[4]),  max(pos[2], lims[5])]
                            
                            #lines.append(ax.plot([ pos[0]],[  pos[1]],[  pos[2]], 'ro')[0])
#'b'         blue
#'g'         green
#'r'         red
#'c'         cyan
#'m'         magenta
#'y'         yellow
#'k'         black
#'w'         white

                            
                            
                        head = user.getSkeleton().getJoint(JointType.JOINT_HEAD)
                        pos=head.getPosition()
                        lines.append(ax.plot([ pos[0]],[  pos[1]],[  pos[2]], 'bo')[0])
                        
                        head = user.getSkeleton().getJoint(JointType.JOINT_LEFT_HAND)
                        pos=head.getPosition()
                        lines.append(ax.plot([ pos[0]],[  pos[1]],[  pos[2]], 'go')[0])
                        
                        head = user.getSkeleton().getJoint(JointType.JOINT_RIGHT_HAND)
                        pos=head.getPosition()
                        lines.append(ax.plot([ pos[0]],[  pos[1]],[  pos[2]], 'ro')[0])
                        
                        head = user.getSkeleton().getJoint(JointType.JOINT_TORSO)
                        pos=head.getPosition()
                        lines.append(ax.plot([ pos[0]],[  pos[1]],[  pos[2]], 'ko')[0])
                        
                        #head = user.getSkeleton().getJoint(JointType.JOINT_HEAD)
                        #pos=head.getPosition()
                        #lines.append(ax.plot([ pos[0]],[  pos[1]],[  pos[2]], 'bo')[0])
                        
                        head = user.getSkeleton().getJoint(JointType.JOINT_LEFT_FOOT)
                        pos=head.getPosition()
                        lines.append(ax.plot([ pos[0]],[  pos[1]],[  pos[2]], 'co')[0])
                        
                        head = user.getSkeleton().getJoint(JointType.JOINT_RIGHT_FOOT)
                        pos=head.getPosition()
                        lines.append(ax.plot([ pos[0]],[  pos[1]],[  pos[2]], 'yo')[0])
                        
                        print("User {} : {}".format(uid, pos))
                        #lines.append(ax.plot([0, pos[0]],[0,  pos[1]],[0,  pos[2]])[0])
                    print  user.getSkeleton().getState()
                    
        
        
            #line,=ax.plot([0,random.randint(0,10)],[0,random.randint(0,10)],[0,random.randint(0,10)])
            #line2,=ax.plot([0,random.randint(0,10)],[0,random.randint(0,10)],[0,random.randint(0,10)])
            ax.clear()
            #ax.set_xlim3d([lims[0], lims[1]])
            #ax.set_ylim3d([lims[2], lims[3]])
            #ax.set_zlim3d([lims[4], lims[5]])
        #     line.set_ydata(random.randint(0,10))
        #     line.set_xdata([random.randint(0,10), random.randint(0,10)])
            
        #     line.set_ydata( [random.randint(0,10),random.randint(0,10)])  
            return lines

    ani = animation.FuncAnimation(fig, animate, np.arange(1, 10),   interval=20, blit=True)
    plt.show()
    sys.exit()
    

#console mode
import numpy as np
from nite2 import *

import time

# Test code -- print head coordinates of users

NiTE.initialize()

tracker = UserTracker()
tracker.create()

def USER_MESSAGE(m):
    print m

g_visibleUsers={}

g_skeletonStates={}

def updateUserState( user, ts):

        if user.isNew():
                USER_MESSAGE("New")
        elif (user.isVisible() and not g_visibleUsers[user.getId()]):
                USER_MESSAGE("Visible")
        elif (not user.isVisible() and g_visibleUsers[user.getId()]):
                USER_MESSAGE("Out of Scene")
        elif (user.isLost()):
                USER_MESSAGE("Lost")

        g_visibleUsers[user.getId()] = user.isVisible();


        #if (g_skeletonStates[user.getId()] != user.getSkeleton().getState()):
       
                #switch(g_skeletonStates[user.getId()] = user.getSkeleton().getState())
                #{
                #case nite::SKELETON_NONE:
                        #USER_MESSAGE("Stopped tracking.")
                        #break;
                #case nite::SKELETON_CALIBRATING:
                        #USER_MESSAGE("Calibrating...")
                        #break;
                #case nite::SKELETON_TRACKED:
                        #USER_MESSAGE("Tracking!")
                        #break;
                #case nite::SKELETON_CALIBRATION_ERROR_NOT_IN_POSE:
                #case nite::SKELETON_CALIBRATION_ERROR_HANDS:
                #case nite::SKELETON_CALIBRATION_ERROR_LEGS:
                #case nite::SKELETON_CALIBRATION_ERROR_HEAD:
                #case nite::SKELETON_CALIBRATION_ERROR_TORSO:
                        #USER_MESSAGE("Calibration Failed... :-|")
                        #break;
                #}
        #}
#}


while(True):
	f = tracker.readFrame()
	users=f.getUsers()
	#print users
	for uid in users:		
		
		user = f.getUserById(uid)
		uid=user.getId()
		updateUserState(user, f.getTimestamp());
		if user.isNew():
			print("New user id %d !" % uid)
			tracker.startSkeletonTracking(uid)
		
		elif user.getSkeleton().getState() == SkeletonState.SKELETON_TRACKED:
                    head = user.getSkeleton().getJoint(JointType.JOINT_HEAD)
                    rhand = user.getSkeleton().getJoint(JointType.JOINT_RIGHT_HAND)
                    print [head.getPosition(), rhand.getPosition()]
                    print("User {} : {}".format(uid, head.getPosition()))
		print  user.getSkeleton().getState()
		#else:
			#if user.isVisible():
				#head = user.getSkeleton().getJoint(JointType.JOINT_HEAD)
				#print("User {} : {}".format(uid, head.getPosition()))
			









tracker.destroy()
NiTE.shutdown()




