"""Stacks"""
# works on lifo principle:
# last in first out

browsing_session = []

browsing_session.append(1)

browsing_session.append(2)

browsing_session.append(3)

# you remove the last element first in stack:
last = browsing_session.pop()
print(f"last element removed: {last}")

print(f"New last element: {browsing_session[-1]}")

print(browsing_session)
browsing_session.pop()
browsing_session.pop()


if browsing_session:
    print("Back button available")
# the way to check for back button is empty or not:
elif not browsing_session:
    print("Back button diabled")
