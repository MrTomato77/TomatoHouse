class Time:                                   # ประกาศ class Time
    def __init__(self, hour, minute):         # กำหนด attribute ไว้ 2 ค่าเป็น ชั่วโมง กับ นาที
        self.hour = hour
        self.minute = minute

class ClockDisplay:                          # ประกาศ class ClockDisplay
    def __init__(self, hour, minute):        # กำหนด attribute ไว้ 2 ค่าเป็น ชั่วโมง กับ นาที
        self.time = Time(hour,minute)        # ดึงค่า ชั่วโมง กับ นาที จาก class Time มาใช้

    def tick(self):
        self.time.minute += 1                # เพิ่ม 1 นาทีทุกๆ การเรียกใช้ 1 ครั้ง
        
        if self.time.minute == 60:           # เมื่อค่านาทีเท่ากับ 60 จะทำการ reset ค่ากลับไปเป็น 0 แล้วเพิ่มค่าชั่วโมง +1
            self.time.hour += 1
            self.time.minute = 0
            
        if self.time.hour == 24:             # เมื่อค่าชั่วโมงเท่ากับ 24 จะทำการ reset ค่ากลับไปเป็น 0
            self.time.hour = 0
            
    def __str__(self):
        return f"{str(self.time.hour).zfill(2)}:{str(self.time.minute).zfill(2)}"         # จัดรูปแบบนาฬิกาด้วย f-string


#MAIN
clock1 = ClockDisplay(9, 15)
clock2 = ClockDisplay(22, 18)
for x in range(250):
    clock1.tick()
    clock2.tick()
    print(str(clock1) + ", "  + str(clock2))         # เวลาเพิ่มขึ้นทุกๆ 1 นาทีต้อ tick