import cv2

# 读取图片
image = cv2.imread('./1.webp')

# 检查图片是否成功加载
if image is None:
    print("无法加载图片！")
else:
    # 显示图片
    cv2.imshow('Image', image)

    # 等待按键输入后关闭窗口
    cv2.waitKey(0)
    cv2.destroyAllWindows()
