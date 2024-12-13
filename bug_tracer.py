class Bug:
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority
        self.resolved = False

    def resolve(self):
        self.resolved = True

    def __str__(self):
        return f"Bug: {self.title}, Priority: {self.priority}, Resolved: {self.resolved}"

class BugTracker:
    def __init__(self):
        self.bugs = []

    def log_bug(self, title, description, priority):
        bug = Bug(title, description, priority)
        self.bugs.append(bug)

    def resolve_bug(self, bug):
        bug.resolve()

    def get_bugs(self, priority=None, resolved=None):
        filtered_bugs = self.bugs
        if priority:
            filtered_bugs = [bug for bug in filtered_bugs if bug.priority == priority]
        if resolved is not None:
            filtered_bugs = [bug for bug in filtered_bugs if bug.resolved == resolved]
        return filtered_bugs

    def __str__(self):
        return "\n".join(str(bug) for bug in self.bugs)

# Example usage
tracker = BugTracker()
tracker.log_bug("Bug 1", "Null pointer exception in module X", "High")
tracker.log_bug("Bug 2", "Layout issue on homepage", "Medium")
tracker.log_bug("Bug 3", "Performance lag in search functionality", "Low")

# Resolving a bug
tracker.resolve_bug(tracker.bugs[0])

# Get unresolved high-priority bugs
high_priority_bugs = tracker.get_bugs(priority="High", resolved=False)
print("Unresolved High Priority Bugs:")
if high_priority_bugs:
    for bug in high_priority_bugs:
        print(bug)
else:
    print("No unresolved high-priority bugs.")