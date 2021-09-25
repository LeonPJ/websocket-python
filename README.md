# amarisoft-websocket-python
## 

Create server
```
python3 server.py
```
Create client to connect server
```
ptython3 client.py
```
String to object example
> import json
> word='{"Name":"Jennifer", "Age":"30"}'
> obj = json.loads(word)
> print(type(obj))// <type 'dict'>
> print(obj)// {u'Age': u'30', u'Name': u'Jennifer'}
> print(obj['Name'])// Jennifer
> print(obj['Age']) // 30

ref
```
https://cutejaneii.wordpress.com/2017/11/07/python-5-%E5%9E%8B%E6%85%8B%E8%BD%89%E6%8F%9B%E7%B3%BB%E5%88%97%EF%BD%9Ejson-string-to-object/
```