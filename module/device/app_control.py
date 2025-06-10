from module.device.method.uiautomator_2 import Uiautomator2
from module.device.method.adb_input import AdbInput
from module.exception import RequestHumanTakeover
from module.logger import logger


class AppControlMultiInheritance(Uiautomator2, AdbInput):
    """Multiple inheritance to get all app control methods"""
    pass


class AppControl(AppControlMultiInheritance):
    _app_u2_family = ['minitouch']
    _app_adb_family = ['ADB']

    def app_is_running(self) -> bool:
        method = self.config.Emulator_ControlMethod
        if method in AppControl._app_u2_family:
            package = self.app_current_uiautomator2()
        elif method in AppControl._app_adb_family:
            package = self.app_current_adb()
        else:
            raise RequestHumanTakeover

        package = package.strip(' \t\r\n')
        logger.attr('Package_name', package)
        return package == self.package

    def app_start(self):
        method = self.config.Emulator_ControlMethod
        logger.info(f'App start: {self.package}')
        if method in AppControl._app_u2_family:
            self.app_start_uiautomator2()
        elif method in AppControl._app_adb_family:
            self.app_start_adb()
        else:
            raise RequestHumanTakeover

    def app_stop(self):
        method = self.config.Emulator_ControlMethod
        logger.info(f'App stop: {self.package}')
        if method in AppControl._app_u2_family:
            self.app_stop_uiautomator2()
        elif method in AppControl._app_adb_family:
            self.app_stop_adb()
        else:
            raise RequestHumanTakeover
