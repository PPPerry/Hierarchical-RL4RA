from pyecharts.charts import Geo  # 导入地理信息处理模块
from pyecharts import options as opts  # 配置
import xlrd
 
# geo_sight_coord = {data['景区地点'][i]: [data['经度'][i], data['纬度'][i]] for i in range(len(data))}  # 构造位置字典数据
ex_data = xlrd.open_workbook(r'hospitals.xlsx')
excel = ex_data.sheets()[0]

col_values = excel.col_values(0)

col_len = len(col_values)

tables = []
tables.append((excel.cell_value(0, 0), excel.cell_value(0, 1)))

g = Geo(init_opts=opts.InitOpts(width="1200px",
                                height="600px",
                                ))  # 地理初始化
g.add_schema(maptype="北京") 
list1 = []
for i in range(col_len):  # 对地理点循环
    g.add_coordinate(i, excel.cell_value(i, 0), excel.cell_value(i, 1))  # 追加点位置
    list1.append([i, i])
 
 
g.add("医护设施分布图", list1, symbol_size=10, label_opts=opts.LabelOpts(
            position="top",
            is_show=True,
            formatter='{b}'))
 
g.render("医疗地图.html")