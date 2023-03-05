# django 设计的公司网站
## 基本功能如下：


后台添加主页展示图片和产品：

![img_1.png](img_1.png)

留言功能：

![img_2.png](img_2.png)

产品筛选功能：

![img_3.png](img_3.png)

修改步骤：
1，删除自带数据库，db.splite3,

   进行数据迁移,执行命令

  python manage.py makemigrations

  python mange.py migrate

  创建超级用户

  python manage.py createsuperuser

2，修改留言功能的邮箱为自己的邮箱：

views.py:

![img_4.png](img_4.png)

settings.py:

![img_5.png](img_5.png)