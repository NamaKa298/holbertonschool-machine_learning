#!/usr/bin/env python3
"""Plots a line graph of y = x^3"""
import numpy as np
import matplotlib.pyplot as plt


def line():
    """Plots a line graph of y = x^3"""
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))
    plt.xlim(0, 10)
    plt.plot(y, color='red')
    plt.savefig('line_plot.png')  # Enregistre la figure dans un fichier
    plt.show()
