# -*- coding: utf-8 -*-
from flask import Blueprint,request
import os
import json
import datetime
import platform
import csv
import os
import traceback
import yaml

from const import *

data = Blueprint('register', __name__)
if platform.system()=="Linux":
    path_home="/home/wuhan2020/wuhan2020"
else:
    from index import app
    path_home=os.path.join(app.root_path,"wuhan2020")
# wuhan2020文件夹为https://github.com/wuhan2020/wuhan2020项目文件的本地clone
# 阿里云serverless使用挂载nas远程目录来存放缓存文件；在本机调试时，缓存文件夹将存放在项目根目录

if not os.path.exists(path_home):
    os.mkdir(path_home)
    
"""
CACHE PATH
"""
HOSPITAL_PATH = os.path.join(path_home, "HOSPITAL.csv")
HOTEL_PATH = os.path.join(path_home, "HOTEL.csv")
LOGISITICAL_PATH = os.path.join(path_home, "LOGISTICAL.csv")
NEWS_PATH = os.path.join(path_home, "NEWS.csv")
DONATION_PATH = os.path.join(path_home, "DONATION.csv")
FACTORY_PATH = os.path.join(path_home, "FACTORY.csv")
CLINIC_PATH = os.path.join(path_home, "CLINIC.csv")


"""
Tools
"""
def csv_helper(fpath, headers):
    result = []
    with open(fpath) as f:
        for line in f.readlines()[1:]:
            csv_data = line.strip().split(",")
            result.append(dict(zip(headers,csv_data)))
    return result
    
def csv_helperpage(fpath, headers,page,size):
    result = []
    firstpage=(page-1)*size+1
    lastpage=page*size+1
    with open(fpath) as f:
        for line in f.readlines()[firstpage:lastpage]:
            csv_data = line.strip().split(",")
            result.append(dict(zip(headers,csv_data)))
    return result

def yaml_helper(fpath):
    result = []
    with open(fpath, 'r') as f:
        result = yaml.load(f)
    return result


def xml_helper(xml_path):
    with open(xml_path, 'r') as f:
        xml_str = f.read()
    json = xmltodict.parse(xml_str)
    return json


def json_helper(json_path):
    with open(json_path, 'r', encoding='UTF-8') as f:
        return json.loads(f.read())

@data.route('/hospital_list')
def hospital_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_helper(HOSPITAL_PATH,HOTEL_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)
    
@data.route('/hospital_list_page',methods=['post','get'])
def hospital_list_page():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        page=int(request.args.get("page"))
        size=int(request.args.get("size"))
        resp_data = csv_helperpage(HOSPITAL_PATH,HOTEL_HEADERS, page, size)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)

@data.route('/hospitallcount')
def hospital_count():
    resp = {
        'count': 0,
    }
    try:
        #count = 0
        total = sum(1 for line in open(HOSPITAL_PATH))
        resp['count']=total-1
    except Exception as e:
        print e
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/hotel_list')
def hotel_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_helper(HOTEL_PATH, HOTEL_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)
@data.route('/hotelcount')
def hotel_count():
    resp = {
        'count': 0,
    }
    try:
        #count = 0
        total = sum(1 for line in open(HOTEL_PATH))
        resp['count']=total-1
    except Exception as e:
        print e
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)
    
@data.route('/logstics_list')
def logstics_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_helper(LOGISITICAL_PATH,LOGISTICS_HEADERS )
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)



@data.route('/news_list')
def news_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_helper(NEWS_PATH, NEWS_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/donation_list')
def donation_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_helper(DONATION_PATH, DONATION_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/factory_list')
def factory_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_helper(FACTORY_PATH, FACTORY_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/clinic_list')
def clinic_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_helper(CLINIC_PATH,CLINIC_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)
