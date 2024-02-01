from queue_class import *


def queue_process():
    que = Queue()

    for i in range(1, 5):
        que.enqueue(i)

    print("Queue:", que)
    print("\nDequeue:", str(que.dequeue()))
    print("Peek:", que.peek)
    print("Queue:", que)

    for i in range(5, 9):
        que.enqueue(i)

    print("\nQueue:", que)
    print("Queue Tab:", str(que.tab))

    print("\nQueue Elements:")
    while not que.is_empty:
        print(str(que.dequeue()), end=" ")
    print()
    print(que)


if __name__ == '__main__':
    queue_process()
