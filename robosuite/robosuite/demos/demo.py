import numpy as np
import robosuite as suite

# create environment instance
env = suite.make(
    env_name="Door", # try with other tasks like "Stack" and "Door"
    robots="Panda",  # try with other robots like "Sawyer" and "Jaco"
    has_renderer=False,  # Set to False for headless mode (no visible window)
    has_offscreen_renderer=True,  # Keep True for camera observations
    use_object_obs=False, 
    use_camera_obs=True,
    camera_names="agentview",  # Must be a list of camera names
    camera_heights=84, # image height
    camera_widths=84, # image width
)

# reset the environment
env.reset()

for i in range(5000):
    action = np.random.randn(*env.action_spec[0].shape) * 0.1
    obs, reward, done, info = env.step(action)  # take action in the environment
    
    if (i%1000 == 0):
        image = obs["agentview_image"]
        print(image.shape)
        print(image.dtype)
        joint_pos = obs["robot0_joint_pos"]
        print(joint_pos.shape)
        print(joint_pos.dtype)
    # env.render()  # render on display