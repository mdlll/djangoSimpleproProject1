# 将所有属于这个app的路由都放进来
from django.urls import path, re_path

import ap1
from . import views
from .views import ap1ListView

urlpatterns = [
    # 跳转到views视图
    path('', views.ap1View1),
    # 这个的意思是，可以自由定义输入的路由，按照年/月/日三个数字输入的格式，会在页面响应，如果参数对应不上，会响应失败
    path('<year>/<int:month>/<slug:day>', views.ap1TimeView),
    # 添加路由地址之外的变量
    path('ap1/', views.ap1TimeView2, {'day': '2020.20.20'}),
    #     正则表达式（）小括号进行控制，？P是标配，<变量名>，[0-9]{4}代表取值0-9且长度只为4
    re_path('ap1/(?P<year>[0-9]{4}/)', views.appTimeView3),
    #     响应方式的不同
    path('ap1/a1/', views.ap1ResponView),
    # 基础视图templateView
    path('ap1/a2/', views.ap1TemplateView.as_view(), name='ap1TemplateView'),
    # listViews视图
    path('ap1/a3/', ap1.views.ap1ListView.as_view(), name='ap1ListView'),
    # detailView
    path('ap1/a4/<pk>/<age>', ap1.views.ap1DetailView.as_view(), name='ap1Detail'),
    # formView
    path('ap1/a5/', ap1.views.ap1FormView.as_view(), name='ap1Form'),
    path('ap1/a5/result', views.result, name='result'),
    # createView
    path('ap1/a6/', ap1.views.ap1CreateView.as_view(), name='ap1Create'),
    path('ap1/a6/result', views.result, name='result'),
    # updateView
    path('<age>.html', ap1.views.ap1UpdateView.as_view(), name='ap1Update'),#查询age必须唯一
    path('result', views.result, name='result'),
]
