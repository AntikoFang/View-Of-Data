# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 08:16:29 2019

@author: Administrator
"""

import pyecharts.charts as pyec

# 柱状图
x = ['甲','乙','丙']
y = [300,800,600]

bar = pyec.Bar()
bar.add_xaxis(x)
bar.add_yaxis(series_name = '公司A',yaxis_data = y)
# 保存
bar.render(r'D:\Python Spyder\数据可视化\My PyEcharts\柱状图.html')

#加一些配置选项
import pyecharts.options as opts
    # 添加标题
bar.set_global_opts(title_opts = opts.TitleOpts(title = '比较图'))
bar.render(r'D:\Python Spyder\数据可视化\My PyEcharts\柱状图2.html')

#增加一个数据系列
y1 = [1200,500,200]
bar.add_yaxis(series_name = '公司B',yaxis_data=y1) 
bar.render(r'D:\Python Spyder\数据可视化\My PyEcharts\柱状图3.html')

# 变成条形图
bar.reversal_axis()
bar.render(r'D:\Python Spyder\数据可视化\My PyEcharts\条形图.html')

#========================================================================

# 折线图
x1 = ['2017','2018','2019']
y1 = [300,900,500]
line = pyec.Line()
line.add_xaxis(x1)
line.add_yaxis(series_name='A',y_axis = y1)
line.render(r'D:\Python Spyder\数据可视化\My PyEcharts\折线图.html')

# Line 增加提示项目
#提示项 Tool

line.set_global_opts(title_opts=opts.TitleOpts(title = '我的pyecharts'),
                     tooltip_opts = opts.TooltipOpts(trigger='axis',axis_pointer_type='cross'),
                     # 工具箱设置  is_show = True 默认展示图例     
                     #orient 参数 ：horizontal 横向  v  纵向
                     toolbox_opts = opts.ToolboxOpts(is_show=True,orient='horizontal'),
                     # 设置滚动条
                     datazoom_opts=opts.DataZoomOpts(type_='slider',range_start=(),range_end=2500)
                     )
line.render(r'D:\Python Spyder\数据可视化\My PyEcharts\折线图4.html')


# 设置图表的大小
line1 = pyec.Line(init_opts=opts.InitOpts(width = '500px',height = '300px'))
line.add_xaxis(x1)
line.add_yaxis(series_name='A',y_axis = y1)
line.render(r'D:\Python Spyder\数据可视化\My PyEcharts\折线图4.html')

#====================================================================

# 饼图

#构建饼图数据
x_data = ['直接访问','营销推广','博客推荐','搜索引擎']
y_data = [800,214,300,1100]
    # Pie 设置指定的格式
data_pair = list(zip(x_data,y_data))
print(data_pair)

# 画饼图
pie = pyec.Pie()
pie.add(series_name='推广渠道',data_pair=data_pair, 
        # 环形图
        radius=['40%','75'])
pie.render(r'D:\Python Spyder\数据可视化\My PyEcharts\环形图.html')

#====================================================================

# 撒点图

# 生成数据
import numpy as np
x = np.linspace(0,10,30)
y1 = np.sin(x)

scatter = pyec.Scatter()
scatter.add_xaxis(xaxis_data=x)
scatter.add_yaxis(series_name='y = sin(x)',y_axis=y1,
                  #设置数据点是否展示
                  label_opts=opts.LabelOpts(is_show=False),
                  # 改变点的大小
                  symbol_size = 15,
                  # 控制点的形状
                  symbol = 'roundRect'
                  )
scatter.render(r'D:\Python Spyder\数据可视化\My PyEcharts\散点图.html')

#====================================================================

#词云图

import this

s = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

s = s.lower() #全部转小写
s = s.split() #转化为单词列表
# 统计词频
d = {}
for i in s:
    d[i] = d.get(i,0) + 1
    
#d = d.items()

wordcloud = pyec.WordCloud()
wordcloud.add(series_name='',data_pair=d)
wordcloud.render(r'D:\Python Spyder\数据可视化\My PyEcharts\词云图.html')

#========================================================================

# 使用主题

import pyecharts.charts as pyec
import pyecharts.options as opts
from pyecharts.globals import ThemeType

x = ['a','b','c','d','e','f']
y1 = [5,20,36,10,75,90]
y2 = [15,6,45,20,55,40]
y3 = [45,30,6,10,5,50]
y4 = [25,20,16,30,25,80]

bar = pyec.Bar()
    #设置主题类型    在实例化时设置
    # DARK MACARONS PURPLE_PASSION ROMA ROMANTIC 
        #SHINE VINTAGE WALDEN  WESTEROS WONDERLAND
bar = pyec.Bar(init_opts = opts.InitOpts(theme = ThemeType.MACARONS))
bar.add_xaxis(x)
bar.add_yaxis(series_name = 'A',yaxis_data = y1)
bar.add_yaxis(series_name = 'B',yaxis_data = y2)
bar.add_yaxis(series_name = 'C',yaxis_data = y3)
bar.add_yaxis(series_name = 'D',yaxis_data = y4)

bar.set_global_opts(title_opts = opts.TitleOpts(title='默认',subtitle='副标题'))
bar.render(r'D:\PythonSpyder\数据可视化\My PyEcharts\主题柱状图MACARONS.html')

#==============================================================================

# 日历图

import datetime
import random

from pyecharts import options as opts
from pyecharts.charts import Calendar

def calendar_base() -> Calendar:
    begin = datetime.date(2017, 1, 1)
    end = datetime.date(2017, 12, 31)
    data = [
        [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
        for i in range((end - begin).days + 1)
    ]

    c = (
        Calendar()
        .add("", data, calendar_opts=opts.CalendarOpts(range_="2017"))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Calendar-2017年微信步数情况"),
            visualmap_opts=opts.VisualMapOpts(
                max_=20000,
                min_=500,
                orient="horizontal",
                is_piecewise=True,
                pos_top="230px",
                pos_left="100px",
            ),
        )
    )
    return c
calendar_base().render(r'D:\PythonSpyder\数据可视化\My PyEcharts\日历图1.html')

# 日历图

import datetime
import random

from pyecharts import options as opts
from pyecharts.charts import Calendar

begin = datetime.date(2017, 1, 1)
end = datetime.date(2017, 12, 31)
data = [
    [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
    for i in range((end - begin).days + 1)
]
calender = Calendar()
calender.add('',data,calendar_opts=opts.CalendarOpts(range_="2017"))
calendar_base().render(r'D:\PythonSpyder\数据可视化\My PyEcharts\日历图2.html')

#==============================================================================

# 漏斗图

from pyecharts.charts import Funnel
data = 
funnel = Funnel()
funnem.add('',data)
funne.render()

#==============================================================================

# 仪表盘

from pyecharts.charts import Gauge
gauge = Gauge()
gauge.add('',[('完成率',60)],
              # 不同颜色
              axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color=[(0.6, "#67e0e3"), (1, "#37a2da")], width=30
                )))
gauge.render(r'D:\PythonSpyder\数据可视化\My PyEcharts\仪表盘(不同颜色).html')

#==============================================================================

# 水球图
from pyecharts.charts import Liquid
liquid = Liquid()
liquid.add('',[0.6])
liquid.render(r'D:\PythonSpyder\数据可视化\My PyEcharts\水球图.html')




