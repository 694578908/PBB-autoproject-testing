import os
import pytest


if __name__ == '__main__':
    pytest.main()
    os.system("allure generate ./reports/allure-temp -o ./reports/allure-report --clean")