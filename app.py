from flask import Flask

FAI=Flask(__name__)
@FAI.route('/wish/<na>')

def wish(na):
    return f'hello world:{na}'

if __name__==('__main__'):
    FAI.run(debug=True,port=5001,host='127.0.0.1')