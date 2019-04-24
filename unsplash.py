import requests
import os
import time
from bs4 import BeautifulSoup


class BeautifulPicture():
    def __init__(self):
        self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        self.web_url = "https://unsplash.com/"
        self.save_path = "E:\PycharmProjects\MyPython\save_pic"

    def get_pic(self):
        # 先创建图片保存目录
        self.mkdir(self.save_path)
        # 再获取图片并保存
        print("正在爬取图片，请稍候......")
        re = self.request(self.web_url, self.headers)       # 访问web_url
        all_a = BeautifulSoup(re.text, 'lxml').find_all('img', class_='_2zEKz')     # 获取网页中所有class为_2zEKz的标签
        print(len(all_a))
        for a in all_a:     # 循环每个标签，找到其中的图片链接并打开保存为文件
            print(a)
            # img_url = a.get('srcset')       # 获取srcset属性值
            try:
                img_url = a['srcset']
            except KeyError:
                print("没有找到srcset属性")
            else:
                img_url = str(img_url).split(" ")[0]    # 截取其中的图片链接
                if img_url == 'None':       # 因截取的链接会出现None，这里处理掉为None的数据
                    pass
                elif 'photo' not in img_url:
                    pass
                else:
                    print("爬取图片链接%s" % img_url)
                    self.save_pic(img_url)

    # 调用requests请求页面，返回response
    def request(self, url, headers):
        re = requests.get(url, headers)
        return re

    # 创建图片保存目录
    def mkdir(self, path):
        if not os.path.exists(path):
            os.mkdir(path)
            print("文件目录%s创建成功!" % path)
        else:
            print("图片保存目录已经存在！")

    # 从图片链接中截取图片名
    def cut_picname(self, url):
        first_pos = str(url).index('com/') + 4      # 取'com/'的索引，+4表示/后的一个字符
        end_pos = str(url).index('?')       # 取'？'的索引
        name = url[first_pos:end_pos]       # 从url中截取从first_pos起始至end_pos前一个字符截止的字符串
        pic_name = name + '.jpg'     # 以截取的字符串 加上后缀.jpg作为图片文件名
        return pic_name

    # 图片保存，且截取url中部分作为文件名
    def save_pic(self, url):
        pic_name = self.cut_picname(url)
        pic_dir = os.path.join(self.save_path, pic_name)       # 拼接上图片保存目录
        print("开始保存图片....")
        img = self.request(url, self.headers)
        time.sleep(3)       # 设置一个等待时间，等待图片加载完成
        op = open(pic_dir, 'ab')       # 打开图片文件
        op.write(img.content)       # 把img写入图片文件
        print("图片%s保存成功！" % pic_name)
        op.close()


picture = BeautifulPicture()
picture.get_pic()



