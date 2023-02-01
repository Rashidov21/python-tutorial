
def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args,**kwargs)
        end = time.time()
        print(f'[*] Время выполнения: {round(end-start,2)} секунд.')
    return wrapper