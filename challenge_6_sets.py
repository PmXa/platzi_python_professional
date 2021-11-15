# ---------------------------
# Main function & entry point
# ---------------------------

def run():
    old_users = [x for x in range(41) if x%2 == 0]
    new_users = [x for x in range(41) if x%3 == 1]
    ugly_numbers = [x for x in range(100) if x%2 == 0]

    old_users = set(old_users)
    new_users = set(new_users)
    ugly_numbers = set(ugly_numbers)

    special_members = set()
    special_members.add(0)

    # Union
    users = old_users | new_users

    # Intersection
    suspicious_users = old_users & new_users
    special_members.update([-1, 1], suspicious_users)

    # Difference
    banned = users - ugly_numbers

    # Symmetric difference
    normal_users = old_users ^ new_users

    # Results
    print(f"{len(users)} total users: {users}")
    print(f"{len(normal_users)} normal users: {normal_users}")
    print(f"{len(suspicious_users)} strange users: {suspicious_users}")
    print(f"{len(special_members)} special users: {special_members}")
    print(f"{len(banned)} banned users: {banned}")


if __name__ == '__main__':
    run()