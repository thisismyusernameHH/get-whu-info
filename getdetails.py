import re
import os
import codecs
patternlist=["_ac6482636fd67a15","_9278027141da2948","_a1d6b9ccabdbbe40","_3510aeda764a1e4e","col3","col5","col6","<option selected=\"selected","col4.*?>(.*?)>"]
p="{0}.*?value=(.*?) "
pathlsit=["./16computer/{0}{1}"] #第一个是学院 后面是个人号
js=0
tmp=""
store=codecs.open("./16computer_info/info.txt","a+","utf-8")
for year in ['2016301500']:
	path=pathlsit[js]
	js+=1
	for i in range(400):
		filepath=path.format(year,i)
		if os.path.exists(filepath):
			f=open(filepath,encoding='UTF-8')
			content=f.read()
			f.close
			for  token in patternlist:
				mode=p.format(token)
				info=re.findall(mode, content)
				if "col4" in token:
					info=re.findall(token,content)
				if type(info) == str:
					info=info[0]
					tmp+=" "+info
				else:
					for s in info:
						tmp+=" "+s
			store.write(tmp+"\n")
			tmp=""
store.close()

