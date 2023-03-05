from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split(" ")]
locks = deque(int(x) for x in input().split(" "))
earned = int(input())

bullet_count = 0
reload = barrel_size

while locks:
    if not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        raise SystemExit

    current_bullet = bullets.pop()
    bullet_count += 1
    current_lock = locks.popleft()

    if current_bullet <= current_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.insert(0, current_lock)

    reload -= 1
    if reload == 0 and bullets:
        print("Reloading!")
        reload = barrel_size

print(f"{len(bullets)} bullets left. Earned ${earned - bullet_count * bullet_price}" )