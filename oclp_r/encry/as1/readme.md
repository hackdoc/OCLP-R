# 这里是as1加密(编码级别)
这个编码基本没有什么用,仅仅提供最基本的加密功能,当然也是其他加密的基础,你无法禁用
可以调用based的 **encry** 或 **decry**,也可以使用**used**的 **encry** 或 **decry**(更简单)
<br/> 以下是使用方法:

导入模块
```python
#导入based模块
import encry.as1.based
from encry.as1.based import Encry,Decry
#导入used模块
import encry.as1.used
from encry.as1.used import *
```

Example:

```python
#based:
from encry.as1.based import Encry,Decry
data = "hello world"
data2= b'aGVsbG8gd29ybGQ='
a=Encry(data)
b=Decry(data2)
print(a.encry(data))
print(b.decry(data2))
```

```python
#used:
from encry.as1.used import *
a=encry_abve("hello".encode())
print(a.decode())
```
Usage(based):<br/>
1.Encry使用方法
首先需要配置data **(加密前的字符/字符串)** ,如下
```python
from encry.as1.based import *
a = Encry(data)
```
可以用: **encry**,**encry_16**,**encry_32**,**encry_85**,其中encry基于**base64**,encry_16基于**base16**
,如下
```python
from encry.as1.based import *
a = Encry(data)
a.encry(data)
a.encry_16(data)
a.encry_32(data)
a.encry_85(data)
```
decry使用类似:
```python
from encry.as1.based import *
a = Decry(data)
```

```python
from encry.as1.based import *
a = Decry(data)
a.decry(data)
a.decry_16(data)
a.decry_32(data)
a.decry_85(data)
```