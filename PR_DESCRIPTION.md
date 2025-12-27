# Gather all the rules for truck transportation at Tehran

## Summary
This PR implements a comprehensive rules system for truck transportation in Tehran, Iran. It provides a structured data model and API to access all relevant transportation rules, restrictions, and regulations.

## Changes Made

### New Files
- **`transportation_rules.py`**: Main module containing:
  - `VehicleType` enum: Categorizes trucks (light, medium, heavy, semi-trailer, tanker, refrigerated)
  - `TimeRestriction` enum: Defines time-based restrictions (daytime, nighttime, weekends, etc.)
  - `TransportationRule` dataclass: Represents individual rules with all relevant metadata
  - `TehranTransportationRules` class: Container and API for accessing all rules

- **`test_transportation_rules.py`**: Comprehensive test suite covering:
  - Rule loading and retrieval
  - Filtering by vehicle type and area
  - Rule structure validation
  - Weight and dimension restrictions
  - Permit requirements
  - Vehicle-specific rules (tankers, refrigerated trucks)

### Rules Implemented
The implementation includes 10 comprehensive rules covering:

1. **TEH-001**: Restricted zones in central Tehran (peak hour restrictions)
2. **TEH-002**: Weight limits on city bridges (20 tons max)
3. **TEH-003**: Nighttime truck movement in residential areas
4. **TEH-004**: Maximum vehicle dimensions (12m x 2.5m x 4.5m)
5. **TEH-005**: Environmental zone restrictions for older vehicles
6. **TEH-006**: Highway access and lane restrictions
7. **TEH-007**: Weekend truck ban (Fridays)
8. **TEH-008**: Tanker truck regulations (hazardous materials)
9. **TEH-009**: Refrigerated truck access (perishable goods)
10. **TEH-010**: Construction vehicle regulations

## API Usage

```python
from transportation_rules import tehran_rules, VehicleType

# Get all rules
all_rules = tehran_rules.get_all_rules()

# Get rules for specific vehicle type
heavy_truck_rules = tehran_rules.get_rules_by_vehicle_type(VehicleType.HEAVY_TRUCK)

# Get rules for specific area
central_rules = tehran_rules.get_rules_by_area("Central Tehran")

# Get specific rule by ID
rule = tehran_rules.get_rule_by_id("TEH-001")
```

## Testing
- All tests pass successfully
- Test coverage includes:
  - Rule loading and structure validation
  - Filtering functionality
  - Edge cases (non-existent rules, empty filters)
  - Vehicle-specific and area-specific rule retrieval

## Design Decisions
- Used Python dataclasses for clean, type-safe rule representation
- Enum types for vehicle types and time restrictions ensure type safety
- Flexible data model supports weight, dimensions, permits, and exceptions
- Singleton pattern via global instance for easy access
- Comprehensive test suite ensures reliability

## Related
- Trello Card: [694fcab331f11847bc231bd1](https://trello.com/c/694fcab331f11847bc231bd1)
- Board: Transport
- List: In progress
