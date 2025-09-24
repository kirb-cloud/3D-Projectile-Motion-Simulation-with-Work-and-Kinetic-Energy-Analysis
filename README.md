# 3D-Projectile-Motion-Simulation-with-Work-and-Kinetic-Energy-Analysis
This project simulates the motion of two projectiles in a 3D environment using VPython 3.2. The simulation calculates and visualizes the kinetic energy and work done on each object over time. This program demonstrates fundamental physics concepts such as projectile motion, momentum, and energy transformations.

## Features
- 3D visualization of projectiles with **trails**.
- Real-time calculations of:
  - **Momentum** (`p = m * v`)
  - **Velocity** (`v = p / m`)
  - **Kinetic Energy** (`KE = |p|^2 / (2 * m)`)
  - **Work Done** (`W = Σ F · v dt`)
  - **Change in Kinetic Energy** (`ΔKE = KE - KE0`)
- Interactive graphs:
  - Work vs Time
  - Change in Kinetic Energy vs Time

## Equations Used

**Momentum:**  
`p = m * v`  

**Velocity from Momentum:**  
`v = p / m`  

**Kinetic Energy (KE):**  
`KE = |p|^2 / (2 * m)`  

**Work Done:**  
`W = Σ F · (v * dt)`  

**Change in Kinetic Energy:**  
`ΔKE = KE - KE0`  

**Gravitational Force on object A:**  
`FA = m * g`  

**Constant Upward Force on object B:**  
`FB = m`  

## Simulation Setup

- **Projectiles:**
  - Mass = `0.5 kg`
  - Radius = `0.2 m`
  - Initial velocity = `5 m/s` at `45°` angle
- **Ground object:** height = `0.2 m`, width = `3 m`, white color
- **Time step:** `dt = 0.001 s`

## How It Works

1. **Initialization**
   - Define constants (mass, gravity, initial position, velocity).
   - Create VPython `sphere` objects for the projectiles with trails.
   - Initialize momentum, velocity, kinetic energy, and work.

2. **Time Evolution (Loop)**
   - Update momentum using the applied force:  
     `p = p + F * dt`
   - Compute velocity from updated momentum:  
     `v = p / m`
   - Update projectile position:  
     `pos = pos + v * dt`
   - Calculate current kinetic energy:  
     `KE = |p|^2 / (2 * m)`
   - Update work done:  
     `W += F · (v * dt)`
   - Compute change in kinetic energy:  
     `ΔKE = KE - KE0`

3. **Graph Updates**
   - Plot **Work** vs **Time**
   - Plot **Change in Kinetic Energy** vs **Time**

4. **Iteration**
   - Continue until the projectile hits the ground (`y <= 0`)
   - All graphs and projectile positions are continuously updated
