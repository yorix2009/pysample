# coding: UTF-8



def show_rdd(rdd):
    print("*" * 20)
    print("RDD数据集：[{0}]".format(rdd.count()))
    print("-" * 20)
    rdd.foreach(lambda x: print('->', x,' type:',type(x)))
    print("*" * 20)


def show_maprdd(rdd):
    print("*" * 20)
    print("RDD数据集：[{0}]".format(rdd.count()))
    print("-" * 20)
    def printline(k):
        print("[%-10s] %s type:%s" % (k[0], k[1],type(k[1])))
    rdd.foreach(lambda k: printline(k))
    print("*" * 20)
