## 技巧

#### 方法一:

- 查看当前项目所安装的包: pip freeze
- 将项目所有依赖的包(无论有没有使用到)导出到指定的文件(如: requirements.txt文件): pip freeze > requirements.txt

#### 方法二:

首先安装：

> ```
> pip install --no-deps pipreqs
> pip install yarg==0.1.9 docopt==0.6.2
> ```

然后执行: pipreqs --encoding=utf-8 --ignore venv --force

> 安装依赖包
> pin install -r requirements.txt

























