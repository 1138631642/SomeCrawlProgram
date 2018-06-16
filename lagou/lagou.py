#-*- coding:utf-8 -*-
# created 2017.9.12

import json
import requests
import xlwt
import time
from lxml import etree

#解决编码的问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# 获取存储职位信息的json对象，
# 遍历获得公司名、福利待遇、工作地点、学历要求、工作类型、
# 发布时间、职位名称、薪资、工作年限
def get_json(url,datas):
    my_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput=',
    }
    cookies = {
        "Cookie": "user_trace_token=20180301213557-7952b810-1d55-11e8-b109-5254005c3644; LGUID=20180301213557-7952baf1-1d55-11e8-b109-5254005c3644; WEBTJ-ID=20180604163331-163c9ee0cf728c-0900d8b44c3028-5d4e211f-2073600-163c9ee0cf8764; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D1%26rsv_idx%3D2%26tn%3Dbaiduhome_pg%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rsv_spt%3D1%26oq%3D%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%26rsv_pq%3Dcb74115f0000e570%26rsv_t%3D299dAezj8qqSDpkahzS07PpK0VfIvgIC1SGYhU3FLvHih56fBE3mHIh8v8Ecg2jAOMYB%26rqlang%3Dcn%26rsv_enter%3D1%26rsv_sug3%3D4%26rsv_sug1%3D4%26rsv_sug7%3D100%26bs%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; TG-TRACK-CODE=index_search; _gat=1; JSESSIONID=ABAAABAACEBACDG1CAD7C63BA8D4346C5003710E3E73E2B; SEARCH_ID=85b052544835418eb6e76917e3056c8f; X_HTTP_TOKEN=a113be9fc3b0742e905fc069141e6bd6; LGSID=20180604163332-f74575bb-67d1-11e8-9378-5254005c3644; LGRID=20180604170119-d88eab5e-67d5-11e8-9378-5254005c3644; LG_LOGIN_USER_ID=f6cd15f431aa5b1666419899eaf748bfdb9d96528e2a8c89; _putrc=C30DDF74DB1579DA; login=true; unick=%E6%9D%A8%E5%BB%BA%E6%A4%BF; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=7f84692691f0cf51dc6e973c5d32712d2387162a4aff079b; index_location_city=%E5%8C%97%E4%BA%AC; _gid=GA1.2.2014976523.1528101212; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528101211; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528102915; _ga=GA1.2.1967392159.1519911359",
    }
    time.sleep(8)
    content = requests.post(url=url,cookies=cookies,headers=my_headers,data=datas)
    # content.encoding = 'utf-8'
    result = content.json()
    print result

    info = result['content']['positionResult']['result']
    # print info
    info_list = []
    for job in info:
        information = []
        information.append(job['positionId']) # 岗位对应ID
        information.append(job['companyFullName']) # 公司全名
        information.append(job['companyLabelList']) # 福利待遇
        information.append(job['district']) # 工作地点
        information.append(job['education']) # 学历要求
        information.append(job['firstType']) # 工作类型
        information.append(job['formatCreateTime']) # 发布时间
        information.append(job['positionName']) # 职位名称
        information.append(job['salary']) # 薪资
        information.append(job['workYear']) # 工作年限
        info_list.append(information)
        # 将列表对象进行json格式的编码转换,其中indent参数设置缩进值为2
        print json.dumps(info_list, ensure_ascii=False, indent=2)
        print info_list
    return info_list


def main():
    page = int(raw_input('请输入你要抓取的页码总数：'))
    kd = raw_input('请输入你要抓取的职位关键字：')
    # city = raw_input('请输入你要抓取的城市：')


    info_result = []
    title = ['岗位id','公司全名','福利待遇','工作地点','学历要求','工作类型','发布时间','职位名称','薪资','工作年限']
    info_result.append(title)
    for x in range(1,page+1):
        url = 'https://www.lagou.com/jobs/positionAjax.json?&needAddtionalResult=false'
        datas = {
            'first': True,
            'pn': x,
            'kd': 'python',
            'city': '上海'
        }
        info = get_json(url,datas)
        info_result = info_result+info
        # 创建workbook,即excel
        workbook = xlwt.Workbook(encoding='utf-8')
        # 创建表,第二参数用于确认同一个cell单元是否可以重设值
        worksheet = workbook.add_sheet('lagouzp',cell_overwrite_ok=True)
        for i, row in enumerate(info_result):
            # print row
            for j,col in enumerate(row):
                # print col
                worksheet.write(i,j,col)
        workbook.save('lagouzp.xls')

if __name__ == '__main__':
    main()

# 作者：意气相许的许
# 链接：https://www.jianshu.com/p/5cf59099ff5e
# 來源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。