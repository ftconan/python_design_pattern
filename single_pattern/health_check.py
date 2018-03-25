# coding = utf-8


class HealthCheck(object):
    """
    服务器列表监控类
    """
    _instance = []

    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck._instance

    def __init__(self):
        self.servers = []

    def add_server(self):
        self.servers.append("Server 1")
        self.servers.append("Server 2")
        self.servers.append("Server 3")
        self.servers.append("Server 4")

    def change_server(self):
        self.servers.pop()
        self.servers.append("Server 5")


if __name__ == '__main__':
    hc1 = HealthCheck()
    hc2 = HealthCheck()

    hc1.add_server()
    print("Schedule health check for servers (1) ...")
    for i in range(4):
        print("Checking ", hc1.servers[i])

    hc2.change_server()
    print("Schedule health check for servers (2) ...")
    for i in range(4):
        print("Checking ", hc2.servers[i])
