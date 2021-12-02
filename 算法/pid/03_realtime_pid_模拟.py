import time

import matplotlib.pyplot as plt

class PID():
    def __init__(self, dt, max, min, Kp, Kd, Ki):
        # self.dt = dt  # 采样周期
        self.max = max  # 最大调整值
        self.min = min  # 最小调整值

        self.Kp = Kp  # 比例系数
        self.Kd = Kd  # 积分系数
        self.Ki = Ki  # 微分系数

        self.integral = 0  # 积分和
        self.previous_error = 0  # delta_t 产生偏差
        self.error = 0 #当前位置距离目标位置的偏差


    def calculate(self, setpoint, measured_value, delta_time):
        '''
        :param setpoint: 目标位置
        :param measured_value:  当前位置
        :param 传入一次函数真实时间
        :return: 返回需要调整的速度
        '''

        self.error = setpoint - measured_value  # 计算得到偏差

        P_out = self.Kp * self.error  # 计算出比例值
        self.integral = self.integral + self.error * delta_time  # 计算得到积分累加和

        I_out = self.Ki * self.integral  # 计算出积分值
        derivative = (self.error - self.previous_error) / delta_time

        D_out = self.Kd * derivative  # 计算出微分值

        self.previous_error = self.error  # 保存上一次偏差
        output = (P_out + I_out + D_out)

        if output > self.max:
            output = self.max

        if output < self.min:
            output = self.min

        return output

plt.ion()
list_x = list()
list_y = list()

pos_x = list()
pos_y = list()

testPID = PID(dt=0.1, max=100, min=-100,
              Kp=0.2, Kd=0.5, Ki=0.01);

val = 20 # 初始化位置
speed = 0 # 初始化速度
lasttime = time.time()
plt.pause(0.05)
for point in range(0, 200):
    curtime = time.time()
    deltatime = curtime - lasttime # 求得间距的系统真实时间
    lasttime = time.time()

    inc = testPID.calculate(0, val, deltatime) # 返回一个加速度
    speed += inc * deltatime # 速度 + 加速度*time
    val += speed * deltatime # 调整位置, 1是一个代码时间片,速度*time==调整的位置

    list_x.append(point)
    list_y.append(speed)

    pos_x.append(point)
    pos_y.append(val)

    plt.scatter(list_x, list_y, alpha=0.6,  c='yellow')
    p1, = plt.plot(list_x,list_y)

    plt.scatter(pos_x, pos_y, alpha=0.6, c='red')
    p2, = plt.plot(pos_x, pos_y, c='red')

    plt.legend([p1, p2], ["speed", "pos"], loc="upper right")

    plt.pause(0.05)
# plt.show()