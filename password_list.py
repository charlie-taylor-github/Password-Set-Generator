import time as t

class PasswordList:
    def __init__(self, set: list, length: int):
        self.__set = set
        self.__length = length
        self.__time_at_log = 0
        self.__log_interval = 1
    
    @property
    def amount(self):
        return len(self.__set) ** self.__length

    def set_log_interval(self, t: float):
        self.__log_interval = t
    
    def write_to_file(self, dir: str, log_progress: bool=False):
        def write(pw):
            self.__write_pw_to_file(pw, dir)
        self.execute_each_pw(write, log_progress)
    
    def display(self, log_progress: bool=False):
        def display_pw(pw):
            print(pw)
        self.execute_each_pw(display_pw, log_progress)

    def execute_each_pw(self, execute: callable, log_progress: bool=False):
        pw = self.__set[0] * self.__length
        self.__start_time = t.time()
        execute(pw)
        for i in range(1, self.amount):
            pw = self.__get_next_pw(pw)
            execute(pw)
            self.__attempt_log(i, log_progress)
        self.__attempt_log(self.amount, log_progress)
        self.__start_time = 0
    
    def __attempt_log(self, i: int, log_progress: bool=False):
        due_log = t.time() - self.__time_at_log >= self.__log_interval
        if not log_progress or not due_log:
            return
        self.__time_at_log = t.time()
        self.__log(i)
    
    def __log(self, i: int):
        total_time = t.time() - self.__start_time
        pws_ps = i / total_time
        time_left = (self.amount - i) / pws_ps
        percent = int(i*100/self.amount)
        txt = f'{str(percent)}% | {i} of {self.amount} | {int(total_time)}s | {int(pws_ps)} pws/s | {int(time_left)}s left'
        print(txt)

    def __get_incr_char(self, c: str):
        if self.__set.index(c) < len(self.__set) - 1:
            return self.__set[self.__set.index(c) + 1]
    
    def __get_next_pw(self, pw: str):
        pw = "".join(pw)
        for i in range(self.__length):
            reverse_i = self.__length - i - 1
            incr_char = self.__get_incr_char(pw[reverse_i])
            if incr_char:
                start = pw[: reverse_i]
                end = self.__set[0] * (self.__length - reverse_i - 1)
                return start + incr_char + end
    
    def __write_pw_to_file(self, pw: str, dir: str):
        with open(dir, 'a') as f:
            f.write(pw + '\n')
