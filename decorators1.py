import time

# def timer(func): #func = count_calls(message) = count_calls.inner
#     def inner(*args, **kwargs):
#         begin = time.perf_counter()
#         r = func(*args, **kwargs)
#         finish = time.perf_counter()
#         t = finish - begin
#         print(f"{(t):.10f}")
#         return r
#     return inner

# def count_calls(func):
#     count = 0
#     def inner(*args, **kwargs):
#         nonlocal count
#         r = func(*args, **kwargs)
#         count += 1
#         print(count)
#         return r
#     return inner



# @timer
# @count_calls
# def message():  #message = timer(count_calls(message))
#     print("hello!")

# message()
# message()
# message()
# message()


# def repeat(n):
#     def dec(func):
#         def inner(*args, **kwargs):
#             for _ in range(n):
#                 r = func(*args, **kwargs)
#             return r
#         return inner
#     return dec

# @repeat(5)
# def message():  #message = repeat(3)(message)
#     print("new message")

# message()




# def limit(seconds):
#     def dec(func):
#         def inner(*args, **kwargs):
#             start = time.perf_counter()
#             r = func(*args, **kwargs)
#             end = time.perf_counter()
#             t = end - start
#             if t < seconds:
#                 return r
#             else:
#                 return "ban chem asum"
#         return inner
#     return dec

# @limit(1)
# def long_function():
#     print("before")
#     time.sleep(2)
#     return "after"

# print(long_function())



def timer(func): #func = count_calls(message) = count_calls.inner
    def inner(*args, **kwargs):
        begin = time.perf_counter()
        r = func(*args, **kwargs)
        finish = time.perf_counter()
        t = finish - begin
        print(f"{(t):.10f}")
        return r
    return inner


def factorial(n):
    if n == 2:
        return n
    else:
        return factorial(n - 1) * n
    
@timer
def factorial_helper(n):
    return factorial(n)
    
print(factorial_helper(5))