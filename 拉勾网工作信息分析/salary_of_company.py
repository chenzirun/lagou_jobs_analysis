from pyecharts import Boxplot
import dy

df = dy.con_sql('job')

dom22 = []
for i in df['company_people']:
    if i in dom22:
        continue
    else:
        dom22.append(i)

dom = df[['company_people', 'job_salary']]
data = [[], [], [], [], []]
dom1, dom2, dom3, dom4, dom5 = data
for i, j in zip(dom['company_people'], dom['job_salary']):
    j = ((float(j.split('-')[0].replace('k', '').replace('K', '')) + float(j.split('-')[1].replace('k', '').replace('K', ''))) / 2) * 1000
    if i in ['15-50人']:
        dom1.append(j)
    elif i in ['50-150人']:
        dom2.append(j)
    elif i in ['150-500人']:
        dom3.append(j)
    elif i in ['500-2000人']:
        dom4.append(j)
    else:
        dom5.append(j)

boxplot = Boxplot("拉勾网数据分析岗—公司规模薪水图(元/月)", title_pos='center', title_top='18', width=1200, height=600)
boxplot.use_theme("chalk")
x_axis = ['15-50人', '50-150人', '150-500人', '500-2000人', '2000人以上']
y_axis = [dom1, dom2, dom3, dom4, dom5]
_yaxis = boxplot.prepare_data(y_axis)
boxplot.add("", x_axis, _yaxis)
boxplot.render("拉勾网数据分析岗—公司规模薪水图.html")
