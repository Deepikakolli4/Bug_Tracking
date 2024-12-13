
# Bug Tracking System

A simple bug-tracking system that allows developers to log, resolve, and filter bugs based on their priority. It is intended to help development teams efficiently manage and address software issues.

## Features

- **Log Bugs**: Developers can log new bugs, providing a title, description, and priority.

- **Resolve Bugs**: Mark bugs as resolved once they have been fixed.

- **Filter Bugs**: View and filter bugs based on their priority (e.g., high, medium, low) and resolution status (resolved or unresolved).

## Installation

### Prerequisites

- Python 3.x or later

### Steps to Run the Application

1\. Clone the repository to your local machine:

```bash

git clone https://github.com/yourusername/bug-tracking-system.git

Navigate into the project folder:

bash

Copy code

cd bug-tracking-system

(Optional) Create a virtual environment to keep dependencies isolated:

bash

Copy code

python3 -m venv venv

source venv/bin/activate # On Windows, use venv\Scripts\activate

Run the Python file directly:

bash

Copy code

python bug_tracker.py

Usage

1\. Log a New Bug

To log a bug, call the log_bug method with the following parameters:

title: A short description of the bug.

description: A detailed explanation of the bug.

priority: The severity level of the bug (e.g., "High", "Medium", "Low").

Example:

python

Copy code

tracker.log_bug("Bug 1", "Null pointer exception in module X", "High")

2\. Resolve a Bug

To mark a bug as resolved, use the resolve_bug method with the bug object.

Example:

python

Copy code

tracker.resolve_bug(bug)

3\. Filter Bugs by Priority and Resolution

To view unresolved high-priority bugs, use the get_bugs method with the appropriate filters for priority and resolution.

Example:

python

Copy code

unresolved_high_priority_bugs = tracker.get_bugs(priority="High", resolved=False)

4\. View All Bugs

To view all bugs logged, you can simply print the bug tracker:

python

Copy code

print(tracker)

Code Structure

bug_tracker.py: Contains the main logic for the bug-tracking system, including the Bug and BugTracker classes.

Bug Class: Represents an individual bug with title, description, priority, and resolution status.

BugTracker Class: Manages the list of bugs and provides methods to log, resolve, and filter bugs.
