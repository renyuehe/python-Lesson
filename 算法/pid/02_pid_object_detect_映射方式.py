import math

import matplotlib.pyplot as plt
import time

class PID():
    def __init__(self, dt, max, min, Kp, Ki, Kd):

        self.dt = dt

        self.max = max  # 最大调整值
        self.min = min  # 最小调整值

        self.Kp = Kp  # 比例系数()
        self.Kd = Kd  # 微分系数(当参数为正时起到阻尼的效果,当参数为负则是助力的效果)
        self.Ki = Ki  # 积分系数(误差的积分,能够最终确保距离)

        self.integral = 0  # 积分和

        self.previous_error = 0  # 上一次偏差

        self.error = 0

    def calculate(self, setpoint, measured_value):

        self.error = setpoint - measured_value  # 计算得到偏差

        P_out = self.Kp * self.error  # 计算出比例值

        self.integral = self.integral + self.error * self.dt  # 计算得到累计误差
        I_out = self.Ki * self.integral  # 计算出积分值

        derivative = (self.error - self.previous_error) / self.dt
        D_out = self.Kd * derivative  # 计算出微分值

        self.previous_error = self.error  # 保存上一次偏差
        output = (P_out + I_out + D_out)

        if output > self.max:
            output = self.max

        if output < self.min:
            output = self.min

        return output

def caculatorAreaRadioDistance(view_size:tuple, target_size:tuple, set_point_scale = 0.3, power = 20):
    '''
    # 计算面积比, 并返回面积比于距离的映射公式
    :param view_size: 视图 (w,h)
    :param target_size: 目标框大小 (w,h)
    :param set_point_scale: 目标面积比
    :param power: 倍数
    :return: 面积比至目标比映射出的距离
    '''
    area1, area = target_size[0] * target_size[1] , view_size[0] * view_size[1]
    radio = area1/area
    print(radio)
    # radio = radio if radio < 0.5 else 0.5 # 面积比不会超过0.5
    radio = radio if radio < 1 else 1 # 面积比不会超过1

    # dis = set_point_scale - radio # 离 log1 的距离
    # log_dis = math.log(1 + dis)
    # distance = log_dis * power # 面积比和距离的映射公式

    raido_err = set_point_scale - radio #目标比例 - 当前比例

    # distance = (1/raido_err) * power #比例距离映射

    distance = math.tanh(raido_err * math.pi) * power
    # distance = distance if distance < 100 else 100
    return distance

# if __name__ == '__main__':
#     w, h = 10,10
#     w1, h1 = 0.1, 0.1
#     # w1, h1 = 0.01, 0.
#     distance = caculatorAreaRadioDistance((w,h), (w1, h1),set_point_scale=0.3,  power=200)
#     print(distance)
#     exit()


# 当面积比达到 0.5的时候小车停止前进


list_x = list()
list_y = list()

testPID = PID(dt=0.1, max=100, min=-100,
              Kp=0.2, Kd=0.01, Ki=0.01);

val = 20 #初始化位置
speed = 0 # 初始化速度
for point in range(0, 200):
    inc = testPID.calculate(0, val)

    speed += inc * 1 #速度 + 加速度*time
    val += speed * 1 #调整位置, 1是一个代码时间片,速度*time==调整的位置

    list_x.append(point)
    list_y.append(speed)

plt.scatter(list_x, list_y, alpha=0.6, edgecolors='white')

plt.plot(list_x,list_y)

plt.legend()

plt.show()
