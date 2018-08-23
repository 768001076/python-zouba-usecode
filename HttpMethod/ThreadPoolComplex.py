import threading
import queue
import contextlib
import time

StopLock = object()

class ThreadPool(object):

    def __init__(self,max_num):
        print('-----------Sta------------')
        self.queue = queue.Queue()
        self.max_num = max_num
        self.isStop = False
        self.real_list = []
        self.free_list = []

    def run(self,func,args=None,callback=None):
        if len(self.free_list) == 0 and len(self.real_list) < self.max_num:
            self.create_thread()
        w = (func,args,callback)
        self.queue.put(w)

    def create_thread(self):
        thread = threading.Thread(target=self.call)
        thread.start()

    def call(self):
        current_thread = threading.current_thread
        self.real_list.append(current_thread)
        event = self.queue.get()
        while event != StopLock:
            func,args,callback = event
            try:
                if args is not None:
                    result = func(*args)
                else:
                    result = func()
                status = True
            except Exception as e:
                status = False
                result = e
            if callback is not None:
                try:
                    callback(status,result)
                except:
                    pass
            if self.isStop:
                event = StopLock
            else:
                with self.worker_state(self.free_list,current_thread):
                    event = self.queue.get()
        else:
            self.real_list.remove(current_thread)

    @contextlib.contextmanager
    def worker_state(self, state_list, worker_thread):
        state_list.append(worker_thread)
        try:
            yield
        finally:
            state_list.remove(worker_thread)

    def close(self):
        num = len(self.free_list)
        while num > 0:
            self.queue.put(StopLock)
            num -= 1

    def terminate(self):
        self.isStop = True
        while len(self.free_list) > 0:
            self.queue.put(StopLock)
        self.queue.empty()
        while len(self.real_list) > 1:
            time.sleep(1)
        print('-----------END------------')
