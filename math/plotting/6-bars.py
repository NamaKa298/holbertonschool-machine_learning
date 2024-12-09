#!/usr/bin/env python3
"""6. Stacking Bars"""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """Trace un histogramme de répartition\\
        de quantité de plusieurs fruit en fonction de l'individu"""
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))

    personnes = (
        "Farrah",
        "Fred",
        "Felicia"
    )
    type_de_fruits = {
        "apples": fruit[0, :],
        "bananas": fruit[1, :],
        "oranges": fruit[2, :],
        "peaches": fruit[3, :]
    }
    width = 0.5

    fig, ax = plt.subplots()
    bottom = np.zeros(3)
    bar_colors = {'apples': 'red', 'bananas': 'yellow',
                  'oranges': '#ff8000', 'peaches': '#ffe5b4'}
    for fruit_name, qtt_de_fruits in type_de_fruits.items():
        ax.bar(personnes, qtt_de_fruits, width, label=fruit_name,
               bottom=bottom, color=bar_colors[fruit_name])
        bottom += qtt_de_fruits
    plt.ylim(0, 80)
    ax.set_title('Number of Fruit per Person')
    ax.set_ylabel('Quantity of Fruit')
    ax.legend(type_de_fruits)
    plt.savefig('bars.png')
