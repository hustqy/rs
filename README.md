
#新闻推荐系统

拟支持三种推荐模型:<br>
1.user2user 模型<br>
2.item2item模型<br>
3.UMF
##系统运行
  命令：usage: version.py [-h] [-f \<filename>] [-m \<method>] [-u \<userid>] <br>



optional arguments:<br>
  -h, --help        <br>    
        show this help message and exit <br>
  -f \<filename\>, --filename \<filename\>  <br>
        please specify the data file     <br>
  -m \<method>, --method \<method\> <br>
        please specify method to recommend: 0 for user2user;<br>
        1 for term2term;2 for others  <br>
  -u \<userid>, --userid \<userid\>  <br>
        please specify the user to recommend <br>

for example:version.py -f /Users/qiaoyang/PycharmProjects/data.txt -m 0 -u 5218791 <br>
使用新闻文件data.txt，使用user2user模型，给出用户5218791的推荐新闻。<br>

##系统模块组成 <br>
  * Core.py 总控模块 调用docs模块处理新闻数据，然后再使用user，item等模型实现推荐。
  * docs.py 数据处理模块
    * doc.py  处理新闻数据返回一系列News组成的数组
    * new.py  News类包含userid, newsid, scan_time, title, tags（提取的关键词）等信息
    * tfidf Tfidf类 提取文档的关键词  
      * 当前使用的是中文分词工具jieba，还可以提取关键词中，当前系统要求按照此工具。 https://github.com/fxsjy/jieba
  * usermodel 拟实现user2user模型
