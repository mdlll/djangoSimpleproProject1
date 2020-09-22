from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import RedirectView, TemplateView
from pure_pagination import PaginationMixin

from ap1.models import ap1Person


def ap1View1(request):
    print('where will print?\nIn the running place.')
    vaa = {'title1': '传递content'}
    vbb = {'title2': '传递所有content'}
    # return render(request, 'ap1View/index1.html', context=vaa)
    # 用local的方式可以一次性传递所有，更加方便
    return render(request, 'ap1View/index1.html', locals())


def ap1View2(request):
    return render(request, 'ap1View/index2.html')


def ap1TimeView(request, year, month, day):
    return HttpResponse(str(year) + ':' + str(month) + ':' + str(day))


def ap1TimeView2(request, day):
    return HttpResponse('路由之外：' + day)


def appTimeView3(request, year):
    return HttpResponse('正则表达式：' + str(year))


def ap1ResponView(request):
    valua = '<h1>respon</h1>'
    # 状态码默认200，其余状态码可以查书Django59页
    # 改成400好像也没影响
    # HTTPResponse的方式要用字符串方式传递
    return HttpResponse(valua, status=200)


class ap1TemplateView(TemplateView):
    template_name = 'ap1View/index2.html'  # 模板文件文件名
    template_engine = None  # 解析模板文件的模板引擎
    content_type = None  # 设置HTTP的请求响应，一般用默认值
    extra_context = {'title': 'This is GET'}  # ？书里没说

    # 重新定义末班上下文获取方式
    def get_context_data(self, **kwargs):
        # 调用模板上下文文件，传递视图函数，再由模板引擎转为HTML网页文件
        context = super(ap1TemplateView, self).get_context_data(**kwargs)
        context['value'] = 'I am mmm'
        return context

    def post(self, request, *args, **kwargs):
        # 用于处理响应
        self.extra_context = {'title': 'a post'}
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class ap1ListView(ListView):
    # 设置模板文件，页面渲染
    template_name = 'ap1View/indexList.html'
    # 设置模型外的数据
    extra_context_param = {'title': '人员信息表'}
    # 设置查询模型
    queryset = ap1Person.objects.all()
    # 设置每页展示一条
    paginate_by = 1
    # 对queryset查询的数值返回值，默认为:ap1PerSon_list
    context_object_name = 'ap1PerSon_i'


class ap1DetailView(DetailView):
    # 设置模板文件，页面渲染
    template_name = 'ap1View/indexList.html'
    # 设置模型外的数据
    extra_context_param = {'title2': '人员信息表2'}
    # 设置查询字段
    slug_field = 'age'
    # 设置路由变量，和field联合
    slug_url_kwarg = 'age'
    pk_url_kwarg = 'pk'
    # 设置查询模型
    model = ap1Person
    # 设置查询模型,操作
    queryset = ap1Person.objects.all()
    # 对queryset查询的数值返回值，默认为:ap1PerSon_list
    context_object_name = 'ap1DetailView_i'
