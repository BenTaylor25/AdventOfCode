
SAMPLE_FILENAME = "sample_launch_safety_manual_sheets.txt"
FILENAME = "launch_safety_manual_sheets.txt"

RULE_DELIMETER = '|'
UPDATE_DELIMETER = ','

def get_rules_and_updates_from_file(filename):
    rules = []
    updates = []

    with open(filename) as f:
        for line in f.readlines():
            line = line.strip('\n')

            if RULE_DELIMETER in line:
                rule_params = line.strip().split(RULE_DELIMETER)
                rule_params = [int(x) for x in rule_params]

                assert len(rule_params) == 2

                rules.append(rule_params)

            elif UPDATE_DELIMETER in line:
                pages_to_update = line.strip().split(UPDATE_DELIMETER)
                pages_to_update = [int(x) for x in pages_to_update]

                updates.append(pages_to_update)

    return rules, updates

def filter_updates_by_rules(rules, updates):
    valid_updates = []

    for update in updates:
        update_is_valid = True

        for rule in rules:
            all_rule_components_in_update = set(rule).issubset(set(update))

            if all_rule_components_in_update:
                first_rel_page = rule[0]
                last_rel_page = rule[1]

                first_page_in_rule_is_first = update.index(first_rel_page) < update.index(last_rel_page)

                if not first_page_in_rule_is_first:
                    update_is_valid = False
                    break

        if update_is_valid:
            valid_updates.append(update)

    return valid_updates

def get_middle_page_numbers(updates):
    middle_page_numbers = []

    for update in updates:
        # How should I handle even-sized updates?
        mid_idx = len(update) // 2
        middle_page_number = update[mid_idx]

        middle_page_numbers.append(middle_page_number)

    return middle_page_numbers

def sum_of_middle_page_numbers(filename):
    rules, updates = get_rules_and_updates_from_file(filename)

    updates = filter_updates_by_rules(rules, updates)
    # for update in updates:
    #     print(update)
    # print()

    middle_page_numbers = get_middle_page_numbers(updates)
    # print(middle_page_numbers)

    return sum(middle_page_numbers)

if __name__ == "__main__":
    print(sum_of_middle_page_numbers(FILENAME))
