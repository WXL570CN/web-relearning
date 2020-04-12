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
1. 标签选择器
`div {}`
2. 属性选择器 
`a[title='..'] {}`
2. id选择器
3. class选择器
4. 子代选择器 
`ul>li {}`
5. 后代选择器
`body li {}`
6. 相邻兄弟选择器
`h1 + p {}`
