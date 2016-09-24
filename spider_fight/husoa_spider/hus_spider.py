# coding=utf-8
import json
import requests
import re
import bs4
import xlwt

url_check = 'http://oa.hsu.edu.cn/login/check.shtml'
url_main = 'http://oa.hsu.edu.cn/'
url_department = 'http://oa.hsu.edu.cn/sysman/deptanduserfortree/userslist.shtml?root=source'
url_teacher = 'http://oa.hsu.edu.cn/sysman/deptanduserfortree/userslist.shtml?root='
url_teacherinfo = 'http://oa.hsu.edu.cn//sysman/structure/edit_user.shtml?id='
s = requests.session()
cookie = None


def hus_save(school):
    position = 1
    hus = xlwt.Workbook()
    sheet = hus.add_sheet('sheet 1', cell_overwrite_ok=True)
    sheet.write(0, 0, '昵称'.decode('utf-8'))
    sheet.write(0, 1, '姓名'.decode('utf-8'))
    sheet.write(0, 2, 'id'.decode('utf-8'))
    sheet.write(0, 3, '职位'.decode('utf-8'))
    sheet.write(0, 4, 'email'.decode('utf-8'))
    sheet.write(0, 5, '办公室电话'.decode('utf-8'))
    sheet.write(0, 6, '手机'.decode('utf-8'))
    for depart in school:
        sheet.write(position, 0, depart['name'].encode('utf-8').decode('utf-8'))
        position += 1
        techers = depart['techer']
        for techer in techers:
            sheet.write(position, 0, techer['nickname'].encode('utf-8').decode('utf-8'))
            sheet.write(position, 1, techer['name'].encode('utf-8').decode('utf-8'))
            sheet.write(position, 2, techer['id'].encode('utf-8').decode('utf-8'))
            sheet.write(position, 3, techer['thtitle'].encode('utf-8').decode('utf-8'))
            sheet.write(position, 4, techer['email'].encode('utf-8').decode('utf-8'))
            sheet.write(position, 5, techer['officephone'].encode('utf-8').decode('utf-8'))
            sheet.write(position, 6, techer['phone'].encode('utf-8').decode('utf-8'))
            position += 1
    hus.save('hsu.xls')


def login():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://oa.hsu.edu.cn /login.shtml'
    }
    payload = {'user': 'wfx', 'pass': '9731629553', 'screen_width': '1366', 'screen_height': '768',
               'usertype': 'undefined'}
    proxies = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888"
    }
    try:
        check = json.loads(s.post(url_check, data=payload, headers=headers).text.encode('utf-8'))
        if check['success'] == 'success':
            response = s.get(url_main)
            response.encoding = 'utf-8'
            return response
        return None
    except requests.RequestException as e:
        print e
        return None


def get_teacherinfo(teacher_id):
    teacher = {}
    response = s.get(url_teacherinfo + str(teacher_id))
    response.encoding = 'utf-8'
    content = response.text
    soup = bs4.BeautifulSoup(content, 'lxml')
    teacherinfo = soup.select('span')
    teacherinfo = map(lambda x: x.get_text().strip(), teacherinfo)
    del teacherinfo[0]
    teacher['nickname'] = teacherinfo[0]
    teacher['id'] = teacherinfo[1]
    teacher['name'] = teacherinfo[2]
    teacher['thtitle'] = teacherinfo[3]
    teacher['email'] = teacherinfo[4]
    teacher['officephone'] = teacherinfo[5]
    teacher['phone'] = teacherinfo[6]
    return teacher


def get_teacher(college_id):
    tech = []
    pattern = re.compile(u'<a.*?\(\'(.*?)\'')
    response = s.get(url_teacher + str(college_id))
    response.encoding = 'utf-8'
    content = response.text
    teachers = json.loads(content)
    if len(teachers) > 0:
        for teacher in teachers:
            teacher_id = re.search(pattern, teacher['text']).group(1)
            teacherinfo = get_teacherinfo(teacher_id)
            tech.append(teacherinfo)
    return tech


def get_department():
    school = []
    pattern = re.compile(u'<a.*?>(.*?)</a>')
    response = s.get(url_department)
    response.encoding = 'utf-8'
    content = response.text
    colleges = json.loads(content)[0]['children']
    for college in colleges:
        colg = {}
        college_name = re.search(pattern, college['text']).group(1)
        print '正在收集:' + college_name.encode('utf-8')
        colg['name'] = college_name
        colg['techer'] = get_teacher(college['id'])
        print colg
        school.append(colg)
    return school


def main():
    response_login = login()
    if not response_login:
        print '登陆失败'
        exit()
    school = get_department()
    hus_save(school)
    # print response_login.encode('utf-8')

if __name__ == '__main__':
    main()
    # hus_save()