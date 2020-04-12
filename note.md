# 1、脚本的加载
    script脚本会阻塞html的解析
    但多个script脚本的加载是并行的（同时）：因为实际上现代浏览器会对资源进行预解析，提前把html中要引用到的资源放进请求队列中。

# 2、async 和 defer 的区别
    ```
    <script async></script>
    <script defer></script>
    ```
    **相同点：** 加上两者的 script 脚本都不会阻塞html的解析
    **不同：**
      async：脚本加载过程中html同时在解析，脚本加载完成后立刻开始执行会阻塞html解析
      defer：html解析过程中遇到脚本，两者同时解析，html解析完成后开始脚本的执行

# 3、

