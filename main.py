from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
    role = request.args.get('role')
    type = request.args.get('type')
    han = request.args.get('han')
    fu = request.args.get('fu')
    print(role, type, han, fu)

    # 参照するCSVファイルをリクエストから判断
    path = 'CSV/point_'
    if role == 'oya':
        path += 'oya_'
    else:
        path += 'ko_'
    if type == 'ron':
        path += 'ron.csv'
    else:
        path += 'tumo.csv'
    print(path)

    # CSVファイルの読みこみ
    df = pd.read_csv(path,index_col=0)
    
    # 符と翻から得点を探す
    point_list = list(df.loc[:,fu])
    point = str(point_list[int(han)-1])
    
    #成功下かを表示する
    result = 'success!'
    print(result)
    return jsonify({'point':point})

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8888)