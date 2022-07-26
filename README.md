# Basic GitHub API Demonstration

This project consists of two scripts, one in BASH, and one in Python, which do the same task.

These scripts query GitHub's API and return a list of open, non-pull request Issues, and their label names.

#### Usage:

BASH
```
./issues.sh https://github.com/algorand/pyteal
```

Python:
```
python3 issues.py https://github.com/algorand/pyteal
# Also valid is org/repo
python3 issues.py algorand/pyteal
```

#### Tests

```
python3 -m unittest tests/issues_test.py 
```

#### Output Sample

```json
    {
        "title": "ABI:  Support sequencing bare app call and method invocations",
        "number": 393,
        "labels": [
            "Team Scytale"
        ]
    },
    {
        "title": "Consolidate TEAL and AVM versioning",
        "number": 392,
        "labels": [
            "Team Scytale"
        ]
    },
    {
        "title": "More Efficient Scratch Slot Assignments in the ABI-Router",
        "number": 390,
        "labels": [
            "Team Scytale",
            "new-feature-request"
        ]
    },
    {
        "title": "AVM 8:  Opcode support",
        "number": 388,
        "labels": []
    },
    {
        "title": "Getter method `byte_srt` of `Bytes`",
        "number": 369,
        "labels": [
            "new-bug"
        ]
    },
    {
        "title": "ABI: ABI Subroutine Improvements",
        "number": 352,
        "labels": [
            "Team Scytale",
            "new-feature-request"
        ]
    },
    ...
]
```