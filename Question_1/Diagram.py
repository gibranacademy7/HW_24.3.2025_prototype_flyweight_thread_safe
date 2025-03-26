"""
Diagram:
           ┌───────────────────────┐
           │      Student          │
           ├───────────────────────┤
           │ - name: str           │
           │ - id: str             │
           │ - grades: Dict[int, float] │
           │ - is_active: bool     │
           ├───────────────────────┤
           │ + __init__(...)        │
           │ + add_grade(...)       │
           │ + get_average_grade()  │
           │ + toggle_active_status() │
           │ + clone()              │
           └───────────────────────┘
                      │
                      ▼
      ┌─────────────────────────────┐
      │        Prototype            │
      ├─────────────────────────────┤
      │  Uses deepcopy for cloning  │
      │  Ensures unique instances   │
      └─────────────────────────────┘
                      │
                      ▼
      ┌──────────────────────┐
      │   original_student   │
      │   ID: S12345         │
      │   Grades: {101: 85.5,│
      │           102: 90.0} │
      └──────────────────────┘
                      │ Clone()
                      ▼
      ┌──────────────────────┐
      │   duplicated_student │
      │   ID: S12345         │
      │   Grades: {101: 85.5,│
      │           102: 90.0, │
      │           103: 78.0} │
      └──────────────────────┘
"""