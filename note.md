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
水平垂直居中1.html
#### 绝对定位 + margin-top/left + calc()
水平垂直居中2.html
#### 适用于盒子宽高未知
#### 绝对定位 + transform + top/left
水平垂直居中3.html
#### 绝对定位 + margin: auto
水平垂直居中4.html
#### flex布局 + margin: auto
水平垂直居中5.html
#### flex布局
水平垂直居中6.html
#### table布局
水平垂直居中7.html

## 8、BFC
Block Formatting Contexts （块级格式化上下文)
它是一个独立的盒子，并且这个独立的盒子内部布局不受外界影响。
### 何时会触发BFC：
根元素<html>
float的值不为none。
position的值不为relative和static。
overflow的值为auto,scroll或hidden。
display的值为table-cell, table-caption, inline-block中的任何一个。
### 作用
一：清除浮动（阻止高度塌陷）。
二：外边距合并：同属一个BFC的相邻元素会发生外边距（margin）重叠。
三：阻止元素被浮动元素覆盖，可用来实现两列布局。

## 9、清除浮动
### 浮动影响
在父元素未定义高度时，父元素高度会坍缩
### 清除浮动方法
#### BFC清除浮动
#### 添加额外标签，应用 clear: both
在浮动的盒子后面添加一个空盒子，并给样式添加该属性
清除浮动1.html
#### 使用伪元素 :after
上一种方法的优化，在浮动的盒子后面追加一个块元素
清除浮动2.html

## 10、inline-block的间隙问题
两个被 display: inline-block 的元素放到一起会产生一段空白
因为这时两个元素之间的代码换行会被转换成空白符
### 解决方法
将两个盒子代码写在同一行

## 11、