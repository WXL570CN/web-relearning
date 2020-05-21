# HTML5
## 1、脚本的加载
script脚本会阻塞html的解析
但多个script脚本的加载是并行的（同时）：因为实际上现代浏览器会对资源进行预解析，提前把html中要引用到的资源放进请求队列中。

## 2、async 和 defer 的区别
```
    <script async></script>
    <script defer></script>
```
### 相同点
加上两者的 script 脚本都不会阻塞html的解析

### 不同点：
async：脚本加载过程中html同时在解析，脚本加载完成后立刻开始执行会阻塞html解析
defer：html解析过程中遇到脚本，两者同时解析，html解析完成后开始脚本的执行

## 3、DOMContentLoaded和Load的区别
### DOMContentLoaded
当初始的 HTML 文档被完全加载和解析完成之后，DOMContentLoaded 事件被触发，而无需等待样式表、图像和子框架的完成加载。
### Load
样式表、图像和子框架的完成加载， load 事件被触发。

## 4、href和src的区别
### href
用于在当前文档和指定资源间确定联系
### src
下载资源并替换当前内容

## 5、link和@import的区别
1. link是XHTML提供的标签，不仅仅可以加载CSS。@import是CSS提供的语法规则，只能加载CSS。
2. 加载页面时，link标签引入的 CSS 被同时加载；@import引入的 CSS 将在页面加载完毕后被加载。

## 6、Doctype
Doctype声明位于文档中的最前面，处于html标签之前。告知浏览器的解析器，用什么文档类型规范来解析这个文档

## 7、重定向
mata标签的http-equiv="refresh"属性用来告诉浏览器进行页面的跳转，content属性告知在多少秒后进行跳转，以及跳转的地址。此处为2s后重定向。
```
<meta http-equiv="refresh" content='2;https://messiahhh.github.io/blog'>
```
或者
```
// js
location.href = 'https://messiahhh.github.io/blog'
```
或者根据响应状态码跳转
```
res.statusCode = 301 // or 302
res.setHeader('Location', 'https://messiahhh.github.io/blog')
```

# CSS3
## 1、选择器
1. 标签选择器 `div {}`
2. 属性选择器 `a[title='..'] {}`
2. id选择器
3. class选择器
4. 子代选择器 `ul>li {}`
5. 后代选择器 `body li {}`
6. 群组选择器 `h1,p`
7. 相邻兄弟选择器 `h1 + p {}`
8. 伪类选择器 `:hover`
```
// first-child 和 first-of-type 的区别
p:first-child: 当父元素下的第一个元素为p元素时
p:first-of-type: 父元素下的第一个p元素
```

## 2、属性的权重
!important > 内联样式 > ID选择器 > class选择器 > 标签选择器 > 通配符（*） > 浏览器默认样式 > 继承样式

## 3、盒模型
### box-sizing
`box-sizing: content-box `：浏览器默认，盒子宽度为 width（内容宽度） + padding + border
`box-sizing: border-box`：盒子宽度为width， 即 内容宽度 + padding + border

## 4、transition：过渡效果
`transition-property:` 过渡属性(默认值为all)
`transition-duration:` 过渡持续时间(默认值为0s)
`transiton-timing-function:` 过渡函数(默认值为ease函数)
`transition-delay:` 过渡延迟时间(默认值为0s)
注意：IE9-不支持该属性，safari3.1-6、IOS3.2-6.1、android2.1-4.3需要添加-webkit-前缀；而其余高版本浏览器支持标准写法

## 5、animation：动画效果
`animation-name` 动画名
`animation-duration` 持续时间
`animation-timing-function` 动画曲线
`animation-delay` 延迟
`animation-iteration-count` 播放次数
`animation-direction` 是否在下一周期逆向播放

## 6、元素分类
### 行内元素
不独占一行；宽度(width)、高度(height)、内边距和外边距的 top/bottom 都不可改变，也就是说 padding 和 margin 的左右是可以改变的。
`a b br i span input select`
### 块级元素
独占一行；宽度(width)、高度(height)、内边距(padding)和外边距(margin)都可控制;
`div p h1 h2 h3 h4 form ul`
### 行内块元素
不独占一行；可以设置宽和高。
`<input> 、<img> 、<button> 、<texterea> 、<label>`

## 7、水平垂直居中
### 适用于盒子宽高已知
#### 绝对定位 + margin-top/left + top/left
1水平垂直居中1.html
#### 绝对定位 + margin-top/left + calc()
2水平垂直居中2.html
#### 适用于盒子宽高未知
#### 绝对定位 + transform + top/left
3水平垂直居中3.html
#### 绝对定位 + margin: auto
4水平垂直居中4.html
#### flex布局 + margin: auto
5水平垂直居中5.html
#### flex布局
6水平垂直居中6.html
#### table布局
7水平垂直居中7.html

## 8、BFC
Block Formatting Contexts （块级格式化上下文)
它是一个独立的盒子，并且这个独立的盒子内部布局不受外界影响。
### 何时会触发BFC：
1. 根元素<html>
2. float的值不为none。
3. position的值不为relative和static。
4. overflow的值为auto,scroll或hidden。
5. display的值为table-cell, table-caption, inline-block中的任何一个。
### 作用
1. 清除浮动（阻止高度塌陷）。
2. 外边距合并：同属一个BFC的相邻元素会发生外边距（margin）重叠。
3. 阻止元素被浮动元素覆盖，可用来实现两列布局。

## 9、清除浮动
### 浮动影响
在父元素未定义高度时，父元素高度会坍缩
### 清除浮动方法
#### BFC清除浮动
#### 添加额外标签，应用 clear: both
在浮动的盒子后面添加一个空盒子，并给样式添加该属性
8清除浮动1.html
#### 使用伪元素 :after
上一种方法的优化，在浮动的盒子后面追加一个块元素
9清除浮动2.html

## 10、inline-block的间隙问题
两个被 display: inline-block 的元素放到一起会产生一段空白
因为这时两个元素之间的代码换行会被转换成空白符
### 解决方法
将两个盒子代码写在同一行
10inline-block的间隙问题.html

## 11、display: none，visibility: hidden, opacity: 0 的区别
### 结构上
1. display: none 会让目标元素不会被渲染进渲染树， 因此不占空间，而且不能点击。
2. visibility: hidden目标元素会被渲染进渲染树，因此占空间，但是不能点击。
3. opacity: 0目标元素会被渲染进渲染树，因此占空间，而且能点击。
### 继承上
1. display: none 作用于父元素后，子元素也不会被渲染（即使给子元素加了display: block）
2. visibility: hidden作用于父元素后，子元素继承这个属性，也不可见；不过可以给子元素设置visibility: visible使其可见。
3. opacity: 0作用于父元素后，虽然子元素不会继承这个属性，但是子元素的透明度也会被影响，所以也不可见；而且不能通过给子元素设置opacity: 1使其变成不透明。
### 性能上
1. display: none会造成回流/重绘，性能影响大
2. visibility: hidden会造成元素内部的重绘，性能影响相对小
3. opacity: 0 由于opacity属性启用了GPU加速，性能最好
### opacity属性的补充
opacity是不继承属性，父元素设置opacity，子元素并不会继承。但是因为该属性的特殊性（类似background），父元素有了透明度，子元素的样式也会被影响。如果父元素设置opacity: 0.5，子元素设置opacity: 0.5，那么实际上子元素的透明度是0.5 * 0.5 = 0.25。
如果希望子元素不被父元素的透明度影响，我们可以使用background: rgba代替opacity: 0

## 12、文本溢出
11文本溢出问题.html
### 单行文本溢出
```
overflow:hidden; （超出限定的宽度就隐藏内容）
white-space: nowrap; （设置文字在一行显示不能换行）
text-overflow: ellipsis; （规定当文本溢出时显示省略符号来代表被修剪的文本）
```
### 多行文本溢出
```
overflow: hidden;
-webkit-line-clamp:2; （用来限制在一个块元素显示的文本的行数,2表示最多显示2行。 为了实现该效果，它需要组合其他的WebKit属性）
display: -webkit-box; （和1结合使用，将对象作为弹性伸缩盒子模型显示 ）
-webkit-box-orient:vertical;（ 和1结合使用 ，设置或检索伸缩盒对象的子元素的排列方式 。）
```

## 13、重绘和回流
重绘: 当渲染树中的一些元素需要更新属性，而这些属性只是影响元素的外观、风格，而不会影响布局的操作，比如 background-color，我们将这样的操作称为重绘。
回流：当渲染树中的一部分（或全部）因为元素的规模尺寸、布局、隐藏等改变而需要重新构建的操作，会影响到布局的操作，这样的操作我们称为回流。

## 14、实现三栏布局（高度已知）
1. 浮动
优点：兼容性好  
缺点：脱离文档流，处理不好会带来许多问题
2. 绝对定位
优点：快捷
缺点：脱离文档流，下面的子元素都需要脱离文档流，可使用性比较差
3. flex布局
为了解决上述两个布局的缺陷而出现的
4. table布局
优点：兼容性好，有可能flex布局有兼容性问题
缺点：传统的问题；三栏高度是统一增减的。
5. 网格布局（grid新技术）
当高度未知时，只有flex布局和table布局是能够通用的。

# JavaScript

## 1、js 的基本数据类型
Number String Null Undefined Boolean Symbol

## 2、原始数据类型和引用数据类型
原始数据类型：Number String Null Undefined Boolean

引用数据类型：对象、数组和函数

## 3、堆和栈
堆：堆是一个优先队列，是按优先级来进行排序的，优先级可以按照大小来规定。完全二叉树是堆的一种实现方式。

栈：栈中数据的存取方式为先进后出

## 4、js的内置对象
### 值属性
    Infinity NaN Undefined Null等
### 函数属性
    eval() parseInt() parseFloat()等
### 基本对象
    Object Function Boolean Symbol Error等
### 数字和日期对象
    Number Math Date
### 字符串
    String
### 结构化数据
    JSON

## 5、Null 和 Undefined 区别
Undefined：一般变量声明了但还没有定义的时候会返回 undefined

Null：null主要用于赋值给一些可能会返回对象的变量，作为初始化。

当我们对两种类型使用 typeof 进行判断的时候，Null 类型化会返回 “object”，这是一个历史遗留的问题。当我们使用双等号对两种类型的值进行比较时会返回 true，使用三个等号时会返回 false。

## 6、说几条写 JavaScript 的基本规范？
1. 一个函数作用域中所有的变量声明应该尽量提到函数首部，用一个 var 声明，不允许出现两个连续的 var 声明，声明时如果变量没有值，应该给该变量赋值对应类型的初始值，便于他人阅读代码时，能够一目了然的知道变量对应的类型值。
2. 代码中出现地址、时间等字符串时需要使用常量代替。
3. 在进行比较的时候吧，尽量使用'===', '!=='代替'==', '!='。
4. 不要在内置对象的原型上添加方法，如 Array, Date。
5. switch 语句必须带有 default 分支。
6. for 循环必须使用大括号。
7. if 语句必须使用大括号。

## 7、闭包是什么，有什么特性，对页面有什么影响
闭包就是能够读取其他函数内部变量的函数,使得函数不被GC回收。  
如果过多使用闭包，容易导致内存泄露。


# ES6
## 1、let
ES6新增语法  
只在当前代码块有效：{}中  
不存在变量提升：在使用let命令声明变量之前使用该变量会报错而不是undefined  
暂时性死区：在代码块内，使用let命令声明变量之前，该变量都是不可用的  
在相同作用域内，不允许重复申明

## 2、const
定义时必须赋值  
赋值后常量本身不可更改，其实是不可更改其内存地址

## 3、解构赋值
用于数组，位置一一对应，可以指定默认值

	let [a, b, c = 3] = [1, 2];
	>> a = 1, b = 2, c = 3

用于对象，通过键名对应，位置随意，可以定义一个变量接收，同样可以指定默认值

	let {name, age} = {name:"lisi", age:20}
	let {name: myname, age: myage}

对象的解构赋值本质上是赋值给键值对中的值

    let {name, age} = {name:"lisi", age:20}
    实际上是
    let {name: name, age: age} = {name:"lisi", age:20}


# Vue
## 1、对MVVM的理解
MVVM 是 Model-View-ViewModel 的缩写。

**Model**代表数据模型，也可以在Model中定义数据修改和操作的业务逻辑。  
**View** 代表UI 组件，它负责将数据模型转化成UI 展现出来。  
**ViewModel** 监听模型数据的改变和控制视图行为、处理用户交互，简单理解就是一个同步View 和 Model的对象，连接Model和View。  

在MVVM架构下，View 和 Model 之间并没有直接的联系，而是通过ViewModel进行交互，Model 和 ViewModel 之间的交互是双向的， 因此View 数据的变化会同步到Model中，而Model 数据的变化也会立即反应到View 上。

ViewModel 通过双向数据绑定把 View 层和 Model 层连接了起来，而View 和 Model 之间的同步工作完全是自动的，无需人为干涉，因此开发者只需关注业务逻辑，不需要手动操作DOM, 不需要关注数据状态的同步问题，复杂的数据状态维护完全由 MVVM 来统一管理。

## 2、Vue的生命周期
**beforeCreate（创建前）**：el 和 data 并未初始化（这个时期，this变量还不能使用，在data下的数据，和methods下的方法，watcher中的事件都不能获得到；）

__created（创建后）__ ：完成了 data 数据的初始化，el没有,$el属性还没有显示出来（这个时候可以操作vue实例中的数据和各种方法，但是还不能对"dom"节点进行操作；）。异步请求适合在这调用。

**beforeMount（载入前）**：在挂载开始之前被调用，完成了 el 和 data 初始化，这里的el是虚拟的dom。实例已完成以下的配置：编译模板，把data里面的数据和模板生成html。注意此时还没有挂载html到页面上。

**mounted（载入后）**：在el 被新创建的 vm.$el 替换，并挂载到实例上去之后调用。实例已完成以下的配置：用上面编译好的html内容替换el属性指向的DOM对象。完成模板中的html渲染到html页面中。此过程中进行ajax交互。

**beforeUpdate（更新前）** ：是指view层数据变化前，不是data中的数据改变前触发；

**updated（更新后）** ：是指view层的数据变化之后，调用时，组件DOM已经更新，所以可以执行依赖于DOM的操作。在大多数情况下，应该避免在此期间更改状态，因为这可能会导致更新无限循环。

**beforeDestroy（销毁前）**：在实例销毁之前调用。实例仍然完全可用。

**destroyed（销毁后）**：当前组件已被删除，清空相关内容。调用后，所有的事件监听器会被移除，所有的子实例也会被销毁。该钩子在服务器端渲染期间不被调用。

## 3、有关Vue生命周期的问题
### 3.1、什么是vue生命周期？
答： Vue 实例从创建到销毁的过程，就是生命周期。从开始创建、初始化数据、编译模板、挂载Dom→渲染、更新→渲染、销毁等一系列过程，称之为 Vue 的生命周期。

### 3.2、vue生命周期的作用是什么？
答：它的生命周期中有多个事件钩子，让我们在控制整个Vue实例的过程时更容易形成好的逻辑。

### 3.3、vue生命周期总共有几个阶段？
答：它可以总共分为8个阶段：创建前/后, 载入前/后,更新前/后,销毁前/销毁后。

### 3.4、第一次页面加载会触发哪几个钩子？
答：会触发 下面这几个beforeCreate, created, beforeMount, mounted 。

### 3.5、DOM 渲染在 哪个周期中就已经完成？
答：DOM 渲染在 mounted 中就已经完成了。

### 3.6、在哪个生命周期内调用异步请求？ 
可以在钩子函数 created、beforeMount、mounted 中进行调用，因为在这三个钩子函数中，data 已经创建，可以将服务端端返回的数据进行赋值。但是本人推荐在 created 钩子函数中调用异步请求，因为在 created 钩子函数中调用异步请求有以下优点：
1. 能更快获取到服务端数据，减少页面 loading 时间；
2. ssr 不支持 beforeMount 、mounted 钩子函数，所以放在 created 中有助于一致性；

### 3.7、在什么阶段才能访问操作DOM？ 
在钩子函数 mounted 被调用前，Vue 已经将编译好的模板挂载到页面上，所以在 mounted 中可以访问操作 DOM。

## 4、Vue实现数据双向绑定的原理
vue实现数据双向绑定主要是：采用数据劫持结合发布者-订阅者模式的方式，通过Object.defineProperty（）来劫持各个属性的setter，getter，在数据变动时发布消息给订阅者，触发相应监听回调。当把一个普通 Javascript 对象传给 Vue 实例来作为它的 data 选项时，Vue 将遍历它的属性，用 Object.defineProperty 将它们转为 getter/setter。用户看不到 getter/setter，但是在内部它们让 Vue 追踪依赖，在属性被访问和修改时通知变化。

vue的数据双向绑定 将MVVM作为数据绑定的入口，整合Observer，Compile和Watcher三者，通过Observer来监听自己的model的数据变化，通过Compile来解析编译模板指令（vue中是用来解析 {{}}），最终利用watcher搭起observer和Compile之间的通信桥梁，达到数据变化 —>视图更新；视图交互变化（input）—>数据model变更双向绑定效果。

## 5、简述Vue的响应式原理
当一个Vue实例创建时，vue会遍历data选项的属性，用 Object.defineProperty 将它们转为 getter/setter并且在内部追踪相关依赖，在属性被访问和修改时通知变化。每个组件实例都有相应的 watcher 程序实例，它会在组件渲染的过程中把属性记录为依赖，之后当依赖项的 setter 被调用时，会通知 watcher 重新计算，从而致使它关联的组件得以更新。

## 6、说说你对 SPA 单页面的理解，它的优缺点分别是什么？ 
SPA（ single-page application ）仅在 Web 页面初始化时加载相应的 HTML、JavaScript 和 CSS。一旦页面加载完成，SPA 不会因为用户的操作而进行页面的重新加载或跳转；取而代之的是利用路由机制实现 HTML 内容的变换，UI 与用户的交互，避免页面的重新加载。  
优点： 用户体验好、快，内容的改变不需要重新加载整个页面，避免了不必要的跳转和重复渲染；基于上面一点，SPA 相对对服务器压力小；前后端职责分离，架构清晰，前端进行交互逻辑，后端负责数据处理；  
缺点：  
1. 初次加载耗时多：为实现单页 Web 应用功能及显示效果，需要在加载页面的时候将 JavaScript、CSS 统一加载，部分页面按需加载；
2. 前进后退路由管理：由于单页应用在一个页面中显示所有的内容，所以不能使用浏览器的前进后退功能，所有的页面切换需要自己建立堆栈管理；
3. SEO 难度较大：由于所有的内容都在一个页面中动态替换显示，所以在 SEO 上其有着天然的弱势。

## 7、父子组件之间的传值
父向子组件传值：父组件通过绑定属性传送，子组件通过props接收
子向父组件传值：子组件通过$emit()传送，父组件通过方法绑定接收

## 8、Vue路由实现页面跳转的两种方式（router-link和JS）
### router-link实现
> 简单写法
```
<router-link to="demo2">demo2</router-link>
```
> 使用 v-bind 的写法
```
<router-link :to="'demo2'">demo2</router-link>
<!-- 也可以用{}包裹对应的path或name -->
<router-link :to="{ name: 'demo2' }">demo2</router-link>
```
> 传参的写法
```
<router-link :to="{ name: 'demo2', params: { userId: 123 }}">demo2</router-link>
<!-- router.js 中对 demo2 的路径进行配置 -->
{path: '/demo2/:userId'}
<!-- 如何在页面中获取到userId：在 mounted 钩子中使用 this.$route.params.xx. 获取传过来的参数，如下： -->
mounted () {
    alert(this.$route.params.userId)
}
```
> 传入地址键值对
```
<router-link :to="{ path: 'demo2', query: { plan: 'private' }}">demo2</router-link>
<!-- 页面跳转的结果为 /demo2?plan=private -->
<!-- （注意这里不用在 router.js 里配置路径） -->
<!-- 在新页面中获取到传过来的地址键值对 plan，可以在 mounted 钩子中使用 this.$route.plan.xx. 获取传过来的地址键值对，如下： -->
mounted () {
    alert(this.$route.query.plan)
}
```
### JS实现
```
<!-- template 部分： -->
<button @click="toURL">跳转页面</button>
<!-- script 部分：（注意这里是 router，上面是 route） -->
```
> 简单写法：
```
methods:{
    toURL(){
    this.$router.push({ path: '/demo2' })
    }
}
```
> 传参：
```
methods:{
    toURL(){
    this.$router.push({ name: 'demo2', params: { userId: 123 }})
    }
}
```
> 传入地址键值对：
```
methods:{
    toURL(){
    this.$router.push({ name: 'demo2', params: { userId: 123 }, query: { plan: 'private' } })
    }
}
```


# 计算机网络
## 1、网页从输入网址到渲染完成经历了哪些过程？
1. 输入网址；
2. 发送到DNS服务器，并获取域名对应的web服务器对应的ip地址；
3. 与web服务器建立TCP连接；
4. 浏览器向web服务器发送http请求；
5. web服务器响应请求，并返回指定url的数据（或错误信息，或重定向的新的url地址）；
6. 浏览器下载web服务器返回的数据及解析html源文件；6
7. 生成DOM树，解析css和js，渲染页面，直至显示完成；

