# 🦾 Soft Robotic Gait Optimization

This project explores machine-learning-driven gait optimization for an untethered soft robot that uses electromagnetic pulses to move. The robot is built with silicone legs embedded with permanent magnets, and its forward locomotion depends on the precise timing and coordination of these magnetic actuation signals.

A fully-connected PyTorch regression model is trained to learn the relationship between three actuation parameters—two leg pulse widths and a waveform offset—and the resulting forward velocity of the robot. The model uses a multilayer architecture and is optimized using the Adam optimizer with mean-squared error loss. By training on sampled actuation patterns and their resulting speeds, the system learns a mapping from inputs to outputs.

The long-term goal is to run this model live while the robot is walking. The robot will communicate via WiFi with an external computer, which will continuously infer improved actuation parameters and send them back to the robot in real time. This will allow the robot to automatically adapt its gait to different surfaces and continually optimize its locomotion speed without manual tuning.
