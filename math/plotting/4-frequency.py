#!/usr/bin/env python3
"""4. Frequency"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """Trace un histogramme"""
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    plt.ylim(0, 30)
    plt.xlim(0, 100)
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.title('Project A')
    plt.hist(student_grades, bins=10, edgecolor='k')
    plt.xticks(np.arange(0, 101, 10))
    plt.savefig('frequency.png')
