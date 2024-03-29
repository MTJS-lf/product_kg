# product knowledge graph

a knowledge graph that contains the product-product hierarchy producer sales goods relationship,  
which sum up to 1300 products and more than 90000 brands,  

基于京东网站的1300种商品上下级概念，约10万商品品牌，约65万品牌销售关系，  
商品描述维度等知识库，基于该知识库可以支持商品属性库构建，商品销售问答，  
品牌物品生产等知识查询服务，也可用于情感分析等下游应用．  

# install neo4j

link  

```shell
http://debian.neo4j.org/
```

```shell
wget -O - https://debian.neo4j.org/neotechnology.gpg.key | sudo apt-key add -
echo 'deb https://debian.neo4j.org/repo stable/' | sudo tee /etc/apt/sources.list.d/neo4j.list
sudo apt-get update

sudo apt-get install neo4j
```

open neo4j config file.

```shell
sudo vim /etc/neo4j/neo4j.conf
```

change config file.
```shell
dbms.connectors.default_listen_address=0.0.0.0      #allow remote accese
dbms.connector.bolt.enabled=true            #start bolt service，default port 7687
dbms.connector.http.enabled=true            #start http service，default port 7474
dbms.connector.https.enabled=true           #start https service，default port 7473
```

start neo4j

```shell
neo4j start
or
sudo neo4j start
```
# open neo4j in browser

```shell
http://192.168.4.105:7474/
```

set user and password.  
user name default is neo4j.  
password default is neo4j too.  
first login should need to change the default password.  

# change etc.py file

change NEO4J_HOST to your neo4j IP address.  
change NEO4J_PORT to your neo4j port.  
change NEO4J_USER to your neo4j user.  
change NEO4J_PASSWORD to your neo4j password.  

# How to run?

```shell
bash run.sh
```

This command will create the environment that needed by the models.  
This project is created on the purposes of easy-on-run.  
If you want to know the details about the models, just read code.  


# 项目介绍
概念层级知识是整个常识知识体系中的重要组成部分。  
概念层级目前包括百科性概念层级和专业性概念层级两类，  
百度百科概念体系以及互动百科分类体系是其中的一个代表。  
就后者而言，目前出现了许多垂直行业概念层级，  
如医疗领域概念体系，电商领域概念体系，  
其中以淘宝、京东等为代表的电商网站在以商品为中心上，  
构建起了一种商品概念目录层级以及商品与品牌，品牌与品牌之间的关联关系。  

本项目认为，电商网站中的商品分类目录能够供我们构建起一个商品概念体系，  
基于商品首页，我们可以得到商品与商品品牌之间的关系，商品的属性以及属性的取值信息。  
基于这类信息，又可以进一步得到商品的画像以及商品品牌的画像。  
基于该画像。可以对自然语言处理处理的几个下游应用带来帮助，  
如商品品牌识别，商品对象及属性级别情感分析，  
商品评价短语库构建，商品品牌竞争关系梳理等。  

因此，本项目以京东电商为实验数据来源，采集京东商品目录树，  
并获取其对应的底层商品概念信息，组织形成商品知识图谱。  
目前，该图谱包括有概念的上下位is a关系  
以及商品品牌与商品之间的销售sale关系共两类关系，  
涉及商品概念数目1300+，商品品牌数目约10万+，属性数目几千种，关系数目65万规模。  
该项目可以进一步增强商品领域概念体系的应用，  
对自然语言处理处理的几个下游应用带来帮助，  
如商品品牌识别，商品对象及属性级别情感分析，  
商品评价短语库构建，商品品牌竞争关系梳理等提供基础性的概念服务。  

# 数据介绍
1, 基本数据内容
![image](./image/info.png)
2, is-a概念上下位关系
![image](./image/is_a.png)
3, sale销售关系
![image](./image/sale.png)
4, 混合关联关系
![image](./image/mix.png)

# to be continued..
