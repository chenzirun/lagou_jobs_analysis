import requests
import pymysql
import random
import time
import json

count = 0
proxie = [
    "134.249.156.3:82",
    "1.198.72.239:9999",
    "103.26.245.190:43328",
]
proxies = {
           "http": str(random.sample(proxie, 1))
#         "http":"103.26.245.190:43328"
}
#     agents = random.sample(agent, 1)
url_start = "https://www.lagou.com/jobs/list_数据分析?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput="
url_parse = "https://www.lagou.com/jobs/positionAjax.json?city=全国&needAddtionalResult=false"
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://www.lagou.com/jobs/list_%E8%BF%90%E7%BB%B4?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36' }



# 连接数据库
db = pymysql.connect(host='127.0.0.1', user='root', password='czrlh1234', port=3306, db='lagou_job', charset='utf8mb4')


def add_Mysql(id, job_title, job_salary, job_city, job_experience, job_education, company_name, company_type, company_status, company_people, job_tips, job_welfare):
    # 将数据写入数据库中
    try:
        cursor = db.cursor()
        sql = 'insert into job2(id, job_title, job_salary, job_city, job_experience, job_education, company_name, company_type, company_status, company_people, job_tips, job_welfare) values ("%d", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (id, job_title, job_salary, job_city, job_experience, job_education, company_name, company_type, company_status, company_people, job_tips, job_welfare);
        print(sql)
        cursor.execute(sql)
        print(cursor.lastrowid)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()


def get_message():
    for i in range(1, 50):
        print('第' + str(i) + '页')
        time.sleep(random.randint(10, 20))
        data = {
            'first': 'false',
            'pn': i,
            'kd': '数据分析'
        }
        s = requests.Session()
        s.get(url_start, headers=headers, timeout=3)
        cookie = s.cookies
        response = s.post(url=url_parse, data=data, headers=headers, proxies=proxies,cookies=cookie, timeout=3)
        time.sleep(5)
        response.encoding = response.apparent_encoding
        result = json.loads(response.text)
        job_messages = result['content']['positionResult']['result']
        for job in job_messages:
            global count
            count += 1
            # 岗位名称
            job_title = job['positionName']
            print(job_title)
            # 岗位薪水
            job_salary = job['salary']
            print(job_salary)
            # 岗位地点
            job_city = job['city']
            print(job_city)
            # 岗位经验
            job_experience = job['workYear']
            print(job_experience)
            # 岗位学历
            job_education = job['education']
            print(job_education)
            # 公司名称
            company_name = job['companyShortName']
            print(company_name)
            # 公司类型
            company_type = job['industryField']
            print(company_type)
            # 公司状态
            company_status = job['financeStage']
            print(company_status)
            # 公司规模
            company_people = job['companySize']
            print(company_people)
            # 工作技能
            if len(job['positionLables']) > 0:
                job_tips = ','.join(job['positionLables'])
            else:
                job_tips = 'None'
            print(job_tips)
            # 工作福利
            job_welfare = job['positionAdvantage']
            print(job_welfare + '\n\n')
            # 写入数据库
            add_Mysql(count, job_title, job_salary, job_city, job_experience, job_education, company_name, company_type, company_status, company_people, job_tips, job_welfare)


if __name__ == '__main__':
    get_message()