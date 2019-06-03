import os
import sys
import importlib
import time
from logger import applog

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
        self.add_modules_from_path(abs_module_path)
        #缓存生效
        importlib.invalidate_caches()

    #初始化把该路径下所有的py都加入
    def add_modules_from_path(self, module_root_path):
        for dir_path, _, files in os.walk(module_root_path):
            for file in files:
                if file.endswith(".py"):
                    try:
                        self.add_module(dir_path, os.path.splitext(file)[0])
                    except Exception as err:
                        applog.error('Got an error ' + str(err),exc_info=True)
                        #doLog(str(err))


    #刷新库
    def refresh_modules(self):
        self.add_modules_from_path(self.module_dir_path)

    def add_module(self,dir_path,file_name):
        """
        添加一个模块,返回该模块
        :param dir_path: 'D:\\Python\\JDProject\\bohr\\modules\\merchant1\\module1'
        :param file_name: 'cdpmodel' or 'cdpmodel.py'
        :return:
        """
        #import_path eg: merchant1.module1.cdpmodel
        import_path = self.__get_module_path(dir_path,file_name)

        cur_module = self.module_list.get(import_path)
        if not cur_module:
            self.__load_module(import_path)
        elif cur_module and cur_module["mtime"] != os.path.getmtime(self.__get_os_path(import_path)):
            self.__reload_module(import_path)
        return self.module_list.get(import_path)


    def get_module(self,import_path):
        """
        按import路径返回
        :param import_path: 'merchant1.module1.cdpmodel'
        :return:
        """
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
            "mtime": os.path.getmtime(self.__get_os_path(module_path))
        }
        # 调用初始化
        #module_instance.init()


    def __reload_module(self, module_path):
        cur_module = self.module_list.get(module_path)
        #reload必须传入module类型，原来传入的module_path报错
        cur_module = importlib.reload(cur_module["ref"])
        if module_path.count("."):
            module_class_name = module_path.split(".")[-1]
        module_class = getattr(cur_module, module_class_name.capitalize())
        module_instance = module_class()

        self.module_list[module_path] = {
            "ref": cur_module,
            "instance": module_instance,
            "mtime": os.path.getmtime(self.__get_os_path(module_path))
        }
        #self.__load_module(module_path)
        applog.info("reload module_path" + str(module_path))
        importlib.invalidate_caches()


    def __get_os_path(self, module_path):
        module_path = module_path.replace(".", "/")
        module_path += ".py"

        return os.path.join(self.module_dir_path, module_path)


    def remove_module(self, module_path):
        module = self.module_list[module_path]["ref"]
        del module
        del self.module_list[module_path]



    #获取module路径
    def __get_module_path(self,dir_path,file_name):
        dir_path.replace(self.module_dir_path, "")[1:]
        if file_name.endswith('.py'):
            file_name = os.path.splitext(file_name)[0]
        import_path = os.path.join(
            dir_path.replace(self.module_dir_path, "")[1:],
            file_name
        ).replace("/", ".").replace("\\", ".")        # for windows is \\

        return import_path

    #获取所有的module
    def get_modules(self):
        re_list = {}
        for key in self.module_list.keys():
            re_list[key] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.module_list[key]['mtime']))
        return re_list

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

