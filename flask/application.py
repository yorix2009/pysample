from flask import Flask
from flask import request
from flask import render_template
import json

"""
基于Flask的Python模块
"""
app = Flask(__name__)

@app.route('/')
def hello_world():
    env=request.environ;
    for x in env:
        print(x,env[x])
    app.logger.debug('A value for debugging')
    print(123, __name__)
    x, y = func(2, 4)
    print(x, y)
    env['json']=json.dumps(env)
    return render_template('hello.html',**env)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return '用户 %s' % username


def func(x, y):
    return x ** 2, y ** 2


if __name__ == '__main__':
    app.run(debug=True)
