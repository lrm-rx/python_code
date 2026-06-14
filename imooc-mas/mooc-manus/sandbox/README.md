启动: docker-compose -f .devops/docker-compose.yml up -d --build

uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload

使用插件远程ssh: ssh <用户名>@localhost -p 2222

激活虚拟环境: source ../venv/bin/activate
退出虚拟环境: deactivate