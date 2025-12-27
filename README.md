# Transportation

A comprehensive system for managing truck transportation rules and regulations in Tehran, Iran.

## Features

- Structured data model for transportation rules
- Support for multiple vehicle types (light, medium, heavy trucks, tankers, etc.)
- Time-based restrictions (daytime, nighttime, weekends)
- Area-specific rules and zone restrictions
- Weight and dimension limitations
- Permit requirements tracking
- Comprehensive test coverage

## Usage

```python
from transportation_rules import tehran_rules, VehicleType

# Get all rules
all_rules = tehran_rules.get_all_rules()

# Get rules for heavy trucks
heavy_truck_rules = tehran_rules.get_rules_by_vehicle_type(VehicleType.HEAVY_TRUCK)

# Get rules for a specific area
central_rules = tehran_rules.get_rules_by_area("Central Tehran")
```

## Testing

Run tests with:
```bash
python3 -m unittest test_transportation_rules.py -v
```

## Files

- `transportation_rules.py`: Main module with rules data and API
- `test_transportation_rules.py`: Test suite
