# spwb  
这个是一个存网站的仓库的。网站里面打算想放一些视频，由python的flask框架编写。  
**这个程序现在还不适合用于生产环境，必需等后期换一个服务器。**  




##访问方法
> __pip install -i https://pypi.tuna.tsinghua.edu.cn/simple python-dotenv Flask__  

1. 安装了python3，安装了Flask（如果没有上面这个指令可以一键安装）
2. 在app.py同级目录下创建文件".env"，并在里面加入这样一行内容".env"
3. 编辑电脑的环境变量"FLASK_ENV"(没有的创建)，设置其值为"development"，这样就可以使服务器处于开发调试状态
4. 运行app.py
5. 访问127.0.0.1:8888  


##目录结构  
> app.py是网站服务端主程序  
> template存的是网站的模板  
> static存的是网站的静态文件  

##注意事项  

###注意：
>由于flask使用jinja2作为模板渲染引擎，当需要有如超链接跳转时之类需要引用网站之内的网址时，比如要跳转到/test.html页面，最好别在href=""这里面填网址，而是填
"{{ url_for(test) }}"。要跳转到/p/hello.html页面，填"{{ url_for(hello) }}"。要跳转到主页，填"{{ url_for(index) }}"如果有特例会在这里说 。  

###特例：
+ 主页 -> {{url_for(index)}}  

## 更新日志
> 2020/6/26 
>> 创建仓库  
>> 添加第一个程序和页面  
>
> 2020/6/27
>> 创建了第一个测试网页  
>> 添加了更多测试网页，扩充网站内容  
## 未来的计划
> <不知道>  
> 存一些视频？  
  
没了