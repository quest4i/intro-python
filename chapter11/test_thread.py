import threading


def do_this(what):
    whoami(what)


def whoami(what):
    print("Thread %s says: %s" % (threading.current_thread(), what))


if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = thread.Thread(target=do_this,
                          args=("Im function %s" % n,))
        p.start()



