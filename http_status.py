import platform

requests = [200, 404, 200, 405, 404]
print("EC2 Python lab v1")
print(f"Runtime: {platform.system()} / Python {platform.python_version()}")
for status in sorted(set(requests)):
    print(f"HTTP {status}: {requests.count(status)}")
print(f"Total: {len(requests)}")
