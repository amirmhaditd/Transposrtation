"""
Transportation Rules Module

This module contains rules and regulations for truck transportation in Tehran, Iran.
"""

from dataclasses import dataclass
from typing import List, Optional
from enum import Enum


class VehicleType(Enum):
    """Types of trucks/vehicles"""
    LIGHT_TRUCK = "light_truck"  # Up to 3.5 tons
    MEDIUM_TRUCK = "medium_truck"  # 3.5 to 7.5 tons
    HEAVY_TRUCK = "heavy_truck"  # Above 7.5 tons
    SEMI_TRAILER = "semi_trailer"
    TANKER = "tanker"
    REFRIGERATED = "refrigerated"


class TimeRestriction(Enum):
    """Time-based restrictions"""
    NO_RESTRICTION = "no_restriction"
    DAYTIME_ONLY = "daytime_only"  # 6 AM to 10 PM
    NIGHTTIME_ONLY = "nighttime_only"  # 10 PM to 6 AM
    WEEKDAYS_ONLY = "weekdays_only"
    WEEKENDS_ONLY = "weekends_only"


@dataclass
class TransportationRule:
    """Represents a single transportation rule"""
    rule_id: str
    title: str
    description: str
    vehicle_types: List[VehicleType]
    time_restriction: TimeRestriction
    areas: List[str]  # Specific areas/zones in Tehran
    max_weight: Optional[float] = None  # Maximum weight in tons
    max_dimensions: Optional[dict] = None  # Max length, width, height in meters
    required_permits: List[str] = None
    exceptions: List[str] = None
    
    def __post_init__(self):
        if self.required_permits is None:
            self.required_permits = []
        if self.exceptions is None:
            self.exceptions = []


class TehranTransportationRules:
    """Container for all truck transportation rules in Tehran"""
    
    def __init__(self):
        self.rules: List[TransportationRule] = []
        self._load_rules()
    
    def _load_rules(self):
        """Load all transportation rules for Tehran"""
        # Zone restrictions
        self.rules.append(TransportationRule(
            rule_id="TEH-001",
            title="Restricted Zones in Central Tehran",
            description="Heavy trucks are prohibited from entering central Tehran zones during peak hours (7 AM - 9 PM)",
            vehicle_types=[VehicleType.HEAVY_TRUCK, VehicleType.SEMI_TRAILER],
            time_restriction=TimeRestriction.DAYTIME_ONLY,
            areas=["Central Tehran", "Downtown", "Valiasr Square", "Enghelab Square"],
            required_permits=["Special Entry Permit"]
        ))
        
        # Weight restrictions
        self.rules.append(TransportationRule(
            rule_id="TEH-002",
            title="Weight Limit on City Bridges",
            description="Maximum weight limit of 20 tons for trucks on city bridges and overpasses",
            vehicle_types=[VehicleType.HEAVY_TRUCK, VehicleType.SEMI_TRAILER],
            time_restriction=TimeRestriction.NO_RESTRICTION,
            areas=["All Tehran Bridges", "Overpasses"],
            max_weight=20.0,
            required_permits=["Bridge Crossing Permit"]
        ))
        
        # Nighttime restrictions
        self.rules.append(TransportationRule(
            rule_id="TEH-003",
            title="Nighttime Truck Movement",
            description="Heavy trucks allowed in residential areas only between 10 PM and 6 AM",
            vehicle_types=[VehicleType.HEAVY_TRUCK, VehicleType.SEMI_TRAILER],
            time_restriction=TimeRestriction.NIGHTTIME_ONLY,
            areas=["Residential Zones", "Residential Complexes"],
            exceptions=["Emergency vehicles", "Municipal services"]
        ))
        
        # Dimension restrictions
        self.rules.append(TransportationRule(
            rule_id="TEH-004",
            title="Maximum Vehicle Dimensions",
            description="Maximum dimensions for trucks: Length 12m, Width 2.5m, Height 4.5m",
            vehicle_types=[VehicleType.HEAVY_TRUCK, VehicleType.SEMI_TRAILER],
            time_restriction=TimeRestriction.NO_RESTRICTION,
            areas=["All Tehran"],
            max_dimensions={"length": 12.0, "width": 2.5, "height": 4.5}
        ))
        
        # Environmental restrictions
        self.rules.append(TransportationRule(
            rule_id="TEH-005",
            title="Environmental Zone Restrictions",
            description="Trucks older than 10 years are restricted from entering low-emission zones",
            vehicle_types=[VehicleType.LIGHT_TRUCK, VehicleType.MEDIUM_TRUCK, VehicleType.HEAVY_TRUCK],
            time_restriction=TimeRestriction.NO_RESTRICTION,
            areas=["Low-Emission Zones", "Environmental Zones"],
            required_permits=["Environmental Permit", "Emission Certificate"]
        ))
        
        # Highway restrictions
        self.rules.append(TransportationRule(
            rule_id="TEH-006",
            title="Highway Access",
            description="Heavy trucks must use designated lanes on highways and are restricted from left lanes",
            vehicle_types=[VehicleType.HEAVY_TRUCK, VehicleType.SEMI_TRAILER],
            time_restriction=TimeRestriction.NO_RESTRICTION,
            areas=["Tehran-Karaj Highway", "Tehran-Qom Highway", "Tehran-Saveh Highway"],
            exceptions=["Overtaking situations"]
        ))
        
        # Weekend restrictions
        self.rules.append(TransportationRule(
            rule_id="TEH-007",
            title="Weekend Truck Ban",
            description="Heavy trucks are banned from entering Tehran on Fridays (weekend)",
            vehicle_types=[VehicleType.HEAVY_TRUCK, VehicleType.SEMI_TRAILER],
            time_restriction=TimeRestriction.WEEKENDS_ONLY,
            areas=["All Tehran Entry Points"],
            exceptions=["Essential goods", "Emergency services", "With special permit"]
        ))
        
        # Tanker restrictions
        self.rules.append(TransportationRule(
            rule_id="TEH-008",
            title="Tanker Truck Regulations",
            description="Tanker trucks carrying hazardous materials require special permits and escort vehicles",
            vehicle_types=[VehicleType.TANKER],
            time_restriction=TimeRestriction.DAYTIME_ONLY,
            areas=["All Tehran"],
            required_permits=["Hazardous Materials Permit", "Escort Vehicle Authorization"],
            max_weight=25.0
        ))
        
        # Refrigerated truck rules
        self.rules.append(TransportationRule(
            rule_id="TEH-009",
            title="Refrigerated Truck Access",
            description="Refrigerated trucks carrying perishable goods have extended access hours (5 AM - 11 PM)",
            vehicle_types=[VehicleType.REFRIGERATED],
            time_restriction=TimeRestriction.DAYTIME_ONLY,
            areas=["Markets", "Distribution Centers", "Food Processing Areas"],
            required_permits=["Food Transport Permit"]
        ))
        
        # Construction vehicle rules
        self.rules.append(TransportationRule(
            rule_id="TEH-010",
            title="Construction Vehicle Regulations",
            description="Construction trucks are restricted to construction zones and require site-specific permits",
            vehicle_types=[VehicleType.HEAVY_TRUCK, VehicleType.MEDIUM_TRUCK],
            time_restriction=TimeRestriction.DAYTIME_ONLY,
            areas=["Construction Sites", "Designated Construction Routes"],
            required_permits=["Construction Site Permit", "Route Permit"]
        ))
    
    def get_rules_by_vehicle_type(self, vehicle_type: VehicleType) -> List[TransportationRule]:
        """Get all rules applicable to a specific vehicle type"""
        return [rule for rule in self.rules if vehicle_type in rule.vehicle_types]
    
    def get_rules_by_area(self, area: str) -> List[TransportationRule]:
        """Get all rules applicable to a specific area"""
        return [rule for rule in self.rules if area in rule.areas or "All Tehran" in rule.areas]
    
    def get_all_rules(self) -> List[TransportationRule]:
        """Get all transportation rules"""
        return self.rules.copy()
    
    def get_rule_by_id(self, rule_id: str) -> Optional[TransportationRule]:
        """Get a specific rule by its ID"""
        for rule in self.rules:
            if rule.rule_id == rule_id:
                return rule
        return None


# Global instance for easy access
tehran_rules = TehranTransportationRules()
