import os
import pytest
from common.install_requirements_module import check_and_install_module

if __name__ == '__main__':
    check_and_install_module('requirements.txt')
    pytest.main()
    os.system("allure generate ./reports/allure-temp -o ./reports/allure-report --clean")
