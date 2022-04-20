from interbotix_xs_modules.arm import InterbotixManipulatorXS
import numpy as np

def main():
    bot = InterbotixManipulatorXS("vx300s", "arm", "gripper")
    bot.arm.set_ee_pose_components(x=0.3, z=0.2)
    bot.arm.set_single_joint_position("waist", np.pi/3.0)
    bot.arm.set_ee_cartesian_trajectory(x=-0.1, z=0.16)
    bot.arm.set_single_joint_position("waist", -np.pi/2.0)
    bot.arm.set_ee_cartesian_trajectory(pitch=1.5)
    bot.arm.set_ee_cartesian_trajectory(pitch=-1.5)
    bot.arm.set_single_joint_position("waist", np.pi/2.0)
    bot.arm.set_ee_pose_components(x=0.3, z=0.2)
    

if __name__=='__main__':
    main()