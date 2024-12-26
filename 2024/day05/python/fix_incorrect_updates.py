from launch_safety_manual_sheet import *

def fix(rules, invalid_updates):
    fixed_updates = []

    for invalid_update in invalid_updates:
        fixed_update = []

        for page in invalid_update:
            insertion_idx = 0
            for existing_page in fixed_update:
                for rule in rules:
                    rule_contains_both_pages = set(rule) == set((page, existing_page))

                    if rule_contains_both_pages:
                        if page == rule[1]:
                            insertion_idx += 1

            fixed_update.insert(insertion_idx, page)

        fixed_updates.append(fixed_update)

    return fixed_updates


def fix_incorrect_updates(filename):
    rules, updates = get_rules_and_updates_from_file(filename)

    valid_updates = filter_updates_by_rules(rules, updates)
    invalid_updates = [update for update in updates if update not in valid_updates]

    fixed_invalid_updates = fix(rules, invalid_updates)

    middle_page_numbers = get_middle_page_numbers(fixed_invalid_updates)

    return sum(middle_page_numbers)

if __name__ == "__main__":
    print(fix_incorrect_updates(FILENAME))
