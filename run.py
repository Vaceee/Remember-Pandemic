from src import app

if __name__ == "__main__":
    app.run(host='localhost', port=8888, debug=True)

'''
- 从flask0.11版本开始，建议通过命令行启动程序，而不再使用app.run()
  在本项目中使用命令行启动有利于强调程序模块性和组织文件关系(如静态资源存储)，且不受当前所在路径的影响
- Windows:
    - set FLASK_APP = `path_to_app`     #本项目为src/__init__.py
    - set FLASK_ENV = production|development
    - flask run --host `hostIP` --port `portNumber`
- Linux:
    - export FLASK_APP = `path_to_app`
    - export FLASK_ENV = production|development
    - flask run --host `hostIP` --port `portNumber`
# If the FLASK_ENV is set to development, the flask command will enable debug mode and
# flask run will enable the interactive debugger and reloader.

- 除了每次使用命令行配置环境之外，可以配置.env或.flaskenv文件，flask会自动应用其中的配置
  此功能需要一个Python虚拟环境管理工具`python-dotenv`的支持
  ```pip install python-dotenv```
- .env或.flaskenv所在的路径会成为flask应用的根路径，所以请将.env文件放在/src路径下并在此路径或其子目录运行`flask run`
- .env的配置覆盖.flaskenv的配置，命令行配置覆盖.env的配置
- 官方建议.flaskenv文件中配置公共变量，可以同步到仓库，而.env文件中配置私有变量，应该添加到.gitignore
'''
