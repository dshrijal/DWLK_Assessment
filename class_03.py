import time

def is_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()         

        output = func(*args, **kwargs)

        end = time.time()           

        print(f"Execution time: {end - start:.6f} seconds")

        return output

    return wrapper