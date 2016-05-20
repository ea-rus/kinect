#!/usr/bin/python
# -*- coding: utf-8 -*-


from nite2 import *

import time

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
                    print("User {} : {}".format(uid, head.getPosition()))
		print  user.getSkeleton().getState()
		#else:
			#if user.isVisible():
				#head = user.getSkeleton().getJoint(JointType.JOINT_HEAD)
				#print("User {} : {}".format(uid, head.getPosition()))
			

tracker.destroy()
NiTE.shutdown()
