from time import time

class Timer:
    
    def __init__(self):
        self.start_times = {}
        self.elapsed_times = {}
        
    def start(self, name=None):
        name = 'global' if name is None else name
        assert name not in self.start_times.keys(), "timer '{name}' has already been started"
        self.start_times[name] = time()
        return self
        
    def stop(self, name=None):
        name = 'global' if name is None else name
        assert name in self.start_times.keys(), f"timer ''{name}' does not exit"

        elapsed_time = time() - self.start_times[name]
        if name not in self.elapsed_times.keys():
            self.elapsed_times[name] = 0
            
        self.elapsed_times[name] += elapsed_time

        del(self.start_times[name])
        
        return self
    
    def get(self, name=None):
        name = 'global' if name is None else name
        r = 0
        if name in self.elapsed_times.keys():
            r += self.elapsed_times[name]
            
        if name in self.start_times.keys():
            r += time() - self.start_times[name]
            
        return r