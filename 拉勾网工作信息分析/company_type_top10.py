from pyecharts import Bar
import dy

df = dy.con_sql('job')

place_message = df.groupby(['company_type'])
place_com = place_message['company_type'].agg(['count'])
place_com.reset_index(inplace=True)
place_com_last = place_com.sort_index()
dom = place_com_last.sort_values('count', ascending=False)[0:10]

attr = dom['company_type']
v1 = dom['count']
bar = Bar("拉勾网数据分析岗—公司类型TOP10", title_pos='center', title_top='18', width=800, height=400)
bar.add("", attr, v1, is_convert=True, xaxis_min=0, yaxis_rotate=30, yaxis_label_textsize=10, is_yaxis_boundarygap=True, yaxis_interval=0, is_label_show=True, is_legend_show=False, label_pos='right', is_yaxis_inverse=True, is_splitline_show=False)
bar.render("拉勾网数据分析岗—公司类型TOP10.html")