import time
from interbotix_xs_modules.arm import InterbotixManipulatorXS
from interbotix_perception_modules.armtag import InterbotixArmTagInterface
from interbotix_perception_modules.pointcloud import InterbotixPointCloudInterface

# This script uses a color/depth camera to get the arm to find objects and pick them up.
# For this demo, the arm is placed to the left of the camera facing outward. When the
# end-effector is located at x=0, y=-0.3, z=0.2 w.r.t. the 'wx200/base_link' frame, the AR
# tag should be clearly visible to the camera. A small basket should also be placed in front of the arm.
#
# To get started, open a terminal and type 'roslaunch interbotix_xsarm_perception xsarm_perception.launch robot_model:=wx200'
# Then change to this directory and type 'python pick_place.py'

global block
global level
global height
# Initialize the arm module along with the pointcloud and armtag modules
bot = InterbotixManipulatorXS("vx300s", moving_time=2, accel_time=1.5)
pcl = InterbotixPointCloudInterface()
block=1
level=1
height=0

def odd_level(x,y,z):
    if block==1:
        bot.arm.set_ee_pose_components(x=x, y=y, z=z+0.06, pitch=1.5)
        # bot.arm.set_ee_pose_components(x=x, y=y, z=z, pitch=0.5)
        bot.gripper.close()
        bot.arm.set_ee_pose_components(x=0.3, z=0.2, pitch=1.5)
        # bot.arm.set_ee_pose_components(x=x, y=y, z=z+0.05, pitch=1.5)
        bot.arm.set_ee_pose_components(x=0.35, y=-0.24, z=0.05+height, pitch=1.5)#target coordinates
        bot.gripper.open()
        bot.arm.set_ee_pose_components(x=0.35, y=-0.24, z=0.2, pitch=1.5)
        bot.arm.set_ee_pose_components(x=0.3, z=0.2)
        block=block+1
    else:
        bot.arm.set_ee_pose_components(x=x, y=y, z=z+0.06, pitch=1.5)
        # bot.arm.set_ee_pose_components(x=x, y=y, z=z, pitch=0.5)
        bot.gripper.close()
        bot.arm.set_ee_pose_components(x=0.3, z=0.2, pitch=1.5)
        bot.arm.set_ee_pose_components(x=0.4, y=-0.18 , z=0.05+height, roll=0.25, pitch=1.5)
        bot.gripper.open()
        bot.arm.set_ee_pose_components(x=0.37, y=-0.15, z=0.2, pitch=1.5)
        bot.arm.set_ee_pose_components(x=0.3, z=0.2)
        block=1
        level=level+1
        height=height+0.03

def even_level(x,y,z):
    if block==1:
        bot.arm.set_ee_pose_components(x=x, y=y, z=z+0.06, pitch=1.5)
        # bot.arm.set_ee_pose_components(x=x, y=y, z=z, pitch=0.5)
        bot.gripper.close()
        bot.arm.set_ee_pose_components(x=0.3, z=0.2,roll=-1.45, pitch=1.5)
        # bot.arm.set_ee_pose_components(x=x, y=y, z=z+0.05, pitch=1.5)
        bot.arm.set_ee_pose_components(x=0.38, y=-0.22, z=0.05+height,roll=-1.45, pitch=1.5)#target coordinates
        bot.gripper.open()
        bot.arm.set_ee_pose_components(x=0.38, y=-0.22, z=0.2,roll=-1.45, pitch=1.5)
        bot.arm.set_ee_pose_components(x=0.3, z=0.2)
        block=block+1
    else:
        bot.arm.set_ee_pose_components(x=x, y=y, z=z+0.06, pitch=1.5)
        # bot.arm.set_ee_pose_components(x=x, y=y, z=z, pitch=0.5)
        bot.gripper.close()
        bot.arm.set_ee_pose_components(x=0.3, z=0.2, pitch=1.5)
        bot.arm.set_ee_pose_components(x=0.33, y=-0.19 , z=0.05+height, roll=-1.45, pitch=1.5)#change coordinates
        # bot.arm.set_ee_pose_components(x=x, y=y, z=z+0.05, pitch=1.5)
        # bot.arm.set_ee_pose_components(x=0.35, y=-0.24, z=0.05+i, pitch=1.5)
        bot.gripper.open()
        bot.arm.set_ee_pose_components(x=0.33, y=-0.19 , z=0.2, roll=-1.45, pitch=1.5)
        bot.arm.set_ee_pose_components(x=0.3, z=0.2)
        block=1
        level=level+1
        height=height+0.03


def main():
    
    # armtag = InterbotixArmTagInterface()

    # set initial arm and gripper pose
    bot.arm.set_ee_pose_components(x=0.3, z=0.2)
    bot.gripper.open()

    # get the ArmTag pose
    # bot.arm.set_ee_pose_components(y=-0.3, z=0.2)
    # time.sleep(0.5)
    # armtag.find_ref_to_arm_base_transform()
    # bot.arm.set_ee_pose_components(x=0.3, z=0.2)

    # get the cluster positions
    # sort them from max to min 'x' position w.r.t. the 'wx200/base_link' frame
    success, clusters = pcl.get_cluster_positions(ref_frame="vx300s/base_link", sort_axis="x", reverse=True)
    
    
    
    # print(i)
    # pick up all the objects and drop them in a virtual basket in front of the robot
    for cluster in clusters:
        x, y, z = cluster["position"]
        if level%2!=0:
            odd_level(x,y,z)
        else:
            even_level(x,y,z)  
    bot.arm.go_to_sleep_pose()

if __name__=='__main__':
    
    main()