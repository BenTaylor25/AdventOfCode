
FILENAME = "reactor_levels.txt"
SAMPLE_FILENAME = "sample_reactor_levels.txt"

MIN = 1
MAX = 3

def get_reports_from_file(filename):
    reports = []
    with open(filename) as f:
        for line in f:
            report_as_str = line.strip('\n').split(' ')
            report_as_int = [int(x) for x in report_as_str]
            reports.append(report_as_int)

    return reports

def is_report_safe_default(report, min_delta, max_delta):
    if len(report) < 2:
        # Edge case?
        return True

    if report[0] == report[1]:
        return False

    should_descend = report[0] > report[1]

    for i in range(len(report) - 1):
        current_level = report[i]
        next_level = report[i + 1]

        is_descending = current_level > next_level

        if should_descend != is_descending:
            return False

        if not min_delta <= abs(current_level - next_level) <= max_delta:
            return  False

    return True


def reactor_safety_check(filename, is_report_safe, min_delta, max_delta):
    reports = get_reports_from_file(filename)

    reports_safety_validation = list(map(lambda x : is_report_safe(x, min_delta, max_delta), reports))

    number_of_safe_reports = reports_safety_validation.count(True)
    return number_of_safe_reports

if __name__ == "__main__":
    print(reactor_safety_check(FILENAME, is_report_safe_default, MIN, MAX))
