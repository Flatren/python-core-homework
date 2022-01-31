from fetcher import get
CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    import time
    def wrapper(func):
        def wrapper_arg(url):
            res = None
            all_time = 0
            for i in range(num):
                start_time = time.time()
                res = func(url)
                end_time = time.time() - start_time
                all_time += end_time
                print (i,"---",end_time," s")
            print ("avg time --- ",all_time/num," s")
            return res
        return wrapper_arg
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)

