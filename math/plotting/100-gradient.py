#!/usr/bin/env python3
"""7. Gradient"""
import numpy as np
import matplotlib.pyplot as plt


def gradient():
    """Trace un nuage de points avec gradient en fonction de la hauteur"""
    np.random.seed(5)

    x = np.random.randn(2000) * 10
    y = np.random.randn(2000) * 10
    z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))
    plt.figure(figsize=(6.4, 4.8))

    plt.xlabel('x coordinate (m)')
    plt.ylabel('y coordinate (m)')
    plt.title('Mountain Elevation')
    plt.scatter(x, y, c=z, cmap='viridis')
    plt.colorbar().set_label('elevation (m)')
    plt.savefig('gradient.png')
