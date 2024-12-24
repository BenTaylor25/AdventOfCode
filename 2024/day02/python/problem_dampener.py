from reactor_safety_check import *

def is_report_safe_dampened(report, min_delta, max_delta):
    for i in range(len(report)):
        sub_report = [x for j, x in enumerate(report) if j != i]

        if is_report_safe_default(sub_report, min_delta, max_delta):
            return True
    return False

if __name__ == "__main__":
    print(reactor_safety_check(FILENAME, is_report_safe_dampened, MIN, MAX))
