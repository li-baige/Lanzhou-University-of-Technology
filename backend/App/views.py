import json
import sys
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import pymysql
from server.settings import DATABASES
from django.views.decorators.csrf import csrf_exempt
from .models import *

connection = pymysql.connect(
    host = DATABASES['default']['HOST'],
    user = DATABASES['default']['USER'],
    password = DATABASES['default']['PASSWORD'],
    db = DATABASES['default']['NAME'],
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)
cursor = connection.cursor()

location_path_suffix = r'/data/D_boundary.json'
confirm_path_suffix = r'/data/confirm.json'
# project_path = sys.arrgv[0].replace('/manage.py/', '')
project_path = sys.path[0]
location_path = '{}{}'.format(project_path, location_path_suffix)
city_path = '{}{}'.format(project_path,confirm_path_suffix)
# Create your views here.

def index(request):
    # GET请求获取参数
    # 测试URL:http://101.35.252.249/index
    print("test success!")
    return render(request, 'index.html')

def village_name(request):
    # GET请求获取参数
    # 请求URL: http://101.35.252.249/api/village_name
    village_names = []
    village_dict = None
    with open(location_path,'r', encoding='utf8') as f:
        village_dict = json.load(f)
    for k in village_dict:
        village_names.append(k)
    return HttpResponse(village_names.__str__())

def boundary(request):
    # GET请求获取参数
    # 请求URL: http://101.35.252.249/api/boundary
    village_name = request.GET['village_name']  
    boundarys = []
    village_dict = None 
    with open(location_path, 'r', encoding='utf8') as f:
        village_dict = json.load(f) 
    boundarys = village_dict[village_name] 
    return HttpResponse(boundarys.__str__()) 

def confirm(request):
    # GET请求参数
    # 请求URL:http://101.35.252.249/api/confirm
    data = request.GET['data']
    confirms = []
    data_dict = None
    with open(city_path, 'r', encoding='utf8') as f:
        data_dict = json.load(f)
    confirms = data_dict[data]
    return HttpResponse(confirms.__str__())

def village_data(request):
    # GET请求小区名字
    # 请求实例：http://101.35.252.249/api/village_data?village_name=惠安小区
    # 返回实例:
    '''
    {
        "code": 200, 
        "village_name": "\u60e0\u5b89\u5c0f\u533a", 
        "village_boundary": "103.91664064084362,36.04921222854583;103.91704712408689,36.04804840689462;103.91735030219651,36.04806686417781;103.91841057218993,36.048142808921625;103.91825309923404,36.04839880271529;103.9183429297", 
        "confirmed": 3, 
        "status": 2, 
        "opend_time": 
        "2022-03-31", 
        "closed_time": "2022-03-16"
    }
    '''
    village_name = request.GET['village_name']
    
    sql = "SELECT App_boundary.village_boundary, confirmed, closed_time, opend_time, status FROM App_boundary,App_villagestatus WHERE App_boundary.village_name=\""+village_name+"\" AND App_villagestatus.village_name=\"" + village_name + "\" "
    print(sql)
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    if len(data) == 0:
        ret = {
            "code": 404,
            "msg": "输入参数为空，请输入小区名字"
        }
        return JsonResponse(ret)
    ret = {
        "code": 200,
        "village_name": village_name,
        "village_boundary": data[0]["village_boundary"],
        "confirmed": data[0]["confirmed"],
        "status": data[0]["status"],
        "opend_time": data[0]["opend_time"],
        "closed_time": data[0]["closed_time"],
    }
    return JsonResponse(ret)

def confirmed(request):
    # GET确诊人员病历号
    # 请求实例：http://101.35.252.249/api/confirmed?confirmed=
    # 返回实例：
    '''
    '''
    case_num = request.GET['case_num']
    
    sql = "SELECT track.case_num, id, name, village_name, relation, confirm_date, track,vehicle FROM track WHERE track.case_num=\""+case_num+"\" "
    print(sql)
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    if len(data) == 0:
        ret = {
            "code": 404,
            "msg": "输入参数为空，请输入病例id"
        }
        return JsonResponse(ret)        
    datas = []
    for i in data:
        item = {
            "case_num": i["case_num"],
            "village_name": i["village_name"],
            "relation": i["relation"],
            "confirm_date": i["confirm_date"],
            "track": i["track"],
            "vehicle": i["vehicle"],
        }
        datas.append(item)
    ret = {
        "code": 200,
        "datas": datas
    }
    return JsonResponse(ret)

def city(request):
    # GET城市每天疫情数据具体数值
    # 请求实例：http://101.35.252.249/api/city?year=&data=
    #返回实例：
    '''
    '''
    year = request.GET['year']
    data = request.GET['data']
    
    sql = "SELECT App_city.year, city.data, confirm, dead, heal, suspect, confirm_add FROM city WHERE App_city.year=\""+ year +"\" AND App_city.data=\"" + data + "\" "
    print(sql)
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    if len(data) == 0:
        ret = {
            "code": 404,
            "msg": "输入参数未查询到，请输入正确的日期",
            "msg2": "输入示例:year=2020&data=10.23",
        }
        return JsonResponse(ret)
    ret = {
        "code": 200,
        "year": data[0]["year"],
        "data": data[0]["data"],
        "city": "兰州",
        "confirm": data[0]["confirm"],
        "dead": data[0]["dead"],
        "heal": data[0]["heal"],
        "suspect": data[0]["suspect"],
        "confirm_add": data[0]["confirm_add"],
    }
    return JsonResponse(ret)

@csrf_exempt
def village_date(request):
    # POST小区状态及其具体信息
    # 请求实例：http://101.35.252.249/
    # 返回实例
    village_name = request.POST['village_name']

    sql = "SELECT App_villagedata.village_name, village_boundary, confirmed, name, closed_time, opend_time FROM App_villagedata WHERE village_name=\""+village_name+"\" "
    print(sql)
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    if len(data) == 0:
        ret = {
            "code": 404,
            "msg": "输入参数为空，请输入小区名字"
        }
        return JsonResponse(ret)
    datas = []
    for i in data:
        item = {
            "village_name": i["village_name"],
            "village_boundary": i["village_boundary"],
            "confirmed": i["confirmed"],
            "name": i["name"],
            "closed_time": i["closed_time"],
            "opend_time": i["opend_time"],
        }
        datas.append(item)
    ret = {
        "code": 200,
        "data": datas
    }
    #print (ret)
    return JsonResponse(ret)
    
def community_name(request):
    # GET 请求all 返回所有当前确诊小区
    all = request.GET['all']
    ret = {
        "code": 200,
        "data": []
    }

    data = []
    cs = Community.objects.all()
    print(cs.count())
    for c in cs:
        d = {
            "community": c.community_name,
            "name": []
        }
        flag = False
        for j in data:
            if j["community"] == c.community_name:
                flag = True
            else:
                continue
        if not flag:
            data.append(d)
        
    for c in cs:
        for i in data:
            if i["community"] == c.community_name:
                if c.name not in i["name"]:
                    i["name"].append(c.name)

    ret["data"] = data
    return JsonResponse(ret)

    
