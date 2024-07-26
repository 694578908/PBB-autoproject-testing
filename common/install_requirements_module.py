import subprocess, pkg_resources
import sys, os
from common.log_set import log


def is_pip_installed():
    try:
        result = subprocess.run(['pip', '--version'], capture_output=True, text=True, check=True)
        version_info = result.stdout.strip()
        return version_info
    except subprocess.CalledProcessError as e:
        # 捕获命令执行错误
        log.error(f"检测 pip 失败，返回码: {e.returncode}")
        return None
    except FileNotFoundError:
        # 捕获文件未找到错误
        log.error("pip 未安装或命令不可用")
        return None


def install_module(module_name):
    version_info = is_pip_installed()
    if not version_info:
        log.info("pip 未安装")
        return False
    log.info(f"pip 已安装，版本信息: {version_info}")
    source_url = 'https://pypi.tuna.tsinghua.edu.cn/simple'
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name, '-i', source_url])
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
