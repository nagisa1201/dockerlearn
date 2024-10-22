import cv2

# 打开摄像头（参数0表示默认摄像头）
cap = cv2.VideoCapture(0)

# 检查摄像头是否成功打开
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

while True:
    # 从摄像头读取一帧
    ret, frame = cap.read()
    
    # 检查是否成功读取
    if not ret:
        print("无法接收帧，摄像头可能已断开")
        break
    
    # 显示帧
    cv2.imshow('摄像头', frame)

    # 按下 'q' 键退出循环
    if cv2.waitKey(1) == ord('q'):
        break

# 释放摄像头资源并关闭窗口
cap.release()
cv2.destroyAllWindows()
