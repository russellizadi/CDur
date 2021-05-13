import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns 
import matplotlib as mpl

sns.set_theme(style="whitegrid")
sns.set_style({'font.family': 'Times New Roman'})
SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=SMALL_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('legend', title_fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=SMALL_SIZE)  # fontsize of the figure title

mpl.rcParams['xtick.major.pad'] = -2
mpl.rcParams['ytick.major.pad'] = -2
mpl.rcParams["text.color"] = "black"



w = 244 / 72. 
h = (244//3+10) / 72.


def fig4301(
    x, 
    fig_w, fig_h, 
    path_fig=None, 
    verbose=False
    ):

    fig = plt.figure(figsize=(fig_w, fig_h), tight_layout=True)
    
    ax = sns.heatmap(
        x.T[::-1], 
        cbar=True,
        cbar_kws={"pad": .02},
        linewidths=0.0,
        rasterized=True,
        cmap="magma", #"cubehelix" #"viridis"
    )
    ax.collections[0].colorbar.ax.tick_params(length=0, pad=1)
    ax.tick_params(
        left=False, 
        bottom=False, 
        length=1,
        pad=1,
        width=1, 
    )

    xticks = ax.get_xticks()
    xticks = np.around(np.linspace(0, 500, 11), decimals=0).astype(int)
    xticklabels = np.around(np.linspace(0, 10, len(xticks)), decimals=0).astype(int)
    import librosa
    yticks = np.around(np.linspace(0, 64, 5), decimals=0).astype(int)[:-1]
    yticklabels = np.around(
        librosa.mel_frequencies(64)[np.linspace(0, 63, 5).astype(int)]/1000, 
        decimals=0).astype(int)[::-1][:-1]
    ax.set(
        title=None,
        xlabel="Time (s)",
        xticks=xticks, 
        xticklabels=xticklabels,
        ylabel="Frequency (kHz)",
        yticks=yticks,
        yticklabels=yticklabels, 
    )
    ax.xaxis.set_tick_params(rotation='auto')
    ax.yaxis.set_tick_params(rotation='auto')
    plt.tight_layout()
    if path_fig:
        plt.savefig(path_fig)
    if verbose:
        plt.show(block=False)
    plt.close(fig)

for i in range(10):    
    data = np.load(f"figs/spc-{i}.npz")
    spc = data["spc"]
    filename = data["filename"]

    fig4301(spc, w, h, f"figs/spc-{i}.png")
    fig4301(spc, w, h, f"figs/spc-{i}.eps")