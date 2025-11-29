from queue import Queue
from random import randint
from time import sleep


REQUEST_EXEC_TIME = 2
REQUEST_TYPES = [
    "POST /api/users",
    "GET /api/products",
    "PUT /api/users/me",
    "DELETE /api/sessions/me",
    "GET /index.html",
]


class Request:
    """Class for storing Request info.

    Attributes:
        id (int)
        line (str)
    """

    next_id = 1

    def __init__(self) -> None:
        self.id = Request.next_id
        # Fill request with random task
        self.line = REQUEST_TYPES[randint(0, len(REQUEST_TYPES) - 1)]
        Request.next_id += 1

    def __str__(self) -> str:
        return f"Request #{self.id}: {self.line}"


def generate_request() -> int:
    """Generate Request and put it to queue.

    Returns:
        int: ID of the generated Request.
    """
    req = Request()
    q.put(req)
    return req.id


def process_request() -> None:
    """Imitate execution of the queue's next Request and print info."""
    if not q.empty():
        req = q.get()
        pre_output = f"RUN {req} ... ".ljust(50)
        print(pre_output, end="", flush=True)
        # Imitate task execution
        sleep(REQUEST_EXEC_TIME)
        # Print execution status and current queue state
        print(f"Done.".ljust(70 - len(pre_output)), end="")
        q_str = render_queue()
        print(q_str, flush=True)
    else:
        print("Queue is empty.", flush=True)


def render_queue() -> str:
    """Render Queue content string."""
    return str([item.id for item in q.queue])


if __name__ == "__main__":
    q = Queue()

    while True:
        try:
            # Generate 0 to 3 new tasks and print current queue
            for _ in range(randint(0, 3)):
                id_ = generate_request()
                q_str = render_queue()
                # Hardcode green color for quick demo
                print("\x1b[32m", end="")
                print(f"ADD Request #{id_}.".ljust(70), end="")
                print(f"{q_str}\x1b[0m", flush=True)
                sleep(0.5)

            # Execute from 1 to 2 tasks
            for _ in range(randint(1, 2)):
                process_request()
                sleep(0.5)
        except (KeyboardInterrupt, EOFError):
            print("\nProgram interrupted by user.")
            break
