from pyecharts import Map, Geo
import numpy as np
import xlrd
 
# 区县 -- 具体城市内的区县  xx县
quxian = ['东城区',
'西城区',
'朝阳区',
'丰台区',
'石景山区',
'海淀区',
'门头沟区',
'房山区',
'通州区',
'顺义区',
'昌平区',
'大兴区',
'怀柔区',
'平谷区',
'密云区',
'延庆区']

age65_rate = [18.20,
18.20,
14.30, 
15.80, 
16.40, 
13.10, 
14.80, 
13.20, 
11.50, 
10.80, 
9.72, 
9.70, 
12.80, 
16.40, 
15.20, 
15.70]

age65_rate = np.divide(age65_rate, 100)

population = [708829,
1106214,
3452460,
2019764,
567851,
3133469,
392606,
1312778,
1840295,
1324044,
2269487,
1993591,
441040,
457313,
527683,
345671]

map0 = Map("北京市65岁以上人口分布图", width=1200, height=600)
# map0.set_series_opts(label_opts=opts.LabelOpts(is_show=False),showLegendSymbol=False)
map0.add("", quxian, np.multiply(age65_rate, np.divide(population, 10000)).tolist(), visual_range=[0, 50], maptype="北京",  is_visualmap=True, visual_text_color='#000')

ex_data = xlrd.open_workbook(r'hospitals.xlsx')
excel = ex_data.sheets()[0]

tables = []
tables.append((excel.cell_value(0, 0), excel.cell_value(0, 1)))
print(tables[0])

# map0.add_coordinate("第一个坐标点",tables[0][0],tables[0][1])


map0.render(path="地图.html")