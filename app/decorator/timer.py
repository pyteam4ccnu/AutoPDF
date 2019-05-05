import time


def Timer(func):
    def newFunc(*args, **args2):
        t0 = time.time()
        url = str(*args)
        tail = url.split("/")[-1]
        print("[%s], {%s} start" % (time.strftime("%X", time.localtime()), tail))
        back = func(*args, **args2)
        print("[%s], {%s} end" % (time.strftime("%X", time.localtime()), tail))
        print("-- Cost -- %.3fs for download." % (time.time() - t0))
        return back
    return newFunc
