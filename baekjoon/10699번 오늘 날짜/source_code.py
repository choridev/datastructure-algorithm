from datetime import timezone, datetime

now = datetime.now(timezone.utc)

print(now.date())