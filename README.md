# 3D-Projectile-Motion-Simulation-with-Work-and-Kinetic-Energy-Analysis
This project simulates the motion of two projectiles in a 3D environment using VPython 3.2. The simulation calculates and visualizes the kinetic energy and work done on each object over time. This program demonstrates fundamental physics concepts such as projectile motion, momentum, and energy transformations.

# 3D Projectile Motion Simulation with Work and Kinetic Energy Analysis

## Overview

This project simulates the motion of two projectiles in a 3D environment using **VPython 3.2**. The simulation calculates and visualizes the **kinetic energy** and **work done** on each object over time. This program demonstrates fundamental physics concepts such as projectile motion, momentum, and energy transformations.

## Features

- **3D visualization** of two projectiles using spheres (`objectA` and `objectB`).  
- Calculation of **momentum**, **kinetic energy**, and **work** for each projectile.  
- Interactive **graphs** to track:
  - Work on the system over time.
  - Change in kinetic energy over time.  
- Real-time simulation with adjustable time step for accurate motion dynamics.

## Physics Implemented

1. **Projectile motion equations** with gravitational force:
   - \( \vec{F}_A = m \cdot \vec{g} \) downward  
   - \( \vec{F}_B \) can be modified (example: upward force vector)
2. **Momentum update** using:  
   \[
   \vec{p}_{\text{new}} = \vec{p}_{\text{old}} + \vec{F} \cdot dt
   \]
3. **Velocity update** from momentum:
   \[
   \vec{v} = \frac{\vec{p}}{m}
   \]
4. **Position update** using velocity:
   \[
   \vec{x}_{\text{new}} = \vec{x}_{\text{old}} + \vec{v} \cdot dt
   \]
5. **Kinetic energy**:  
   \[
   KE = \frac{1}{2} m |\vec{v}|^2
   \]
6. **Work done by a force**:
   \[
   W += \vec{F} \cdot \Delta \vec{x}
   \]


