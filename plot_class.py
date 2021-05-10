import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns 
import matplotlib as mpl

font_paths = mpl.font_manager.findSystemFonts()
font_objects = mpl.font_manager.createFontList(font_paths)
font_names = [f.name for f in font_objects]
#print(font_names)
#sns.set_style({'font.family':'serif', 'font.serif':['Times New Roman']})


df = pd.read_excel("figs/class.xlsx", engine='openpyxl')

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

w = 504 / 72. 
h = (244+10) / 72.

# Set up the matplotlib figure
f, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(w, h), sharex=True)

splot = sns.barplot(
    x="Label", y="F1", hue="Method", 
    data=df[df["Eval"] == "Tagging"],
    palette="husl", ax=ax1)
for p in splot.patches:
    splot.annotate(
        format(100*p.get_height(), '.0f'), 
        (p.get_x() + p.get_width() / 2., p.get_height()), 
        ha = 'center', va = 'center', 
        xytext = (0, 5), 
        textcoords = 'offset points')
ax1.xaxis.label.set_visible(False)
ax1.set(ylabel="Tagging-F1")
ax1.legend(loc='lower center', bbox_to_anchor=(0.5, 1.05), ncol=3)

splot = sns.barplot(
    x="Label", y="F1", hue="Method", 
    data=df[df["Eval"] == "Segment"], 
    palette="husl", ax=ax2)
for p in splot.patches:
    splot.annotate(
        format(100*p.get_height(), '.0f'), 
        (p.get_x() + p.get_width() / 2., p.get_height()), 
        ha = 'center', va = 'center', 
        xytext = (0, 5), 
        textcoords = 'offset points')
ax2.xaxis.label.set_visible(False)
ax2.set(ylabel="Segment-F1")
ax2.get_legend().remove()

splot = sns.barplot(
    x="Label", y="F1", hue="Method", 
    data=df[df["Eval"] == "Event"], 
    palette="husl", ax=ax3)
for p in splot.patches:
    splot.annotate(
        format(100*p.get_height(), '.0f'), 
        (p.get_x() + p.get_width() / 2., p.get_height()), 
        ha = 'center', va = 'center', 
        xytext = (0, 5), 
        textcoords = 'offset points')
ax3.xaxis.label.set_visible(False)
ax3.set(ylabel="Event-F1")
ax3.get_legend().remove()

plt.xticks(rotation=45)

for ax in [ax1, ax2, ax3]:
    ax.yaxis.set_major_locator(ticker.MultipleLocator(.25))
    ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1., decimals=0))

plt.tight_layout()
plt.savefig("figs/class.png")
plt.savefig("figs/class.eps")
print(df.head())
