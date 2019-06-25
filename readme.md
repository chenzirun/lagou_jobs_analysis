# 拉勾网数据分析职业分析报告
**摘要**
1.分析动机:学习数据分析相关知识之后，学到不少知识，准备开始找工作。在这之前想自己做一个实战，一是能够证明自己确实做了准备，初步具备数据分析师岗位的能力，二是通过实战复习自己所学知识，熟悉数据分析流程。三是，从自己想从事的数据分析职位入手分析，也能够借此了解数据分析师的收入情况. 判断自己的学历、工作经验是否符合数据分析师的要求, 知晓哪些公司招聘需求高, 哪个城市、哪个领域较为需要数据分析师.
2.分析过程, 使用了爬虫爬取拉勾网数据分析职位的信息,共450条. 收集了以下字段的信息
> 职业名称, job_title
> 薪水, job_salary
> 城市, job_city
> 工作经验, job_experience
> 教育背景, job_education
> 公司名称, company_name
> 公司类型, company_type
> 公司状况, company_status
> 公司人数, company_people
> 技能需要, job_tips
> 工作福利, job_welfare

怕去完成之后导入数据库,这里用到的是mysql数据库. 
在利用pandas进行数据清洗和归类,分析
最后利用pyecharts进行数据可视化操作.

**以求能够全方位的获取和分析数据分析岗位的要求,和前景.为工作的选择和判断做出规划.**

## 数据概览
![avatar](https://github.com/missLH/lagou_jobs_analysis/blob/master/%E6%8B%89%E5%8B%BE%E7%BD%91%E5%B7%A5%E4%BD%9C%E4%BF%A1%E6%81%AF%E5%88%86%E6%9E%90/2.png)

## 1. 岗位在全国范围内的分布情况
例子: 代码如下(后面的分析具体代码见文件)
> from pyecharts import Geo
import dy  #自建库来完成重复的数据库数据调用
df = dy.con_sql('job')
分组, 计数, 重设索引, 排序(数据清洗)
city_message = df.groupby(['job_city'])
city_com = city_message['job_city'].agg(['count'])
city_com.reset_index(inplace=True)
city_com_last = city_com.sort_index()
画图
geo = Geo("拉勾网数据分析岗—城市分布热力图", title_pos='center', title_top='0', width=1200, height=600, title_color="#fff", background_color="#404a59",)
attr = city_com_last['job_city']
value = city_com_last['count']
geo.add("", attr, value, type="heatmap", is_visualmap=True, visual_range=[0, 30], visual_text_color="#fff", is_label_show=True)
geo.render('拉勾网数据分析岗—城市分布图.html')

![avatar](https://github.com/missLH/lagou_jobs_analysis/blob/master/%E6%8B%89%E5%8B%BE%E7%BD%91%E5%B7%A5%E4%BD%9C%E4%BF%A1%E6%81%AF%E5%88%86%E6%9E%90/%E6%8B%89%E5%8B%BE%E7%BD%91%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B2%97%E2%80%94%E5%9F%8E%E5%B8%82%E5%88%86%E5%B8%83%E7%83%AD%E5%8A%9B%E5%9B%BE.png)

从城市维度来看，北京数据分析职位的需求量为最多，其次其次是上海，杭州，深圳的数量不如杭州多。在TOP10城市中,对数据分析人才需求最大少的是郑州、合肥，职位数量仅仅4个。所以想要从事数据分析一职，基本上要选择留在北上广深，或者杭州，才能拥有更好的发展

## 2.公司类型

![avatar](https://github.com/missLH/lagou_jobs_analysis/blob/master/%E6%8B%89%E5%8B%BE%E7%BD%91%E5%B7%A5%E4%BD%9C%E4%BF%A1%E6%81%AF%E5%88%86%E6%9E%90/%E6%8B%89%E5%8B%BE%E7%BD%91%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B2%97%E2%80%94%E5%85%AC%E5%8F%B8%E7%B1%BB%E5%9E%8BTOP10.png)

由图可以看出：在10个细分领域中数据分析职位需求最高的是金融和移动互联网行业，其次是电子商务行业。需求最少的是生活服务和文化娱乐行业。

## 3.工作经验与薪水

![avatar](https://github.com/missLH/lagou_jobs_analysis/blob/master/%E6%8B%89%E5%8B%BE%E7%BD%91%E5%B7%A5%E4%BD%9C%E4%BF%A1%E6%81%AF%E5%88%86%E6%9E%90/%E6%8B%89%E5%8B%BE%E7%BD%91%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B2%97%E2%80%94%E5%B7%A5%E4%BD%9C%E7%BB%8F%E9%AA%8C%E8%96%AA%E6%B0%B4%E5%9B%BE(%E5%85%83_%E6%9C%88).png)

从工作年限来看，大部分公司的需求都在1-3年和3-5年这两个阶段。这两个阶段的人较工作5-10年的人年轻，精力旺盛，对工资要求不是特别高，学习能力也较强。
其中最值得注意的是应届生, 大部分岗位的工资甚至高过了一年经验的.

## 4.公司规模与薪水

![avatar](https://github.com/missLH/lagou_jobs_analysis/blob/master/%E6%8B%89%E5%8B%BE%E7%BD%91%E5%B7%A5%E4%BD%9C%E4%BF%A1%E6%81%AF%E5%88%86%E6%9E%90/%E6%8B%89%E5%8B%BE%E7%BD%91%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B2%97%E2%80%94%E5%85%AC%E5%8F%B8%E8%A7%84%E6%A8%A1%E8%96%AA%E6%B0%B4%E5%9B%BE(%E5%85%83_%E6%9C%88).png)

可以看到15-150内的公司薪资状况差不太多, 150-2000高一个档次, 2000+的又是另一个档次,比如BAT

## 5.学历与薪水

![avatar](https://github.com/missLH/lagou_jobs_analysis/blob/master/%E6%8B%89%E5%8B%BE%E7%BD%91%E5%B7%A5%E4%BD%9C%E4%BF%A1%E6%81%AF%E5%88%86%E6%9E%90/%E6%8B%89%E5%8B%BE%E7%BD%91%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B2%97%E2%80%94%E5%AD%A6%E5%8E%86%E8%96%AA%E6%B0%B4%E5%9B%BE(%E5%85%83_%E6%9C%88).png)

这里可以发现本科和硕士的情况大致相同,知识极端情况本科多一些.我们能判断这个岗位和硕士学历不大匹配.

## 6.公司状态与薪水

![avatar](https://github.com/missLH/lagou_jobs_analysis/blob/master/%E6%8B%89%E5%8B%BE%E7%BD%91%E5%B7%A5%E4%BD%9C%E4%BF%A1%E6%81%AF%E5%88%86%E6%9E%90/%E6%8B%89%E5%8B%BE%E7%BD%91%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B2%97%E2%80%94%E5%85%AC%E5%8F%B8%E7%8A%B6%E6%80%81%E8%96%AA%E6%B0%B4%E5%9B%BE(%E5%85%83_%E6%9C%88).png)
/拉勾网数据分析岗—公司状态薪水图(元_月).png
这是公司是否融资对于薪资的影响情况.

## 7.所需技能

![avatar](https://github.com/missLH/lagou_jobs_analysis/blob/master/%E6%8B%89%E5%8B%BE%E7%BD%91%E5%B7%A5%E4%BD%9C%E4%BF%A1%E6%81%AF%E5%88%86%E6%9E%90/%E6%8B%89%E5%8B%BE%E7%BD%91%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B2%97%E2%80%94%E6%8A%80%E8%83%BD%E5%9B%BE%20(1).png)

这是从450各岗位中筛选出来的所需技能的频次图,并且把其包装成树图的样子,可以清晰的看到,此岗位对于数据分析能力,SQL,数据运营, PowerBI, 数据挖掘, 数据库, 可视化, SPSS软件的使用有要求. 想求职的话最好是掌握和熟悉其中的大部分技能.

## 8.公司福利

![avatar](https://github.com/missLH/lagou_jobs_analysis/blob/master/%E6%8B%89%E5%8B%BE%E7%BD%91%E5%B7%A5%E4%BD%9C%E4%BF%A1%E6%81%AF%E5%88%86%E6%9E%90/%E7%A6%8F%E5%88%A9.jpg)

可以看到五险一金,双休, 扁平化管理,绩效等等


## 小结:
从城市维度来看，北京数据分析职位的需求量为最多，其次是上海，杭州，深圳的
薪资：数据分析职位的工资大部分集中在8K-22K左右，整体呈左偏分布。
从城市角度来看，北京、杭州、上海的数据分析职位工资位列前三名。 
从公司规模维度分析，公司规模越大对数据分析人才的需求也就越大。从结果发现少于15人的公司需求量最少。
薪资：随着公司规模的增大，数据分析职位的工资也随之增高。高工资更多存在于公司规模大一些的公司。
融资阶段
需求情况：可以选择融资A轮以上的公司，尤其是上市公司和不需要融资的公司，这样的公司需求量较高。
薪资：从未融资到D轮融资，融资次数越多的公司工资水平也缓慢增加。
工作年限
需求情况：从工作年限来看，大部分公司的需求都在1-3年和3-5年这两个阶段。
薪资：从工作年限来分析，工作经验的增加有助于提升工资。
学历
需求情况：从学历维度看，本科学历的数据分析人才需求量最高，占比85.3%。
薪资：从学历方面来说，学历的提升还是有助于工资水平的增长。
总的来说维度比较单一.

**数据分析更重要的是数学、统计知识和对业务的理解。后续会增加这方面的学习，进行更加深入的分析。**
