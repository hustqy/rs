
#新闻推荐系统

拟支持三种推荐模型:<br>
1.user2user 模型<br>
2.item2item模型<br>
3.UMF

＃＃系统运行
  命令：usage: version.py [-h] [-f <filename>] [-m <method>] [-u <userid>] 

  recommender system

optional arguments:<br>
  -h, --help            show this help message and exit
  -f <filename>, --filename <filename>
                        please specify the data file
  -m <method>, --method <method>
                        please specify method to recommend: 0 for user2user;
                        1 for term2term;2 for others
  -u <userid>, --userid <userid>
                        please specify the user to recommend

for example:version.py -f /Users/qiaoyang/PycharmProjects/data.txt -m 0 -u 5218791 <br>
使用新闻文件data.txt，使用user2user模型，给出用户5218791的推荐新闻。
