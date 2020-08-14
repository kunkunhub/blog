#-*- 配置文件 -*-#

import os
import sys
from spwb import app

WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

SQLALCHEMY_DATABASE_URI = prefix + os.path.join(
    app.root_path, 'data.db'
)
# 关闭对模型修改的监控
SQLALCHEMY_TRACK_MODIFICATIONS = False