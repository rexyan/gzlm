### 本地环境开发
1. 下载项目
```
git clone git@github.com:rexyan/gzlm.git
```

2. 安装依赖
```
pip install -r requirements. txt 
```

3. 同步表结构
```
python manage.py makemigrations
python manage.py migrate
```

3. 启动项目
```
python manage.py runserver 8000
```

### 导入数据


### 切换数据库
BMS/setting.py 
```
使用 sqlite3
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



