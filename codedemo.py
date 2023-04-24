vexcode_vision_11_objects = None
vexcode_vision_11_object_index = None
myVariable = 0

def when_started1():
    global myVariable, vexcode_vision_11_objects, vexcode_vision_11_object_index
    motor_9.set_stopping(HOLD)
    motor_9.set_velocity(100, PERCENT)
    motor_2.set_velocity(100, PERCENT)
    motor_2.spin(REVERSE)
    drivetrain.set_turn_velocity(25, PERCENT)
    for repeat_count in range(3):
        while True:
            vexcode_vision_11_objects = vision_11.take_snapshot(vision_11__BRIGHTYELLOW)
            if vexcode_vision_11_objects and len(vexcode_vision_11_objects) > 0:
                if vexcode_vision_11_objects[vexcode_vision_11_object_index].centerX > 180:
                    drivetrain.turn_for(LEFT, urandom.uniform(1, 5), DEGREES, wait=True)
                    drivetrain.drive_for(FORWARD, 1, INCHES, wait=True)
                if vexcode_vision_11_objects[vexcode_vision_11_object_index].centerX < 165:
                    drivetrain.turn_for(RIGHT, urandom.uniform(1, 5), DEGREES, wait=True)
                    drivetrain.drive_for(FORWARD, 1, INCHES, wait=True)
                if vexcode_vision_11_objects[vexcode_vision_11_object_index].centerX > 170 and vexcode_vision_11_objects[vexcode_vision_11_object_index].centerX < 180:
                    if vexcode_vision_11_objects[vexcode_vision_11_object_index].centerX > 166 and vexcode_vision_11_objects[vexcode_vision_11_object_index].centerX < 182 or vexcode_vision_11_objects[vexcode_vision_11_object_index].centerX == 175:
                        drivetrain.drive(FORWARD)
                if distance_12.object_distance(MM) < 250:
                    drivetrain.stop()
                    wait(1, SECONDS)
                    motor_9.spin(FORWARD)
            else:
                drivetrain.stop()
            vexcode_vision_11_objects = vision_11.take_snapshot(vision_11__BLUU)
            if vexcode_vision_11_objects and len(vexcode_vision_11_objects) > 0:
                drivetrain.drive(FORWARD)
                vexcode_vision_11_objects = vision_11.take_snapshot(vision_11__BLUU)
                if distance_12.object_distance(MM) < 100:
                    drivetrain.stop()
                    wait(1, SECONDS)
                    motor_2.spin(FORWARD)
                    drivetrain.drive_for(REVERSE, 90, INCHES, wait=True)
                    wait(10, SECONDS)
                    motor_9.spin(REVERSE)
                    wait(3, SECONDS)
                    motor_2.spin(REVERSE)
                    wait(3, SECONDS)
                    drivetrain.stop()
                    break
            else:
                pass
            wait(5, MSEC)
        wait(5, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True
rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)

when_started1()
