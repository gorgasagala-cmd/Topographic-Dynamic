# Topographic-Dynamic

Dynamic topographic wallpaper generator using Python.  
This program creates a real-time animated topographic contour display that adapts to your screen resolution.

## Preview
The animation shows white contour lines on a black background, with smooth circular wave patterns that continuously evolve.

## Features
- Borderless fullscreen display
- Automatic screen resolution detection
- Real-time animation (≈30 FPS)
- Dynamic topographic patterns based on mathematical functions
- Lightweight and easy to run

## How It Works
The program builds a 2D grid using NumPy, then computes height values (Z) based on distances from multiple moving center points.

Core concepts:
- Uses sine and cosine functions
- Computes Euclidean distance
- Combines multiple wave layers for complex patterns

The result is rendered using Matplotlib contour plots.

## Requirements
Install the following dependencies:

```bash
pip install matplotlib numpy screeninfo
