
import time
import webbrowser

class Pomodoro():
    """A Pomodoro class to countdown and help you workout"""

    __name='pomodoro-workout clock' #a private class attribute
    work_time=25 #25
    short_break=5 #5
    long_break=20 #20

    def __init__(self,username):
        self.username=username
        
    def countdown(self,minutes, notify_msg):
        """The magic method to countdown and print a notify message"""
        start = time.perf_counter() # a time to start counting
        while True:
            passed_seconds = int(round(time.perf_counter() - start)) # the time has passed
            left_seconds = minutes * 60 - passed_seconds #the left time
            if left_seconds < 0:
                print('')
                break
            bar_time = '{}:{} ⏰'.format(int(left_seconds / 60), int(left_seconds % 60))
            self.__bar(passed_seconds, minutes * 60, 25, bar_time)
            time.sleep(1)
        print(notify_msg)
        return
    
    def __bar(self,passed, total, bar_len=25, bar_time=''):
        """A private method to show a progress bar in terminal"""
        percentage=passed / total
        tomato = round(percentage * bar_len)
        print('\r','🍅' * tomato + '**' * (bar_len - tomato), '[{:.0%}]'.format(percentage), bar_time, end='')
        return

    def workout(self,url):
        """A public method to open the online workout vedio"""
        return webbrowser.open(url)

    def stretching(self,url):
        """A public method to open the online stretch vedio"""
        return webbrowser.open(url)
    
    def __str__(self) -> str:
        return f'This is the Pomodoro class of {self.__name}'
    
if __name__=='__main__':#two pubic method tests
    pomo=Pomodoro('pomo')
    assert pomo.stretching('wwww.google.com')==True
    print('Public method streching works as expected.')

    assert pomo.workout('www.google.com')==True 
    print('Public method workout works as expected.')



