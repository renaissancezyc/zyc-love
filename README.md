# 项目介绍 (Project Introduction)

这是一个使用Python的Tkinter库创建的动态爱心动画项目。动画展示了一个心形图案，具有脉动和散射效果，代码经过优化以提高性能和可读性。

This project is a dynamic heart animation created using Python's Tkinter library. The animation features a heart shape that pulsates and scatters, with code optimized for performance and readability.

## 使用方法 (How to Run)

```python

pip install zyc_love 

from love_code.love import run 

if __name__=="__main__":
    
    run()

```

## 工作原理 (How it Works)
心形图案是通过一个数学函数生成的，该函数使用参数`t`并返回心形上某点的x和y坐标。程序在心形内部散布点并应用抖动效果，以创造更自然的外观。最后，程序使用Tkinter模块在画布上渲染心形图案。

The heart shape is generated using a mathematical function that takes a parameter `t` and returns the x and y coordinates of a point on the heart. The program then scatters points inside the heart and applies a jitter effect to create a more natural look. Finally, the program renders the heart on a canvas using the Tkinter module.

## 自定义 (Customization)
您可以通过调整`heart_function`函数中的`shrink_ratio`参数来自定义心形的大小和角度。您还可以通过更改`scatter_inside`函数中的`beta`参数来调整散射效果的强度。

You can customize the size and angle of the heart by adjusting the `shrink_ratio` parameter in the `heart_function` function. You can also adjust the intensity of the scattering effect by changing the `beta` parameter in the `scatter_inside` function.

## 许可证 (License)
本项目采用Apache-2.0许可证。欢迎使用和修改代码。

This project is licensed under the Apache-2.0 License. Feel free to use and modify the code as needed.
