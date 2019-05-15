import requests  # 导入requests 模块
from bs4 import BeautifulSoup  # 导入BeautifulSoup 模块
from selenium.common.exceptions import TimeoutException
import os
import time
import re
import threading

g_lock = threading.Lock()  # 初始化一个锁
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
web_url = 'http://tieba.baidu.com/f?kw=%E5%AD%99%E5%85%81%E7%8F%A0&ie=utf-8&pn='  # 初始url不带页码
tieba_url = 'http://tieba.baidu.com'
folder_path = "E:\PycharmProjects\picture"
txt_path = os.path.join(folder_path, 'url.txt')

with open(txt_path, 'r') as f:
    tiezi_urls = f.readlines()
    tiezi_urls.reverse()    # 倒序排，因为后面用到的pop()是删除列表最后一个，而我只想根据原列表第一个开始删


def request(url):  # 网页请求接口
    r = requests.get(url, timeout=600)
    return r


def mkdir(path):  # 创建目录
    path = path.strip()  # 去掉前后空格
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print('创建文件夹%s' % path)
        # os.chdir(path)  # 切换至创建的文件夹
    else:
        print('%s的文件夹已经存在,不用再创建了!' % path)
        # os.chdir(path)  # 切换至已有的文件夹


def get_files(path):  # 获取所有图片的图片名
    pic_names = os.listdir(path)
    return pic_names

# def read_txt(self, path):       # 从txt文件读取所有帖子地址
#     f = open(path, 'ab')
#     for tiezi_url in f.readlines():
#         return tiezi_url


def save_img(url, file_name, path):      # 保存图片
    img = request(url)
    file_names = get_files(folder_path)
    if file_name in file_names:
        print("%s的图片已经存在!不用重新下载了" % file_name)
        return 0
    else:
        time.sleep(1)
        print('开始保存标签中图片%s' % file_name)
        f = open(os.path.join(path, file_name), 'ab')
        f.write(img.content)
        print('图片保存成功!')
        f.close()
    return 1


class BeautifulPicture(threading.Thread):
    def run(self):      # 从各帖子地址中获取图片并保存
        while True:
            g_lock.acquire()
            if len(tiezi_urls) > 0:
                tiezi_url = tiezi_urls.pop()
                tiezi_url = tiezi_url.split('\n')[0]        # 去掉地址中的换行符
                g_lock.release()
                print('开始网页%s的get请求' % tiezi_url)
                try:
                    resp = request(tiezi_url)
                except TimeoutException:
                    print("%s请求失败" % tiezi_url)
                else:
                    print('开始获取帖子标题......')
                    soup = BeautifulSoup(resp.text, 'lxml')
                    img_title = soup.find('h1', class_='core_title_txt')['title']
                    img_title = re.sub('[\/:*?"<>|]', '', img_title)      # 去掉作为文件名不允许的非法字符
                    print("获取帖子标题：%s" % img_title)
                    # 以该帖子标题作为该帖子中图片的存储目录名
                    pic_path = os.path.join(folder_path, img_title)
                    mkdir(pic_path)
                    print("开始获取所有img标签......")
                    all_a = soup.find_all('img', class_='BDE_Image')
                    for a in all_a:
                        try:
                            img_url = a['src']
                        except KeyError:
                            print("没有找到src属性")
                        else:
                            g_lock.acquire()
                            img_name = img_url[img_url.rfind('/') + 1:]
                            res = save_img(img_url, img_name, pic_path)
                            g_lock.release()
                            if res == 0:
                                break
            else:
                print("爬虫运行完毕！")
                g_lock.release()
                break


for i in range(4):
    beauty = BeautifulPicture()      # 创建类的实例
    beauty.start()

