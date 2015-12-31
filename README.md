
#新闻推荐系统

支持三种推荐模型:<br>
0.content-based recommendation
1.user2user 模型<br>
2.item2item模型<br>

##系统运行
  命令：usage: version.py [-h] [-train \<trainfile>] [-test \<testfile>] [-m \<method>] [-u \<userid>] <br>



optional arguments:<br>
  -h, --help        <br>    
        show this help message and exit <br>
  -train \<trainfile\>, --trainfile \<trainfile\>  <br>
        please specify train  data file     <br>
  -test \<testfile\>, --testfile \<testfile\>  <br>
        please specify test  data file     <br>
  -m \<method>, --method \<method\> <br>
        please specify method to recommend: 0 for user2user;<br>
        1 for term2term;2 for others  <br>
  -u \<userid>, --userid \<userid\>  <br>
        please specify the user to recommend <br>

for example:version.py -train /Users/qiaoyang/PycharmProjects/user_click_data.txt -test  /Users/qiaoyang/PycharmProjects/testing.txt -m 1 -u 4858290   <br>
使用新闻文件user_click_data.txt作训练，testing.txt存储给用户推荐的新闻，使用user2user模型，给出用户4858290的推荐新闻。<br>

##系统模块组成 <br>
  * Core.py 总控模块 调用docs模块处理新闻数据，然后再使用user，item等模型实现推荐。
  * docs.py 数据处理模块
    * doc.py  处理新闻数据返回一系列News组成的数组
    * new.py  News类包含userid, newsid, scan_time, title, tags（提取的关键词）等信息
    * tfidf Tfidf类 提取文档的关键词  
      * 当前使用的是中文分词工具jieba，还可以提取关键词中，当前系统要求按照此工具。 https://github.com/fxsjy/jieba

