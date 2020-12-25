import logging

from flask import current_app
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

from info import create_app, db



#  creat_app 类似工厂方法
app = create_app('developement')

# 创建命令行
# manager = Manager(app)

# 将app和db关联
Migrate(app, db)
# 将迁移命令添加到mannager
# manager.add_command('db', MigrateCommand)



if __name__ == "__main__":
    # manager.run()
    app.run(host="0.0.0.0", port=8080, debug=True)
