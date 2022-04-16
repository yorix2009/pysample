# coding: utf-8
from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
from flask import send_file
from io import BytesIO
import json
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
import matplotlib.font_manager as fm
import numpy as np
import base64
import sys
from scipy.fftpack import fft, ifft

"""
基于Flask的Python模块
"""
app = Flask(__name__)


@app.route('/')
def hello_world():
    env = request.environ
    for x in env:
        print(x, env[x])
    app.logger.debug('A value for debugging')
    print(123, __name__)
    x, y = func(2, 4)
    print(x, y)
    # env['json']=json.dumps(env)
    return render_template('hello.html', **env)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return '用户 %s' % username

"""
输出图片的例子
"""
@app.route('/img')
def out_image():
    # 设置matplotlib在后台运行，不显示前台GUI
    plt.switch_backend('agg')
    # 防止处理中文出现错误
    reload(sys)
    sys.setdefaultencoding('utf-8')
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    mpl.rcParams['axes.unicode_minus'] = False  # 显示负号
    # 根据需要手工选择字体
    zhfont1 = fm.FontProperties(fname='/Users/jiangfy/simhei.ttf')
    # Data for plotting
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    # Note that using plt.subplots below is equivalent to using
    # fig = plt.figure and then ax = fig.add_subplot(111)
    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel=unicode('时间 (s)','UTF-8'), ylabel=unicode('电压 (mV)','utf-8'), title=unicode('Matplot测试','utf-8'))
    ax.grid()
    # return send_file(pltAsImg(plt), mimetype='image/jpg')
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    response = make_response(img.getvalue())
    response.headers['Content-Type'] = 'image/png'
    img.close()
    return response


"""
快速傅里叶变换测一个例子
"""
@app.route('/ftt')
def out_fttimage():
    plt.switch_backend('agg')
    reload(sys)
    sys.setdefaultencoding('utf-8')
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    mpl.rcParams['axes.unicode_minus'] = False  # 显示负号
    zh = fm.FontProperties(fname='/Users/jiangfy/simhei.ttf')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    # 采样点选择1400个，因为设置的信号频率分量最高为600赫兹，根据采样定理知采样频率要大于信号频率2倍，所以这里设置采样频率为1400赫兹（即一秒内有1400个采样点，一样意思的）
    x = np.linspace(0, 1, 1400)

    # 设置需要采样的信号，频率分量有200，400和600
    y = 7 * np.sin(2 * np.pi * 200 * x) + 5 * np.sin(2 * np.pi * 400 * x) + 3 * np.sin(2 * np.pi * 600 * x)

    fft_y = fft(y)  # 快速傅里叶变换

    N = 1400
    x = np.arange(N)  # 频率个数
    half_x = x[range(int(N / 2))]  # 取一半区间

    abs_y = np.abs(fft_y)  # 取复数的绝对值，即复数的模(双边频谱)
    angle_y = np.angle(fft_y)  # 取复数的角度
    normalization_y = abs_y / N  # 归一化处理（双边频谱）
    normalization_half_y = normalization_y[range(int(N / 2))]  # 由于对称性，只取一半区间（单边频谱）

    plt.subplot(231)
    plt.plot(x, y)
    plt.title(unicode('原始值', 'UTF-8'), fontsize=9)

    plt.subplot(232)
    plt.plot(x, fft_y, 'black')
    plt.title(unicode('双边振幅谱(未求振幅绝对值)', 'UTF-8'), fontsize=9, color='black')

    plt.subplot(233)
    plt.plot(x, abs_y, 'r')
    plt.title(unicode('双边振幅谱(未归一化)', 'UTF-8'), fontsize=9, color='red')

    plt.subplot(234)
    plt.plot(x, angle_y, 'violet')
    plt.title(unicode('双边相位谱(未归一化)', 'UTF-8'), fontsize=9, color='violet')

    plt.subplot(235)
    plt.plot(x, normalization_y, 'g')
    plt.title(unicode('双边振幅谱(归一化)', 'UTF-8'), fontsize=9, color='green')

    plt.subplot(236)
    plt.plot(half_x, normalization_half_y, 'blue')
    plt.title(unicode('单边振幅谱(归一化)', 'UTF-8'), fontsize=9, color='blue')
    #plt.savefig('1.pdf')
    # 输出图片
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    response = make_response(img.getvalue())
    response.headers['Content-Type'] = 'image/png'
    img.close()
    return response


def func(x, y):
    return x ** 2, y ** 2


def pltAsImg(plt):
    img = BytesIO()
    plt.savefig(img, format='jpg')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode('utf8')


if __name__ == '__main__':
    app.run(debug=True)
