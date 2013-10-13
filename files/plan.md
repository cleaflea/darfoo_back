## server端
* 验证码 ```captcha```＋```widget_tweaks``` 近期可以搞定
* 微信 ```werobot``` ```nodejs```＋```socketio```＋```redis``` 需要人手
* 插件管理 ```Django```＋```memcache``` + ```restful``` 近期可以搞定
* 整体就是一个为```django```为主框架 ```nodejs```为辅处理异步请求(通过```nginx```或者```django```的路由把异步请求代理到```nodejs```的进程)
* 异步请求就是之后的微信通信 以及在线定制应该也会用到 不然体验会很烂 
* ```server```这边还要做的事情就是各大SNS开放平台的接入，我现在在测试新浪的，还要审核身份，微信升级为服务号之后的一些新的权限也在审核中真是蛋疼…..
* 站内搜索，完成定制用户对插件的搜索和查找;
* 认证模块写好了 缺前端(最近也在苦练前端的说= =)
* 购买新的服务器(ec2) 以及绑定darfoo的正宗域名
* 对所有静态资源进行代理，防止加载过慢，影响体验
* 通信用base64编码(!!!)
* 为了性能 是否移到JVM上(现在jvm优化的这么逆天)
* 敏捷开发is everything
* celery+rabbitmq(_或者满足mq协议的db，like redis_)，作delay jobs
* gearman和上面一样也是异步任务神器
* south作为一个db migration工具，just like rails

### server所缺人手
* 主要是```python```程序员 ```nodejs```程序员 会```java``` ```ruby```的也可以  精通```scala``` ```erlang```的可以要  这个绝对需要
* 也就是```python,nodejs``` > ```scala, erlang``` > ```java,ruby```
* 懂网络安全 web攻防的优先录取

## 服务器
* 熟悉```linux/unix```
* 熟悉```git``` (需要维护两个git仓库)
* 熟悉```vim/emacs``` 熟悉bash脚本 或者其他轻量级的系统脚本语言 
* 服务器管理也是需要专门的人 或者是从server端那兼并着管


## 前端
* ajax请求成功和请求失败的提示效果（周日开会说过了） 
* 对email验证以及输入框重内容不能为空的提示也和ajax请求之后的提示框一个效果
* 还有好多奇奇怪怪的效果 比如显示插件列表的 编辑插件等等
* 插件管理的前端也要重新设计 之前我写的那套太丑了！
* 在线定制```html5+css3``` 需要人手
* ```angularjs/jquery``` 大神 
* [FileUpload](http://tekbrand.com/jquery/10-best-jquery-file-upload-plugins)

### 前端所缺人手
* ```html5+css```程序员 ```js```大神 ```css```大神
* （貌似前端我也说不上什么话啊 但是后期我还是会参与的）
* 会使用```phonegap```的优先  可以参与移动端也可以参与前端的大神需要的

## android
* 有经验的android程序员 有开发过项目 不是来学习的 要有实战经验
* 熟练使用jvm上其他奇葩的语言也要 ```groovy scala clojure```大神来者不拒

### android所缺人手
反正就是要能写android啦 用```ndk```的都行 这个也要冰雁把关 冰雁的意见很重要

## ios
* 我中午吃饭的时候想 现在主要的业务对象和受众的确是老年人，但是年轻人才是真正应该关注的用户  现在ios市场占有率那么高  必然不能忽视，当然ios上肯定没有launcher的概念 要写的就是一个定制APP 这个我可以参与开发 到时候```android ios 网页```都可以让年轻人定制才有吸引力和竞争力 ios只要1个或2个有经验的即可 熟悉ios开发 熟悉objective-c

## 美工
* 有才华 嗯嗯 like the Taiwan Guy 让人看了有要让人想给他跪下的感觉

