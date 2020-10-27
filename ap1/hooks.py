# token produce
# 原理:
# 通过hmac sha1 算法产生用户给定的key和token的最大过期时间戳的一个消息摘要，将这个消息摘要和最大过期时间戳通过":"拼接起来，再进行base64编码，生成最终的token
import base64
import hmac
import json
import os
import time

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoSimpleproProject1.settings'
django.setup()
from ap1.models import midAdmin, midCommunity, midCompany, midBuilding, midUnit, midRoom, midInhabitant


def generate_token(key, expire=3600):
    r'''
        @Args:
            key: str (用户给定的key，需要用户保存以便之后验证token,每次产生token时的key 都可以是同一个key)
            expire: int(最大有效时间，单位为s)
        @Return:
            state: str
    '''
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    sha1_tshexstr = hmac.new(key.encode("utf-8"), ts_byte, 'sha1').hexdigest()
    token = ts_str + ':' + sha1_tshexstr
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
    return b64_token.decode("utf-8")


# 原理:
# 将token进行base64解码,通过token得到token最大过期时间戳和消息摘要。判断token是否过期。
# 如没过期才将 从token中的取得最大过期时间戳进行hmac sha1 算法运算(注意这里的key要与产生token的key要相同)，最后将产生的摘要与通过token取得消息摘要进行对比，
# 如果两个摘要相等，则token有效，否则token无效 。
def certify_token(key, token):
    """
    :param key: str
    :param token: str
    :return:  boolean
    """

    token_str = base64.urlsafe_b64decode(token).decode('utf-8')
    token_list = token_str.split(':')
    if len(token_list) != 2:
        return False
    ts_str = token_list[0]
    if float(ts_str) < time.time():
        # token expired
        return False
    known_sha1_tsstr = token_list[1]
    sha1 = hmac.new(key.encode("utf-8"), ts_str.encode('utf-8'), 'sha1')
    calc_sha1_tsstr = sha1.hexdigest()
    if calc_sha1_tsstr != known_sha1_tsstr:
        # token certification failed
        return False
        # token certification success
    return True


def add(content):
    # 新增管理员
    ss = json.loads(content)  # 转为dict
    midAdmin.objects.create(**ss)

def mdf(content):
    # 修改管路员
    ss = json.loads(content)  # 转为dict
    midAdmin.objects.filter(id=ss['id']).update(**ss)

def mdf_pwd(content):
    # 修改管理员密码
    ss = json.loads(content)  # 转为dict
    midAdmin.objects.filter(id=ss['id']).update(**ss)


def admin_del(content):
    # 删除管理员
    ss = json.loads(content)  # 转为dict
    midAdmin.objects.filter(id=ss['id']).delete()


def corp_add(content):
    # 公司新增
    ss = json.loads(content)  # 转为dict
    midCompany.objects.create(**ss)

def corp_mdf(content):
    # 公司修改
    ss = json.loads(content)  # 转为dict
    midCompany.objects.filter(id=ss['id']).update(**ss)

def corp_del(content):
    # 公司删除
    ss = json.loads(content)  # 转为dict
    midCompany.objects.filter(id=ss['id']).delete()


def community_add(content):
    # 小区新增
    ss = json.loads(content)  # 转为dict
    midCommunity.objects.create(**ss)

def community_mdf(content):
    # 小区修改
    ss = json.loads(content)  # 转为dict
    midCommunity.objects.filter(id=ss['id']).update(**ss)

def community_del(content):
    # 小区删除
    ss = json.loads(content)  # 转为dict
    midCommunity.objects.filter(id=ss['id']).delete()


def building_add(content):
    # 楼栋新增
    ss = json.loads(content)  # 转为dict
    midBuilding.objects.create(**ss)

def building_mdf(content):
    # 楼栋修改
    ss = json.loads(content)  # 转为dict
    midBuilding.objects.filter(id=ss['id']).update(**ss)

def building_del(content):
    # 楼栋删除
    ss = json.loads(content)  # 转为dict
    midBuilding.objects.filter(id=ss['id']).delete()

def unit_add(content):
    # 单元新增
    ss = json.loads(content)  # 转为dict
    midUnit.objects.create(**ss)

def unit_mdf(content):
    # 单元修改
    ss = json.loads(content)  # 转为dict
    midUnit.objects.filter(id=ss['id']).update(**ss)

def unit_del(content):
    # 单元删除
    ss = json.loads(content)  # 转为dict
    midUnit.objects.filter(id=ss['id']).delete()

def house_add(content):
    # 房屋新增
    ss = json.loads(content)  # 转为dict
    midRoom.objects.create(**ss)

def house_mdf(content):
    # 房屋修改
    ss = json.loads(content)  # 转为dict
    midRoom.objects.filter(id=ss['id']).update(**ss)

def house_del(content):
    # 房屋删除
    ss = json.loads(content)  # 转为dict
    midRoom.objects.filter(id=ss['id']).delete()

def resident_add(content):
    # 住户新增
    ss = json.loads(content)  # 转为dict
    midInhabitant.objects.create(**ss)

def resident_mdf(content):
    # 住户修改
    ss = json.loads(content)  # 转为dict
    midInhabitant.objects.filter(id=ss['id']).update(**ss)

def resident_del(content):
    # 住户删除
    ss = json.loads(content)  # 转为dict
    midInhabitant.objects.filter(id=ss['id']).delete()


def action(result):
    ss = json.loads(result)  # 转为dict
    code = ss['syncType']
    if code!="del":
        eval(code)(result)  # 字符串调用执行方法
    else:
        admin_del(result)
    print('?')


if __name__=='__main__':
    action(
        '{"email":"lsq28657638@gmail.com","familyName":"超级","id":"1","idCard":"450103198809180013","lastName":"管理员","mobile":"18577866246","sex":"1","syncType":"del"}')
