# 关于本脚本

> 本脚本调用了较多的python模块，在anaconda环境下是完全支持的，如果未配置anaconda，则需根据所需模块自行配置

# 关于旋转张量

旋转张量定义式为：

> $$S=\frac{1}{N}\begin{vmatrix}\sum_i(x_i-x_{cm})^2&\sum_i(x_i-x_{cm})(y_i-y_{cm})&\sum_i(x_i-x_{cm})(z_i-z_{cm})\\\sum_i(x_i-x_{cm})(y_i-y_{cm})&\sum_i(y_i-y_{cm})^2&\sum_i(y_i-y_{cm})(z_i-z_{cm})\\\sum_i(x_i-x_{cm})(z_i-z_{cm})&\sum_i(y_i-y_{cm})(z_i-z_{cm})&\sum_i(z_i-z_{cm})^2\\\end{vmatrix}$$

通过将其对角化，得到三个方向的分量，再由三个分量计算非球形因子与相对各向异性，具体可以参考葛天昊毕业论文2.3.1部分。







