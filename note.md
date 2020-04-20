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

# JavaScript

## 1、js 的基本数据类型
Number String Null Undefined Boolean Symbol

## 2、原始数据类型和引用数据类型
### 原始数据类型：Number String Null Undefined Boolean
### 引用数据类型：对象、数组和函数

## 3、堆和栈
### 堆：堆是一个优先队列，是按优先级来进行排序的，优先级可以按照大小来规定。完全二叉树是堆的一种实现方式。
### 栈：栈中数据的存取方式为先进后出

## 4、js的内置对象
## 值属性
    Infinity NaN Undefined Null等
## 函数属性
    eval() parseInt() parseFloat()等
## 基本对象
    Object Function Boolean Symbol Error等
## 数字和日期对象
    Number Math Date
## 字符串
    String
## 结构化数据
    JSON
...
