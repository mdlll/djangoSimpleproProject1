import redis
# 连接redis
# Redis的增删改查
class StringTest(object):
    def __init__(self):
        self.r = redis.StrictRedis(host='127.0.0.1', port=6379, )

    def test_set(self):
        ''' set -- 设置值 '''
        rest = self.r.set('name2', 'zhang')
        print(rest)
        return rest

    def test_get(self):
        '''get -- 获取值'''
        rest = self.r.get('name2')
        print(rest)
        return rest

    def test_mset(self):
        ''' mset -- 设置多个键值对 '''
        d = {
            'name3': 'Bob',
            'name4': 'Bobx'
        }
        rest = self.r.mset(d)
        print(rest)
        return rest

    def test_mget(self):
        ''' mset -- 设置多个键值对 '''
        d = ['name3', 'name4']
        rest = self.r.mget(d)
        print(rest)
        return rest

    def test_del(self):
        ''' del删除键值 '''
        rest = self.r.delete('name3')
        print(rest)

    '''
    CRM=客户关系中心
    和G有关的是政府government
    供应链是信息流，物流，商流和资金流的链
    EAI是企业内部的集成平台，包括平台，界面，数据库，流程和应用的集成
    软件开发模型：瀑布模型，演化模型（这是一个需求模糊模型），增量模型，螺旋模型，喷泉模型（这就是一个连需求都没有的模型），构件组装模型（这是一个拿来主义模型），
    V模型（瀑布模型增加迭代测试模型），RUP（Rational Unified Process，统一软件开发过程）中的软件生命周期在时间上被分解为四个顺序的阶段，分别是：初始阶段、细化阶段、构造阶段 和交付阶段 。
    内聚性弱到强：偶逻时过通顺功
    耦合性弱到强：非数标控外公内
    '''

    def test_renamenx(self):
        ''' renamenx修改key值 '''
        rest=self.r.renamenx('name4','name5')
        print(rest)
        return rest

    '''
    软件测试包括：单元，集成，确认，系统，验收
    CMM=软件能力成熟度模型，CMMI=软件能力成熟度集成模型（CMM升级版）
    UML=统一建模语言，https://www.cnblogs.com/jiangds/p/6596595.html
    软件架构：2C/S，3C/S和B/S（B是浏览器browser）
    SOA（Service-Oriented Architecture，面向服务的体系结构）是一个组件模型
    软件构建是三个流派：CORBA，EJB和DCOM
    中间件是指：远程过程调用，面向消息的中间件，对象请求代理，事务处理监控
    '''

    def test_push(self):
        ''' lpush/rpush -- 从左/右插入数据 '''
        t = ['Amy', 'Jhon']
        # 如果不加*则会把两个元素当做整体存入
        rest = self.r.lpush('l_eat3', *t)
        print(rest)
        rest = self.r.lrange('l_eat3', 0, -1)
        print(rest)

    def test_pop(self):
        ''' lpop/rpop 移除最左/右边的元素并返回值'''
        rest = self.r.lpop('l_eat3')
        print(rest)
        rest = self.r.lrange('l_eat3', 0, -1)
        print(rest)

    def test_rpush(self):
        ''' rpush插入一个或多个值再列表中'''
        x=['fruit','apple']
        rest = self.r.rpush('l_eat3',*x)
        print(rest)
        rest = self.r.lrange('l_eat3', 0, -1)
        print(rest)

class SetTest(StringTest):
    def test_sadd(self):
        ''' sadd --添加元素 '''
        l = ['cat', 'dog', 'monkey']
        rest = self.r.sadd('zoo2', *l)
        print(rest)
        rest = self.r.smembers('zoo2')
        print(rest)

    def test_srem(self):
        ''' srem -- 删除元素 '''
        rest = self.r.srem('zoo2', 'monkey')
        print(rest)
        rest = self.r.smembers('zoo2')
        print(rest)

    def test_sinter(self):
        ''' sinter --返回元素的交集 '''
        rest = self.r.sinter('zoo2', 'zoo1')
        print(rest)


def main():
    st = StringTest()
    st.test_set()
    st.test_get()
    st.test_mset()
    st.test_mget()
    st.test_del()
    st.test_renamenx()
    st.test_push()
    st.test_pop()
    st.test_rpush()

    set_test = SetTest()
    set_test.test_sadd()
    set_test.test_srem()
    set_test.test_sinter()


if __name__ == "__main__":
    main()
