import subprocess, pkg_resources
import sys, os
from common.log_set import log


def install_module(module_name):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
        installed_version = pkg_resources.get_distribution(module_name).version
        log.info(f"{module_name}=={installed_version}模块已成功安装")

    except subprocess.CalledProcessError as e:
        log.error(f"安装 {module_name} 模块时出错: {e}")


def check_and_install_module(module):
    if not os.path.isfile(module):
        raise FileNotFoundError(f"{module} 不存在")
    if os.path.getsize(module) == 0:
        log.warning(f"{module} 是空文件，跳过安装模块。")
        return
    with open(module, 'r') as file:
        for line in file:
            module_name = line.strip()
            try:
                # 解析模块名和版本要求
                requirement = pkg_resources.Requirement.parse(module_name)
                base_module_name = requirement.project_name

                # 获取已安装模块的版本
                installed_distribution = pkg_resources.get_distribution(base_module_name)
                installed_version = installed_distribution.version
                log.info(f"{base_module_name} 模块已安装，版本为 {installed_version}")

                # 检查模块的版本是否符合要求
                if requirement.specifier.contains(installed_version, prereleases=True):
                    log.info(f"{module_name} 已满足版本要求")
                else:
                    log.error(f"{module_name} 版本不符合要求，正在重新安装...")
                    install_module(module_name)

            except pkg_resources.DistributionNotFound:
                log.error(f"{module_name} 模块未安装，正在安装...")
                install_module(module_name)
            except pkg_resources.VersionConflict as e:
                log.error(f"{base_module_name} 版本冲突: {e.report()}")
                install_module(module_name)
