#!/usr/bin/env python3
""" 5. All in One"""
import numpy as np
import matplotlib.pyplot as plt


def all_in_one():
    """Regroupe plusieurs graphiques ensembles"""
    y0 = np.arange(0, 11) ** 3

    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
    y1 += 180

    x2 = np.arange(0, 28651, 5730)
    r2 = np.log(0.5)
    t2 = 5730
    y2 = np.exp((r2 / t2) * x2)

    x3 = np.arange(0, 21000, 1000)
    r3 = np.log(0.5)
    t31 = 5730
    t32 = 1600
    y31 = np.exp((r3 / t31) * x3)
    y32 = np.exp((r3 / t32) * x3)

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)

    plt.figure(1)

    # Premier graphique (ligne)
    graph1 = plt.subplot2grid((3, 2), (0, 0), colspan=1, rowspan=1)
    graph1.plot(y0, color='red')

    # Deuxième graphique (nuage de points)
    graph2 = plt.subplot2grid((3, 2), (0, 1), colspan=1, rowspan=1)
    graph2.set_title("Men's Height vs Weight", fontsize='x-small')
    graph2.set_xlabel('Height (in)', fontsize='x-small')
    graph2.set_ylabel('Weight (lbs)', fontsize='x-small')
    graph2.scatter(x1, y1, c='m')

    # Troisième graphique (changement d'échelle)
    graph3 = plt.subplot2grid((3, 2), (1, 0), colspan=1, rowspan=1)
    graph3.set_title('Exponential Decay of C-14', fontsize='x-small')
    graph3.set_xlabel('Time (years)', fontsize='x-small')
    graph3.set_ylabel('Fraction Remaining', fontsize='x-small')
    graph3.semilogy(x2, y2)

    # Quatrième graphique (deux courbes)
    graph4 = plt.subplot2grid((3, 2), (1, 1), colspan=1, rowspan=1)
    graph4.set_title('Exponential Decay of Radioactive Elements',
                     fontsize='x-small')
    graph4.set_xlabel('Time (years)', fontsize='x-small')
    graph4.set_ylabel('Fraction Remaining', fontsize='x-small')
    graph4.plot(x3, y31, linestyle='--', c='r', label='C-14')
    graph4.plot(x3, y32, c='g', label='Ra-226')

    # Cinquième graphique (histogramme)
    graph5 = plt.subplot2grid((3, 2), (2, 0), colspan=2, rowspan=1)
    graph5.set_ylim(0, 30)
    graph5.hist(student_grades, bins=range(0, 101, 10), edgecolor='k')
    graph5.set_title('Project A', fontsize='x-small')
    graph5.set_xlabel('Grades', fontsize='x-small')
    graph5.set_ylabel('Number of Students', fontsize='x-small')
    graph5.set_xticks(np.arange(0, 101, 10))
    graph5.set_xlim(0, 100)
    plt.tight_layout()
    plt.suptitle('All in One')
    plt.savefig('all_in_one.png')
    plt.close()
