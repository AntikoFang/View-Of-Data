# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 21:18:07 2019

@author: AntikoFang
@IDE：spyder
"""
from pyecharts import Page
page=Page() 

# 2019全国分布图
#=============================================================================
import jieba
from pyecharts import Geo 
#导入文本
place = open(r'D:\BI大屏\工作地点.txt',encoding = 'utf-8').read()
places=jieba.cut(place)
#读取停用词文件
stops=open(r'D:\BI大屏\去停用词.txt','r',encoding='UTF-8').read()
# 去停用词
pls=[pl for pl in places if pl not in stops]

p={}
for i in pls:
    p[i] = p.get(i,0) + 1
    
place_list = sorted(p.items(), key=lambda x:x[1], reverse=True)[:190]
keyplace = [i[0] for i in place_list]
valueplace = [i[1] for i in place_list]
data = list(zip(keyplace,valueplace))[2:]

geo =Geo(background_color='#404a59')
attr, value =geo.cast(data)
geo.add("", attr,value, type="effectScatter", is_random=True, effect_scale=5)
#geo.render(r'D:\BI大屏\2019GEO地图.html')

page.add_chart(geo,name="geo") 

#=============================================================================

# 薪资柱状图
#=============================================================================
from pyecharts import Bar
import pandas as pd
# 今年薪资
#=========================================

excel = pd.read_excel(r'D:\BI大屏\tongjixue1.xlsx')

a = []
a_avg = []
for i in range(0,len(excel["薪资"])):
    dw = excel["薪资"][i][-3:]
    a = excel["薪资"][i][0:-3].split("-")
    if dw == '千/月':
        a_avg.append((float(a[0])+float(a[1]))*500)
    elif dw == '万/月':
        a_avg.append((float(a[0])+float(a[1]))*5000)
    elif dw == '万/年':
        a_avg.append((float(a[0])+float(a[1]))*5000/12)
        
excel["平均薪资"] = a_avg
excel.to_excel(r'D:\BI大屏\tongjixue1.xlsx')

b0 = 0
b1 = 0
b2 = 0
b3 = 0
b4 = 0
b5 = 0
b6 = 0
b7 = 0

for avg in a_avg:
    if avg <= 10000:
        b0 += 1
    elif avg <= 20000:
        b1 += 1
    elif avg <= 30000:
        b2 += 1    
    elif avg <= 40000:
        b3 += 1
    elif avg <= 50000:
        b4 += 1
    elif avg <= 70000:
        b5 += 1      
    elif avg <= 90000:
        b6 += 1
    else:
        b7 += 1
b = [b0,b1,b2,b3,b4,b5,b6,b7]
# 去年薪资
#===========================
excel1 = pd.read_excel(r'D:\BI大屏\拉勾网.xlsx',sheet_name = 1)
excel2 = pd.read_excel(r'D:\BI大屏\拉勾网.xlsx',sheet_name = 2)

a1_avg = []
for i in range(0,len(excel1["薪资区间"])):
    a1 = excel1["薪资区间"][i].replace("k","000").split("-")
    a1_avg.append(float(a1[0])+float(a1[1]))
     
for j in range(0,len(excel2["薪资"])):
    dw1 = excel["薪资"][j][-3:]
    a1 = excel["薪资"][j][0:-3].split("-")
    if dw1 == '千/月':
        a1_avg.append((float(a[0])+float(a[1]))*500)
    elif dw1 == '万/月':
        a1_avg.append((float(a[0])+float(a[1]))*5000)
    elif dw1 == '万/年':
        a1_avg.append((float(a[0])+float(a[1]))*5000/12)
        
c0 = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
for avg1 in a1_avg:
    if avg1 <= 10000:
        c0 += 1
    elif avg1 <= 20000:
        c1 += 1
    elif avg1 <= 30000:
        c2 += 1    
    elif avg1 <= 40000:
        c3 += 1
    elif avg1 <= 50000:
        c4 += 1
    elif avg1 <= 70000:
        c5 += 1      
    elif avg1 <= 90000:
        c6 += 1
    else:
        c7 += 1
c = [c0,c1,c2,c3,c4,c5,c6,c7]
attr = ['0-1万','1-2万','2-3万','3-4万','4-5万','5-7万','7-9万','大于9万']

bar = Bar(background_color='#404a59')
bar.use_theme("dark")  
bar.add('2019',attr,b,mark_point=['average'])  #追加最大值标记点、最小值标记点 
bar.add('2018',attr,c,mark_point = ['average'],bar_category_gap=45)  #追加最大值标记点、最小值标记点 
#bar.render(r"D:\BI大屏\薪资对比柱状图.html")

page.add_chart(bar,name="bar") 

#=============================================================================

# 学历需求饼图
from pyecharts import Pie
#=============================================================================
#导入文本
txt = open(r'D:\BI大屏\学历.txt',encoding = 'utf-8').read()
  # 导入停用词
jieba.load_userdict(r'D:\BI大屏\停用词.txt')
#分词
cun=jieba.cut(txt)
#读取停用词文件
stops=open(r'D:\BI大屏\去停用词.txt','r',encoding='UTF-8').read()
# 去停用词
tokens=[token for token in cun if token not in stops]
d={}
for i in tokens:
    d[i] = d.get(i,0) + 1

count_list = sorted(d.items(), key=lambda x:x[1], reverse=True)
count_list = count_list[:20]
keyword_list = [k[0] for k in count_list]
value_list = [k[1] for k in count_list]


attr = keyword_list
v1 = value_list
#v2 = [19, 21, 32, 20, 20, 33]
pie =Pie(background_color='#404a59')
pie.use_theme('dark')
#pie.add("学历", attr, v1, center=[25, 50], is_random=True, radius=[20, 60], rosetype='radius')
pie.add("学历", attr, v1, is_random=True, radius=[20, 60], is_legend_show=False, is_label_show=True)
pie.show_config() 
#pie.render(r"D:\BI大屏\学历需求饼图.html")
page.add_chart(pie,name="pie") 

#=============================================================================
# 工作经验折线图
import pandas as pd
from pyecharts import Line
#=============================================================================

#导入文本
a = []
txt1 = pd.read_excel(r'D:\BI大屏\拉勾网.xlsx')
exper = txt1['工作经验']
for i in range(len(exper)):
    a.append(exper[i][2])
   
d1={}
for j in a:
    d1[j] = d1.get(j,0) + 1
    
count_list1 = sorted(d1.items(), key=lambda x:x[0], reverse=False)
del count_list1[-2:]
k1 = [k1[0] for k1 in count_list1]
v1 = [k1[1] for k1 in count_list1]

txt = open(r'D:\BI大屏\工作经验.txt',encoding = 'utf-8').read()

  # 导入停用词
jieba.load_userdict(r'D:\BI大屏\停用词.txt')
#分词
cun=jieba.cut(txt)
#读取停用词文件
stops=open(r'D:\BI大屏\去停用词.txt','r',encoding='UTF-8').read()
# 去停用词
tokens=[token for token in cun if token not in stops]
d={}
for i in tokens:
    d[i] = d.get(i,0) + 1

count_list = sorted(d.items(), key=lambda x:x[0], reverse=False)
del count_list[-2]
keyword_list = [k[0] for k in count_list]
k2 = []
for i in keyword_list:
    k2.append(i[0])
#k_list = sorted(k, key=lambda x:x[0], reverse=False)
value_list = [k[1] for k in count_list]
v2 = value_list


line = Line(background_color='#404a59')
line.use_theme('dark')
# is_datazoom_show=True,
line.add('2018',k1,v1,mark_point=['average'], is_smooth=True)
line.add('2019',k2,v2,mark_point=['average'], is_smooth=True)
#line.add('',attr,v1)
#line.render(r"D:\BI大屏\工作经验折线.html")
page.add_chart(line,name="line") 

#=============================================================================

# 漏斗图
from pyecharts import Funnel 
import os as os 
from bs4 import BeautifulSoup  
#=============================================================================

#导入文本
txt = open(r'D:\BI大屏\职能类别.txt',encoding = 'utf-8').read()

  # 导入停用词
jieba.load_userdict(r'D:\BI大屏\停用词.txt')
#分词
cun=jieba.cut(txt)
#读取停用词文件
stops=open(r'D:\BI大屏\去停用词.txt','r',encoding='UTF-8').read()
# 去停用词
tokens=[token for token in cun if token not in stops]
d={}
for i in tokens:
    d[i] = d.get(i,0) + 1

count_list = sorted(d.items(), key=lambda x:x[1], reverse=True)
count_list = count_list[:15]
keyword_list = [k[0] for k in count_list]
value_list = [k[1] for k in count_list]


funnel=Funnel(background_color='#404a59')    #修改标题位置 
funnel.use_theme("dark")    #修改图表主题 
funnel.add("",keyword_list,
           value_list,
           is_label_show=True,
           is_legend_show=False,
           label_pos="outside")   #是否显示标签、是否显示图例、标签位置 
funnel._option['series'][0]["top"]=70   #修改漏斗图上间隔 
funnel._option['series'][0]["bottom"]=20    #修改漏斗图下间隔 
funnel._option['series'][0]["left"]="5%"    #修改漏斗图左间隔 
funnel._option['series'][0]["width"]="90%"  #修改漏斗图宽度 
#funnel.render(r"D:\BI大屏\漏斗图.html")
page.add_chart(funnel,name="funnel") 

#=============================================================================

# 关系图
from pyecharts import Graph
#=============================================================================

nodes = [
        {"name": "统计学", "symbolSize": 81},
        {"name": "英语熟练", "symbolSize": 66},
        {"name": "普通话", "symbolSize": 46},
        {"name": "数学与应用数学", "symbolSize": 38},
        {"name": "管理", "symbolSize": 19},
        {"name": "会计学", "symbolSize": 17},
        {"name": "计算机科学与技术", "symbolSize": 17},
        {"name": "信息与计算科学", "symbolSize": 15},
    ]
links = []
for i in nodes:
        for j in nodes:
            links.append({"source": i.get("name"), "target": j.get("name")})

graph = Graph(background_color='#404a59')
graph.use_theme('dark')
graph.add("",nodes,links,
        categories=None, # 结点分类的类目，结点可以指定分类，也可以不指定。
        is_focusnode=True, # 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。默认为 True
        is_roam=True,
        is_rotatelabel=True, # 是否旋转标签，默认为 False
        graph_layout="force", # 布局类型，默认force=力引导图，circular=环形布局
        graph_edge_length=300, # 力布局下边的两个节点之间的距离，这个距离也会受 repulsion 影响。默认为 50，TODO 值越大则长度越长
        graph_gravity=0.5, # 点受到的向中心的引力因子。TODO 该值越大节点越往中心点靠拢。默认为 0.2
        graph_repulsion=100, # 节点之间的斥力因子。默认为 50，TODO 值越大则斥力越大
        is_label_show=True,
        line_curve=0.2 # 线的弯曲度
          )
#graph.render(r"D:\BI大屏\关系图.html")
page.add_chart(graph,name="graph") 
page.render("D:\BI大屏\page.html") 
#=============================================================================


with open(os.path.join(os.path.abspath("."),"D:\BI大屏\page.html"),'r+',encoding="utf8") as html:     
    html_bf=BeautifulSoup(html,"lxml")     
    divs=html_bf.find_all("div")     
    #修改图表大小、位置、边框
    divs[0]["style"]="width:800px;height:500px;position:absolute;top:100px;left:400px;border-style:solid;border-color:#444444;border-width:0px;"    
    #修改图表大小、位置、边框
    divs[1]["style"]="width:800px;height:300px;position:absolute;top:600px;left:400px;border-style:solid;border-color:#444444;border-width:0px;"
    #修改图表大小、位置、边框
    divs[2]["style"]="width:400px;height:300px;position:absolute;top:100px;left:0px;border-style:solid;border-color:#444444;border-width:0px;"    
    #修改图表大小、位置、边框
    divs[3]["style"]="width:500px;height:400px;position:absolute;top:100px;left:1200px;border-style:solid;border-color:#444444;border-width:0px;"
    #修改图表大小、位置、边框
    divs[4]["style"]="width:400px;height:560px;position:absolute;top:340px;left:0px;border-style:solid;border-color:#444444;border-width:0px;"    
    #修改图表大小、位置、边框
    divs[5]["style"]="width:500px;height:400px;position:absolute;top:500px;left:1200px;border-style:solid;border-color:#444444;border-width:0px;"

    
    html_new=str(html_bf)    
    #修改页面背景色、追加标题
    html_new=html_new.replace("<body>","<body style=\"background-color:#404a59;\">\n<div align=\"center\" style=\"width:1700px;\">\n<span style=\"font-size:32px;font face=\'黑体\';color:#ffffff\"><b>刘永芳统计学专业招聘的BI监控大屏</b></div>")	     
    html.seek(0,0)     
    html.truncate()     
    html.write(html_new)     
    html.close()
