import requests  # 导入requests 模块
from bs4 import BeautifulSoup  # 导入BeautifulSoup 模块
from selenium import webdriver  # 导入Selenium的webdriver
from selenium.common.exceptions import TimeoutException
import os
import time
import re


class BeautifulPicture():
    def __init__(self):
        self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        self.web_url = 'http://tieba.baidu.com/f?kw=%E5%AD%99%E5%85%81%E7%8F%A0&ie=utf-8&pn='   # 初始url不带页码
        self.tieba_url = 'http://tieba.baidu.com'
        self.folder_path = "E:\PycharmProjects\picture"
        self.txt_path = os.path.join(self.folder_path, 'url.txt')

    def request(self, url):     # 网页请求接口
        r = requests.get(url, timeout=600)
        return r

    def mkdir(self, path):      # 创建目录
        path = path.strip()     # 去掉前后空格
        path = re.sub('[\/:*?"<>|]', '', path)      # 去掉文件名的非法字符
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            os.chdir(path)
            print('创建并切换至文文件夹%s' % path)
        else:
            print('%s的文件夹已经存在,不用再创建了!' % path)

    def get_files(self, path):      # 获取所有图片的图片名
        pic_names = os.listdir(path)
        return pic_names

    # def read_txt(self, path):       # 从txt文件读取所有帖子地址
    #     f = open(path, 'ab')
    #     for tiezi_url in f.readlines():
    #         return tiezi_url

    def save_img(self, url, file_name):      # 保存图片
        img = self.request(url)
        file_names = self.get_files(self.folder_path)
        if file_name in file_names:
            print("%s的图片已经存在!不用重新下载了" % file_name)
            return 0
        else:
            time.sleep(3)
            print('开始保存标签中图片%s' % file_name)
            f = open(file_name, 'ab')
            f.write(img.content)
            print('图片保存成功!')
            f.close()
            return 1

    def get_tiezi_url(self, path):      # 从网页获取所有帖子地址并保存至txt文件
        page_pn = 0
        f = open(path, 'a')
        print('开始网页的get请求')
        driver = webdriver.Chrome()
        while page_pn <= 11450:
            web_url_pn = self.web_url + str(page_pn)    # 带页码的url地址，实际每页的地址
            driver.get(web_url_pn)
            print('开始获取网页%s所有class为j_th_tit的a标签' % page_pn)
            all_a = BeautifulSoup(driver.page_source, 'lxml').find_all('a', class_='j_th_tit')
            for a in all_a:     # 循环a标签，并获取其中的帖子地址
                try:
                    tiezi_str = a['href']
                except KeyError:
                    print("没有找到srcset或title属性")
                else:
                    tiezi_url = self.tieba_url + tiezi_str
                    print("帖子地址%s" % tiezi_url)
                    f.write(tiezi_url)    # 将所有帖子地址保存到txt文件中
                    f.write('\n')
            page_pn = page_pn + 50

    def get_pic(self):      # 从各帖子地址中获取图片并保存
        print('开始创建图片文件夹')
        self.mkdir(self.folder_path)
        # #调用获取帖子方法，获取所有帖子地址
        # self.get_tiezi_url(self.txt_path)
        with open(self.txt_path, 'r') as f:
            tiezi_urls = f.readlines()
            for tiezi_url in tiezi_urls:
                tiezi_url = tiezi_url.split('\n')[0]        # 去掉地址中的换行符
                print('开始网页%s的get请求' % tiezi_url)
                try:
                    re = self.request(tiezi_url)
                except TimeoutException:
                    print("%s请求失败" % tiezi_url)
                else:
                    print('开始获取帖子标题......')
                    soup = BeautifulSoup(re.text, 'lxml')
                    img_title = soup.find('h1', class_='core_title_txt')['title']
                    print("获取帖子标题：%s" % img_title)
                    # 以该帖子标题作为该帖子中图片的存储目录名
                    pic_path = os.path.join(self.folder_path, img_title)
                    self.mkdir(pic_path)
                    print("开始获取所有img标签......")
                    all_a = soup.find_all('img', class_='BDE_Image')
                    for a in all_a:
                        try:
                            img_url = a['src']
                        except KeyError:
                            print("没有找到src属性")
                        else:
                            img_name = img_url[img_url.rfind('/') + 1:]
                            res = self.save_img(img_url, img_name)
                            if res == 0:
                                break

    def scroll_down(self, driver, height):
        # 执行JavaScript实现网页下拉倒底部
        driver.execute_script("window.scrollTo(0,%d);" % height)


beauty = BeautifulPicture()  # 创建类的实例
beauty.get_pic()    # 获取每个帖子中所有图片并保存
