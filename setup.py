from setuptools import find_packages, setup

setup(
    name = "tablip",      #这里是pip项目发布的名称
    version = "1.0.8",  #版本号，数值大的会优先被pip
    keywords = ("pip", "tablip","featureextraction"),
    description='export data to file such as excel etc..',
    long_description=(
            open('README.md',encoding='utf-8').read()
    ),
    long_description_content_type="text/markdown",
    license = "MIT Licence",

    url = "https://github.com/bn0901/tablip",     #项目相关文件地址，一般是github
    author = "bn.zheng",
    author_email = "zhengbingxian666@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",

    install_requires=[
        'xlrd',
        'xlwt',
    ]
)
