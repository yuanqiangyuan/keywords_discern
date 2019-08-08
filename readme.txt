目录说明
   hanlp
      --config.py     配置文件，可以按实际情况修改
      --env.sh        环境变量文件，主要是指明oracle客户端库的路径
      --hanlp_handler.py  字段识别代码部分
      --oracle_handler.py  oracle数据库操作接口
      --main.py     程序主入口


环境搭建
1. 系统要求 ： 
        软件或模块                版本
        python                  3.6.5
        cx_Oracle               7.1.3
        JPype1                  0.6.3
        pyhanlp                 0.1.45
        instantclient-basic     12.2.0.1.0-2  (大版本对的上就可以)

2. 硬件要求
   磁盘至少需要2G  ， pyhanlp的model库比较大，大概有1.3G，


3. 安装步骤
   1） 下载安装oracle客户端：instantclient-basic  安装略。。。。。，安装完成后修改env.sh里面的客户端库的路径。
    然后执行 source env.sh
   2） 参考https://www.cnblogs.com/shaosks/p/9172606.html安装python 3.6.5
   
   3) 安装pyhanlp和cx_Oracle  (安装前需要确认环境环境变量已经导出， 如果没有则执行 source ./env.sh )
      pip3 install pyhanlp
      pip3 cx_Oracle

4. 修改配置文件config.py

5. 运行 (运行前需要确认环境环境变量已经导出， 如果没有则执行 source ./env.sh  )
   进入代码目录 然后执行  python3 ./main.py
   

