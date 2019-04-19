import os
import sys
import importlib


#参考网络上项目的一个根据目录动态加载其中的py文件并可调用对应的实例，来调用约定的方法


def Init(modules_dir_path):
    print("Init begin")
    abs_mod_dir_path = os.path.abspath(modules_dir_path)

    if not os.path.exists(modules_dir_path) or not os.path.exists(abs_mod_dir_path):
        print("Error: cannot find module path '{}'".format(abs_mod_dir_path))
        return None

    if not os.path.isdir(abs_mod_dir_path):
        print("Error: provided path is not a directory")
        return None

    return Manager(abs_mod_dir_path)


class Manager:
    def __init__(self, abs_module_path):
        #追加路径
        sys.path.insert(0, abs_module_path)
        self.module_dir_path = abs_module_path

        #字典存module
        self.module_list = {}
        #加载
        self.__load_modules_from_path(abs_module_path)
        #缓存生效
        importlib.invalidate_caches()

    #初始化把该路径下所有的py都加入
    def __load_modules_from_path(self, module_root_path):
        for dir_path, _, files in os.walk(module_root_path):
            for file in files:
                if file.endswith(".py"):
                    self.add_module(dir_path,os.path.splitext(file)[0])

    #刷新库
    def refresh_modules(self):
        self.__load_modules_from_path(self.module_dir_path)


    #添加一个模块,返回该模块
    def add_module(self,dir_path,file_name):
        #import_path eg: merchant2.module1.m2m1
        import_path = os.path.join(
            dir_path.replace(self.module_dir_path, "")[1:],
            file_name
        ).replace("/", ".").replace("\\", ".")
        # for windows is \\
        cur_module = self.module_list.get(import_path)
        if not cur_module:
            self.__load_module(import_path)
        elif cur_module and cur_module["mtime"] != os.path.getmtime(self.get_os_path(import_path)):
            self.__reload_module(import_path)
        return self.module_list.get(import_path)

    #按import路径返回
    def get_module(self,import_path):
        return self.module_list.get(import_path)
    def __load_module(self, module_path):
        module_class_name = module_path
        if module_path.count("."):
            module_class_name = module_path.split(".")[-1]
        #模块相关信息
        module = importlib.import_module(module_path)
        module_class = getattr(module, module_class_name.capitalize())
        module_instance = module_class()

        self.module_list[module_path] = {
            "ref": module,
            "instance": module_instance,
            "mtime": os.path.getmtime(os.path.join(self.get_os_path(module_path)))
        }
        # 调用初始化
        #module_instance.init()


    def __reload_module(self, module_path):
        importlib.reload(module_path)
        self.module_list[module_path]["mtime"] = os.path.getmtime(self.get_os_path( module_path))
        importlib.invalidate_caches()


    def get_os_path(self, module_path):
        module_path = module_path.replace(".", "/")
        module_path += ".py"

        return os.path.join(self.module_dir_path, module_path)


    def remove_module(self, module_path):

        module = self.module_list[module_path]["ref"]
        module.shutdown()
        del module
        del self.module_list[module_path]


    def run(self,parameters):
        for module in self.module_list.values():
            module["instance"].run(parameters)

    #获取module路径
    def get_module_path(self,os_path):
        os_path = os_path.replace(self.module_dir_path, "")
        if os_path[0] == "/":
            os_path = os_path[1:]
        os_path = os_path.replace("/", ".")
        return os.path.splitext(os_path)[0]

    #获取所有的module
    def get_modules(self):
        return self.module_list

if __name__ == '__main__':
    work_path = os.path.dirname(__file__) + "/dynamics/"
    #logger 在1 处导入，初始化时就可以走logger中的doLog(再根据环境是否print),在2处就走print
    #1 import logger
    moduleManager = Init(work_path)
    #实际开发中，一般在最上面import
    #2 import logger
    re2 = moduleManager.get_module("module1.m1m1")
    if re2:
        re2["instance"].execute("input parameter2")
    else:
        print("re2 is null ")
    pass

