# import json
# from APP import APP
# from flask import Flask, request, render_template
# from search_api import Seach
# from Parser import Data
# from Tables.liks_db import Medication

# app = APP().app
# search = Seach()
# last_query = {"name": None,
#               "url": None,
#               "manufacturer": None,
#               "composition": None,
#               "popular_name": None,
#               "expiration_date": None,
#               "prescription": None,
#               "type": None}


# @app.route('/')
# def home():
#     return render_template('index.html')


# @app.route('/info')
# def liks():
#     return render_template('info.html', my_list=last_query)


# @app.route('/save')
# def save():
#     return render_template('save.html')


# @app.route('/search_name_test', methods=["POST"])
# def search_name():

#     # p = json.loads(str(request.data))
#     string = request.json["med"]
#     print(string)

#     # data = search.search_by_name(string.lower())
#     # print(data)
#     # results = {'results': []}
#     # #
#     # # for i in data:
#     # #     results['results'].append(Data.toJSon(i))
#     # print(results)
#     return ""


# @app.route('/search_contains', methods=["POST"])
# def search_contains():
#     string = request.form["contains"]

#     data = search.search_by_component(string.lower())
#     results = {'results': []}

#     for i in data:
#         results['results'].append(Data.toJSon(i))

#     return  render_template('info.html', my_list=results) #results


# if __name__ == '__main__':
#     app.run(host="10.10.225.248",port=5000, debug=True)

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
