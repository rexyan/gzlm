### 本地环境开发
1. 下载项目
```shell
git clone git@github.com:rexyan/gzlm.git
```

2. 安装依赖
```shell
pip install -r requirements.txt 
```

3. 同步表结构
```shell
python manage.py makemigrations
python manage.py migrate
```

4. 启动项目
```shell
python manage.py runserver 8000
```

5. 创建超级管理员
```
python manage.py createsuperuser  # 创建
python manage.py changepassword username  # 修改密码
```

### 导入数据
将一个或者多个 xlsx 数据文件放到 data 目录下，执行以下命令导入数据
```shell
python data/import_data.py
```
命令输出
```
正在读取文件：xxx.xlsx
读取文件：xxx.xlsx, 共写入数据 18 条
正在读取文件：xxx.xlsx2.xlsx
读取文件：xxx.xlsx2.xlsx, 共写入数据 18 条
```

### 切换数据库
在 BMS/setting.py 文件中进行设置
使用 sqlite3
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

使用 MySQL
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bms',  # 数据库名
        'HOST': '127.0.0.1',   # 数据库地址
        'PASSWORD': '123456',  # 数据库密码
        'PORT': 3306,   # 数据库端口
        'USER': 'root', # 数据库账号
    }
}
```

### 分页设置
在 BMS/setting.py 文件中进行设置
```
PAGE_SIZE = 20
```

