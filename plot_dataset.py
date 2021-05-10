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

df_duration = pd.DataFrame()
for name in ['train', 'test']:
    df = pd.read_csv(f"data_urbansed/flists/urban_sed_{name}_strong.tsv", sep='\t', header=0)
    df1 = df.groupby(by='filename', as_index=False).agg({'event_label': pd.Series.count})
    list1 = list(df1["event_label"])
    min_event = min(list1)
    max_event = max(list1)
    df2 = np.histogram(list1, bins=int(max_event-min_event+1), range=(min_event-.5, max_event+.5))
    df3 = pd.DataFrame(
        {'# Events': np.sort(np.unique(list1)), '# Clips': df2[0]})
    df3.to_csv(f"figs/event_clip_{name}.csv")

    df["Duration (s)"] = df['offset'] - df['onset']
    df["Set"] = name.capitalize()
    df_duration = df_duration.append(df)
    

df_duration["Label"] = df_duration["event_label"].map(lambda s:s.split("_")[0].capitalize())
df_duration.to_csv("figs/duration.csv")

# plot event vs clip
w = 244 / 72. 
h = (244//2+10) / 72.
f, ax = plt.subplots(1, 1, figsize=(w, h), sharex=True)

df = pd.read_excel("figs/event_clip.xlsx", engine='openpyxl')
splot = sns.barplot(
    x="# Events", y="# Clips", hue="Set", 
    data=df, 
    palette="Set2", ax=ax)
for p in splot.patches:
    splot.annotate(
        format(p.get_height(), '.0f'), 
        (p.get_x() + p.get_width() / 2., p.get_height()), 
        ha = 'center', va = 'center', 
        xytext = (0, 5), 
        textcoords = 'offset points')
ax.legend(loc='lower center', bbox_to_anchor=(0.5, 1.05), ncol=2)

ax.yaxis.set_major_locator(ticker.MultipleLocator(200))
plt.tight_layout()
plt.savefig("figs/event_clip.png")
plt.savefig("figs/event_clip.eps")

# plot duration
w = 244 / 72. 
h = (244+20) / 72.
f, ax = plt.subplots(1, 1, figsize=(w, h), sharex=True)

df = pd.read_csv("figs/duration.csv")
flierprops = dict(
    marker='o', markerfacecolor='k', markersize=1.5,
    linestyle='none', markeredgecolor='k')
sns.boxplot(
    x="Duration (s)", y="Label", hue="Set", 
    width=.8,
    linewidth=.5,
    flierprops=flierprops,
    data=df, 
    palette="Set2",
    ax=ax)

ax.legend(loc='lower center', bbox_to_anchor=(0.5, 1.01), ncol=2)
ax.yaxis.label.set_visible(False)
plt.xlim(0, 10)
plt.yticks(rotation=45)
plt.tight_layout()
plt.savefig("figs/duration.png")
plt.savefig("figs/duration.eps")