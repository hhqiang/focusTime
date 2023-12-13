import time

def focus_timer(duration):
    print("专注时钟开始！")
    time.sleep(duration)
    print("专注时间结束！")

if __name__ == "__main__":
    focus_duration = 25 * 60  # 专注时长，以秒为单位，这里设置为25分钟
    focus_timer(focus_duration)
