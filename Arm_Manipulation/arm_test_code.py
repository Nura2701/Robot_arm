from interbotix_xs_modules.arm import InterbotixManipulatorXS
import numpy as np

def main():
    bot = InterbotixManipulatorXS("vx300s", "arm", "gripper")
    # bot.arm.set_ee_pose_components(x=0.35, y=-0.23, z=0.3)#x=0.3, y=0.24, z=0.06, pitch=1.5,pitch=1.55,roll=1.3) # moves end effector to the coordinate
    # bot.arm.set_ee_pose_components(x=0.35, y=-0.24, z=0.12, pitch=1.5)
    # bot.arm.set_ee_pose_components(x=0.4, y=-0.18 , z=0.2, roll=0.25, pitch=1.5)
    # bot.arm.set_ee_pose_components(x=0.38, y=-0.22, z=0.05,roll=-1.45, pitch=1.5)
    # bot.arm.set_ee_pose_components(x=x, y=y, z=z+0.06, pitch=1.5)
    bot.arm.go_to_sleep_pose()
    # bot.arm.set_ee_pose_components(x=0.15, z=0.2,pitch=1.5)
    # bot.gripper.close()
    # bot.gripper.open()
    # bot.arm.set_single_joint_position("wrist", np.pi/4.0)
    # bot.arm.set_ee_cartesian_trajectory(x=-0.1, z=0.16)
    # bot.arm.set_single_joint_position("wrist_angle", np.pi/3.0)
    # bot.arm.set_single_joint_position("wrist_rotate", np.pi/2.0)
    # bot.arm.set_single_joint_position("elbow", 0)
    # bot.arm.set_ee_cartesian_trajectory(pitch=1.5)
    # bot.arm.set_ee_cartesian_trajectory(pitch=-1.5)
    # bot.arm.set_single_joint_position("waist", np.pi/2.0)
    # bot.arm.set_ee_pose_components(x=0.3, z=0.2)
    

if __name__=='__main__':
    main()