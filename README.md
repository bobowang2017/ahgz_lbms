# APP开发流程
1、在控制台进入虚拟环境，然后进入当前项目路径下
2、利用命令创建APP：python manage.py startapp XXX_app
3、在setting.py文件中INSTALLED_APPS中注册添加的APP
4、model层的编写，参照test_app模块中的models.py
5、serializer层的编写，参照test_app模块中的serializer.py
6、core层的编写，参照test_app模块中的core.py
7、view层的编写，参照test_app模块中的view.py
8、url层的编写，参照test_app模块中的urls.py
9、同步数据库操作
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---- python manage.py makemigrations app_name
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---- python manage.py migrate app_name
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---- 如果上述命令后面不加app_name，则默认同步全部数据库
10、利用RestClient测试开发的模块
11、提交代码


# 开发规范

## 命名规范
1、view层命名规范：XyzView(eg:UserView)
2、core层命名规范：小写横杠连接(eg:get_user_by_id)
3、model层命名规范：以对象的英文单词命名，如有多词采用拼接(eg: User、Role、UserRoleMapping)
4、app的命名统一加上后缀“_app”：user_app、common_app、privilege_app
