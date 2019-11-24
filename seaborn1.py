# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 08:13:40 2019

@author: Administrator
"""

#准备工作
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
import numpy as np
import pandas as pd

plt.rcParams['font.family']='SimHei'#'SimHei'为黑体
plt.rcParams['axes.unicode_minus'] = False #显示负号
sns.set_style('darkgrid',{'font.sans-serif':['SimHei','Arial']})

import warnings  # 去除部分警告信息
warnings.filterwarnings('ignore')

n = 1024
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)
g = sns.joinplot(x,y,
                kind = 'reg' #回归线 ‘kde’'hex'
                )

#=============================================================================

# 绘制大型分布图

import seaborn as sns
sns.set(style="whitegrid")

diamonds = sns.load_dataset("diamonds")

clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]

sns.boxenplot(x="clarity", y="carat",
              color="b", order=clarity_ranking,
              scale="linear", data=diamonds,k_depth='trustworthy')

help(sns.boxenplot)

x=None, y=None, hue=None, data=None, order=None, hue_order=None, 
orient=None, color=None, palette=None, saturation=0.75, width=0.8, 
dodge=True, k_depth='proportion',linewidth=None, scale='exponential',
outlier_prop=None, ax=None



