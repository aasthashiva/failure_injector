import time
import functools
import logging
from failure_injector.policies import FailurePolicy
from failure_injector.metrics import metrics


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


class FailureInjector:
    def __init__(self, policy: FailurePolicy):
        self.policy = policy

    def inject(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            metrics.total_calls += 1
            failure = self.policy.pick_failure()

            if failure == "timeout":
                metrics.timeouts += 1
                logging.warning("Injected timeout")
                time.sleep(1)
                raise TimeoutError("Injected failure: timeout")

            if failure == "exception":
                metrics.exceptions += 1
                logging.error("Injected exception")
                raise RuntimeError("Injected failure: exception")

            if failure == "slowdown":
                metrics.slowdowns += 1
                logging.info("Injected slowdown")
                time.sleep(self.policy.slowdown_seconds)

            result = func(*args, **kwargs)
            metrics.successes += 1
            logging.info("Call succeeded")
            return result

        return wrapper
