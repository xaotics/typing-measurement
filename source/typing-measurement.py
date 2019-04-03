import keyboard 
import time

def update_state(event):
    global  start_time
    if not start_time:
        start_time = time.time()    
    if event.event_type == 'up' and event.scan_code == 57: # when space bar released
        type_sequence = ''.join(current_state)        
        if type_sequence in candidate:
            print(type_sequence.rjust(6), '|', f'{round(time.time() - start_time, 3):6.3f}' , '秒')
        start_time = None
        current_state.clear()
    elif event.event_type == 'up':
        current_state.append(event.name)
    else:
        pass
    
current_state = []
start_time = None

candidate = input('輸入想測的字(以空白隔開)：').split()

print('以下開始記錄(按esc結束)')
print('----------------------')

keyboard.hook(update_state)
keyboard.wait('esc')
print('----------------------')
input('')