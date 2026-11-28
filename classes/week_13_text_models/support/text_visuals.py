"""Иллюстрации к занятию о текстовых моделях."""
import matplotlib.pyplot as plt
import numpy as np


def plot_memory_trace(characters, gates, memory, coordinate):
    fig, axes = plt.subplots(2, 1, figsize=(9, 4.2), sharex=True,
                             layout="constrained", height_ratios=[1, 1.1])
    image = axes[0].imshow(gates.T, vmin=0, vmax=1, cmap="GnBu", aspect="auto")
    axes[0].set_yticks([0, 1, 2], ["запись i", "перенос f", "чтение o"])
    fig.colorbar(image, ax=axes[0], ticks=[0, .5, 1], shrink=.85)
    axes[1].plot(np.arange(len(memory)), memory, "o-", color="#245868")
    axes[1].axhline(0, color="grey", lw=.7)
    axes[1].set_xticks(range(len(characters)), list(characters.replace(" ", "·").replace("\n", "↵")))
    axes[1].set(xlabel="Прочитанный символ", ylabel="Память c")
    axes[0].set_title(f"Одна координата обученной LSTM: {coordinate}", loc="left")
    axes[1].set_xlim(-.5, len(memory)-.5)
    plt.show()
