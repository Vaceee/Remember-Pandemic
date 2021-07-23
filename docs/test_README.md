# TEST

测试板块通过 <b>Unittest</b> 为主体构建，另以 <b>ddt</b> 为参数化主要工具，报告以 <b>BeautifulReport</b> 进行输出。

## 具体操作

---

### 1. runall.py

通过 *test_login/logout/posts/replies...* 等一系列 py 文件中预设好的测试程序，在 /test 目录下通过添加想要测试的板块作为参数运行 runall.py，如：

> python runall.py login logout

则可以进行对 login 以及 logout 两个板块的测试

另外，测试模块之间具有优先级，如即使运行命令为：

> python runall.py logout login

也从 login 先开始测试，而后为 logout
主要原因还是我懒得写，直接一堆 if 完事儿不就行了。

再测试开始之前，会提示有哪些路由被添加进测试中。
![added](./img/added.png)

附板块测试对应的参数表，以及优先级：
py文件名|对应测试参数|优先级
:-:|:-:|:-:
test_login|login|1
test_sections|sections|2
test_posts|posts|3
test_replies|replies|4
test_logout|logout|5

### 2. runall.sh

如果想直接进行全部测试，直接使用 runall.sh
例如：在 test 目录下：
> ./runall.sh

---

## 使用模块

### 1. Unittest

此为 pytest 的弱化版。
直译为单元测试，我的理解就是可以将需要测试的大项目划分为若干个单元，各自之间独立进行测试。

代码中将各个大的路由作为一个 class ，其下有诸如： setUp tearDown test_xxx 等类，可灵活地进行自定义测试。（只不过我没写出来那种感觉

或许 pytest 更好吧……（写完之后才发现

### 2. ddt

对 Unittest 进行参数化的第三方插件。
在类外以列表的方式进行参数化，相较于 parameterize 库，支持字典格式，可以直接传成 json。
![ddt](./img/datasets.png)

### 3. BeautifulReport

效果很酷炫，但是 GitHub 上面评价低到爆炸的插件。
但如果只用来生成一个简单的报告而不追究其他东西的话，我觉得挺好看的。
该插件直接在当前目录下生成一个叫做 test 的 html 文件。（写在程序里面的，也能改
![BeautifulReport1](./img/beauty1.png)
![BeautifulReport1](./img/beauty2.png)
（至少比很多 pytest 的模板好看
