import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#this would be income brackets 1-7
labels = ['1','2','3', '4', '5', '6', '7']

f= open("NumberZipsPerBracket2019.txt")
g= open("NumberZipsPerBracket2020.txt")
comp2019= f.readlines()
comp2020= g.readlines()
companies2019=[]
companies2020=[]
#getting rid of the new lines and converting the data to integers
for item in comp2019:
    item=item.strip()
    item= int(item)
    companies2019.append(item)

for comp in comp2020:
    comp= comp.strip()
    comp= int(comp)
    companies2020.append(comp)
f.close()
g.close()

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, companies2019, width, label='2019')
rects2 = ax.bar(x + width/2, companies2020, width, label='2020')

# labels, title 
ax.set_ylabel('Companies Incorporated')
ax.set_xlabel('Income Bracket')
ax.set_title('Companies Incorporated by Income Bracket and Year')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()


#saving as pdf 
fig.savefig("graph.pdf")
