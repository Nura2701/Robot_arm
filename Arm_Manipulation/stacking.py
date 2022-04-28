import time
from interbotix_xs_modules.arm import InterbotixManipulatorXS
from interbotix_perception_modules.armtag import InterbotixArmTagInterface
from interbotix_perception_modules.pointcloud import InterbotixPointCloudInterface

bot = InterbotixManipulatorXS("vx300s", moving_time=1.5, accel_time=0.75)
pcl = InterbotixPointCloudInterface()

def odd_layer(x,y,z):
    bot.arm.set_ee_pose_components(x=x, y=y, z=z+0.05, pitch=0.5)
    # bot.arm.set_ee_pose_components(x=x, y=y, z=z, pitch=0.5)
    bot.gripper.close()
    bot.arm.set_ee_pose_components(x=0.3, y=0.24, z=0.06, pitch=1.55,roll=1.3) #some x,y,z coordinates
    # bot.arm.set_ee_pose_components(x=0.3, z=0.2)
    bot.gripper.open()

def even_block(x,y,z):
    bot.arm.set_ee_pose_components(x=x, y=y, z=z+0.05, pitch=0.5)
    bot.arm.set_ee_pose_components(x=x, y=y, z=z, pitch=0.5)
    bot.gripper.close()
    bot.arm.set_ee_pose_components(x=0.35, y=0.24, z=0.06, pitch=1.55,roll=1.3) #some x,y,z coordinates
    # bot.arm.set_ee_pose_components(x=0.3, z=0.2)
    bot.gripper.open()

# def even_layer():

def main():
    # Initialize the arm module along with the pointcloud and armtag modules
   
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
    counter=0
    print(clusters[0])
    layer=1
    block=1

    for cluster in clusters:
        # if layer%2!=0:
            if block == 1:
                x, y, z = cluster["position"]
                odd_layer(x,y,z)
                block+=1
            else:
                x, y, z = cluster["position"]
                even_block(x,y,z)
                block=1
            
        # else:
            # if block == 1:
            #     x, y, z = cluster["position"]
            #     odd_layer(x,y,z)
            # else:
            #     x, y, z = cluster["position"]
            #     odd_layer(x,y+3,z)




    # for cluster in clusters:

    #     # counter=counter+1
    #     x, y, z = cluster["position"]
    #     if counter%2==0:
    #         odd_layer()
    #     else:
    #         even_layer()

    #     bot.arm.set_ee_pose_components(x=x, y=y, z=z+0.05, pitch=0.5)
    #     bot.arm.set_ee_pose_components(x=x, y=y, z=z, pitch=0.5)
    #     bot.gripper.close()
    #     bot.arm.set_ee_pose_components(x=x, y=y, z=z+0.05, pitch=0.5)
    #     bot.arm.set_ee_pose_components(x=0.3, z=0.2)
    #     bot.gripper.open()
    # bot.arm.go_to_sleep_pose()

if __name__=='__main__':
    main()