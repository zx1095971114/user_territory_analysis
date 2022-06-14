from operator import imod
from time import sleep
from matplotlib.font_manager import json_dump, json_load
from requests import request
import requests
import scrapy
from selenium import webdriver
from yaml import parse
from bs4 import BeautifulSoup
from importlib.metadata import metadata
from weibo_project.items import WeiboProjectItem
from weibo_project.items import CommentItem
class WeibospiderSpider(scrapy.Spider):
    name = 'weiboSpider'

    start_urls = ['https://s.weibo.com/top/summary/']

    
    def start_requests(self):
        cookies = "login_sid_t=fb88840a5c2ebad61a5998b3da291385; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=3201104882332.868.1654741926705; SINAGLOBAL=3201104882332.868.1654741926705; ULV=1654741926709:1:1:1:3201104882332.868.1654741926705:; WBtopGlobal_register_version=2022060910; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh.6O3O_fW98sYRYf2fwTI35NHD95QfSKqcSKeNShqEWs4DqcjDi--ciKLhi-2Ri--NiKn0i-82i--Ri-isi-8Wi--4iKnNiKyheh5N1K.t; SSOLoginState=1654747716; SUB=_2A25PpQIUDeThGeNL7VQU8ynIzT6IHXVtaa5crDV8PUJbkNB-LVb-kW1NSNJowHemz3SFfRdogVei7q2wbzVUbVWl" #获取一个cookie
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies,
        )

    def parse(self, response):
        #print(response.body.decode(response.encoding))
        uls = response.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr')
        print("************************************************uls:")
        print(len(uls))
        i=0
        for ul in uls:
            if i>10:
                break
            if i==0:
                i+=1
                continue
            #print(ul)
            item = {}
            name = ul.xpath('./td[2]/a/text()').get()
            item['hot_order'] = i
            i+=1
            item['name'] = name;
            next_url = ul.xpath("./td[2]/a/@href").get()
            next_url = "https://s.weibo.com/"+next_url
            print(next_url)
            print(item)
            print("*****************")
            cookies = "login_sid_t=fb88840a5c2ebad61a5998b3da291385; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=3201104882332.868.1654741926705; SINAGLOBAL=3201104882332.868.1654741926705; ULV=1654741926709:1:1:1:3201104882332.868.1654741926705:; WBtopGlobal_register_version=2022060910; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh.6O3O_fW98sYRYf2fwTI35NHD95QfSKqcSKeNShqEWs4DqcjDi--ciKLhi-2Ri--NiKn0i-82i--Ri-isi-8Wi--4iKnNiKyheh5N1K.t; SSOLoginState=1654747716; SUB=_2A25PpQIUDeThGeNL7VQU8ynIzT6IHXVtaa5crDV8PUJbkNB-LVb-kW1NSNJowHemz3SFfRdogVei7q2wbzVUbVWl" #获取一个cookie
            cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
            yield scrapy.Request(url=next_url,callback=self.parse_detail,meta={'data':item},cookies=cookies)     
        print(len(uls))
    
    def parse_detail(self, response):
        #print(response.body.decode(response.encoding))
        #print(response.meta['data'])
        item = response.meta['data']

        cookies = "login_sid_t=fb88840a5c2ebad61a5998b3da291385; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=3201104882332.868.1654741926705; SINAGLOBAL=3201104882332.868.1654741926705; ULV=1654741926709:1:1:1:3201104882332.868.1654741926705:; WBtopGlobal_register_version=2022060910; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh.6O3O_fW98sYRYf2fwTI35NHD95QfSKqcSKeNShqEWs4DqcjDi--ciKLhi-2Ri--NiKn0i-82i--Ri-isi-8Wi--4iKnNiKyheh5N1K.t; SSOLoginState=1654747716; SUB=_2A25PpQIUDeThGeNL7VQU8ynIzT6IHXVtaa5crDV8PUJbkNB-LVb-kW1NSNJowHemz3SFfRdogVei7q2wbzVUbVWl" #获取一个cookie
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        # print("进入热搜详情页面：("+item['name']+")")         查看运行细节请取消注释此行

        username = response.xpath('.//*[@class="name"]/text()').extract_first()
        detail = response.xpath('.//*[@class="from"]/a[1]/@href').extract_first()
        weibo_id = response.xpath('.//*[@action-type="feed_list_item"]/@mid').extract_first()
        # print("weibo ID:\t" + weibo_id)           查看运行细节请取消注释此行
        # print("detail url:\t" + detail)           查看运行细节请取消注释此行
        # print("username\t" + username)            查看运行细节请取消注释此行

        
        headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        }
        
        params = {
        "flow" : 0,
        "is_reload" : 1,
        "id" : weibo_id,
        "is_show_bulletin" : 2,
        "is_mix" : 0,
        "max_id" : 0,
        "count" : 20,
        "uid" : 6512991534
        }
        count = 0
        while True : 
            r = requests.get(url = "https://weibo.com/ajax/statuses/buildComments",params = params,headers = headers)
            jsonObj = r.json()
            
            data = jsonObj["data"]
            max_id = jsonObj["max_id"]


            for item1 in data:
                comment_item = CommentItem()
                comment_item['hot_point_name'] = item['name']
                comment_item['hot_point_order'] = item['hot_order']
                comment_item['hot_point_auth_name'] = username
                comment_item['hot_point_weibo_id'] = weibo_id
                comment_item['hot_point_detail_url'] = 'https:' + detail
                user = item1["user"]
                userID = user["id"]
                userName = user["name"]
                userCity = user["location"]
                content = BeautifulSoup(item1["text"], "html.parser").text
                comment_item['comment_user_name'] = userName
                comment_item['comment_user_id'] = userID
                comment_item['comment_user_location'] = userCity
                comment_item['comment_user_content'] = content
                
                # print(comment_item)                                           查看运行细节请取消注释此行
                count+=1
                yield comment_item
            params["max_id"] = max_id
            if max_id == 0 or count>1000:
                break
            # # 评论id
            # comment_Id = item["id"]
            # # 评论内容
            
            # # 评论时间
            # created_at = item["created_at"]
            # # 点赞数
            # like_counts = item["like_counts"]
            # # 评论数
            # total_number = item["total_number"]
            
            # 评论者 id，name，city

        

        # driver = webdriver.Edge('D:\webDriver\edgedriver_win64\msedgedriver.exe')
        # secookie = "login_sid_t=fb88840a5c2ebad61a5998b3da291385; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=3201104882332.868.1654741926705; SINAGLOBAL=3201104882332.868.1654741926705; ULV=1654741926709:1:1:1:3201104882332.868.1654741926705:; wb_view_log=1920*10801; XSRF-TOKEN=d5i2zD5UWIuwQ4Fb3axOWPqm; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh.6O3O_fW98sYRYf2fwTI35NHD95QfSKqcSKeNShqEWs4DqcjDi--ciKLhi-2Ri--NiKn0i-82i--Ri-isi-8Wi--4iKnNiKyheh5N1K.t; SSOLoginState=1654747716; SUB=_2A25PpQIUDeThGeNL7VQU8ynIzT6IHXVtaa5crDV8PUJbkNB-LVb-kW1NSNJowHemz3SFfRdogVei7q2wbzVUbVWl; WBPSESS=qzAurrh_D58S_1mxjbwHKmo8q5jD5fY5V3uAmlK1s0bdTtzG9NSokRMKJb_sEzUsq5-3jDLBpbyesYbEs1PKME-ECVMhIqkxiNYOt4nWjaV3qK2-7Tmp9llRpiOLu1v3hUCMos-aI3s1Oz9P263XIA=="
        # driver.get('https://weibo.com')
        # time.sleep(6)
        # for i in secookie.split("; "):
        #     cookie_dict = {
        #         'name':i.split('=')[0],
        #         'value':i.split('=')[1],    
        #         "expires": "",
        #         'path': '/',
        #         'httpOnly': True,
        #         'HostOnly': False,
        #         'Secure': False               
        #     }
        #     driver.delete_cookie(cookie_dict['name'])
        #     driver.add_cookie(cookie_dict=cookie_dict)
        # driver.get(url='https:' + detail)
        # time.sleep(5)
        # driver.execute_script('window.scrollBy(0,1000)')
        # time.sleep(3)
        # element1 = driver.find_elements_by_xpath('//*[@class="info woo-box-flex woo-box-alignCenter woo-box-justifyBetween"]/div[1]/span')
        # driver.execute_script('window.scrollBy(0,1000)')
        # time.sleep(3)
        # driver.execute_script('window.scrollBy(0,1000)')
        # time.sleep(4)
        # driver.execute_script('window.scrollBy(0,1000)')
        # time.sleep(4)
        # driver.refresh()
        # driver.execute_script('window.scrollBy(0,1000)')
        # time.sleep(4)

        # driver.execute_script('window.scrollBy(0,1000)')
        # element = driver.find_elements_by_xpath('//*[@class="info woo-box-flex woo-box-alignCenter woo-box-justifyBetween"]/div[1]/span')

        # user_loc_list = []
        # print('$$$$$$$$$$$$$$$$$$$$$$$element:')
        # for el in element:
        #     user_loc_list.append(el.text)
        #     print(el.text)
        # print('$$$$$$$$$$$$$$$$$$$$$$$element1:')
        # for el in element1:
        #     user_loc_list.append(el.text)
        #     print(el.text)
        # print(user_loc_list)
        # print(len(user_loc_list))
        # #yield scrapy.Request(url='https:' + detail,callback=self.parse_location,meta={'data':item},cookies=cookies)
