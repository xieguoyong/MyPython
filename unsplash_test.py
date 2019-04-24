import requests  # 导入requests 模块
from bs4 import BeautifulSoup  # 导入BeautifulSoup 模块
from selenium import webdriver  # 导入Selenium的webdriver
from selenium.webdriver.common.keys import Keys  # 导入Keys
import os
import time


class BeautifulPicture():
    def __init__(self):
        self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        self.web_url = 'https://unsplash.com'
        self.folder_path = "E:\PycharmProjects\MyPython\save_pic"

    def request(self, url):
        r = requests.get(url, timeout=3600)
        return r

    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字为%s的文件夹' % path)
            os.makedirs(path)
            print('创建成功!')
        else:
            print('%s的文件夹已经存在,不用再创建了!' % path)

    def get_files(self, path):
        pic_names = os.listdir(path)
        return pic_names

    def save_img(self, url, name):
        img = self.request(url)
        file_name = name + '.jpg'
        file_names = self.get_files(self.folder_path)
        if file_name in file_names:
            print("%s的图片已经存在!不用重新下载了" % file_name)
            return 0
        else:
            time.sleep(3)
            print('开始保存图片')
            f = open(file_name, 'ab')
            f.write(img.content)
            print('图片保存成功!')
            f.close()
            return 1

    def get_pic(self):
        print('开始创建文件夹')
        self.mkdir(self.folder_path)
        print('开始切换文件夹')
        os.chdir(self.folder_path)
        print('开始网页的get请求')
        # 使用selenium通过PhantomJS来进行网络请求
        driver = webdriver.Chrome()
        driver.get(self.web_url)
        for scr in range(100):
            print('开始获取所有的a标签')
            all_a = BeautifulSoup(driver.page_source, 'lxml').find_all('img', class_='_2zEKz')
            print(len(all_a))
            # for a in reversed(all_a):
            for a in reversed(all_a):
                try:
                    img_str = a['srcset']
                    # print(img_str)
                except KeyError:
                    print("没有找到srcset属性")
                else:
                    img_string = img_str[0:img_str.find('?')]
                    img_name = img_string[img_string.rfind('/') + 1:]
                    img_url = str(img_str).split(" ")[0]  # 截取其中的图片链接
                    print(img_string)
                    print(img_name)
                    print(img_url)
                    res = self.save_img(img_url, img_name)
                    if res == 0:
                        break
            self.scroll_down(driver=driver, height=(scr + 1) * 6000)

    def scroll_down(self, driver, height):
        # 执行JavaScript实现网页下拉倒底部
        driver.execute_script("window.scrollTo(0,%d);" % height)


beauty = BeautifulPicture()  # 创建类的实例
beauty.get_pic()  # 执行类中的方法