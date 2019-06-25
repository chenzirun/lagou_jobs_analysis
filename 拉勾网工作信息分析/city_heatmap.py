from pyecharts import Geo
import dy

df = dy.con_sql('job')

# 分组, 计数, 重设索引, 排序
city_message = df.groupby(['job_city'])
city_com = city_message['job_city'].agg(['count'])
city_com.reset_index(inplace=True)
city_com_last = city_com.sort_index()

geo = Geo("拉勾网数据分析岗—城市分布热力图", title_pos='center', title_top='0', width=1200, height=600, title_color="#fff", background_color="#404a59",)
attr = city_com_last['job_city']
value = city_com_last['count']
geo.add("", attr, value, type="heatmap", is_visualmap=True, visual_range=[0, 30], visual_text_color="#fff", is_label_show=True)
geo.render('拉勾网数据分析岗—城市分布图.html')