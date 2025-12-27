"""
Tests for transportation rules module
"""

import unittest
from transportation_rules import (
    TehranTransportationRules,
    VehicleType,
    TimeRestriction,
    TransportationRule
)


class TestTehranTransportationRules(unittest.TestCase):
    """Test cases for TehranTransportationRules"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.rules = TehranTransportationRules()
    
    def test_rules_loaded(self):
        """Test that rules are loaded correctly"""
        all_rules = self.rules.get_all_rules()
        self.assertGreater(len(all_rules), 0, "Rules should be loaded")
    
    def test_get_rules_by_vehicle_type(self):
        """Test filtering rules by vehicle type"""
        heavy_truck_rules = self.rules.get_rules_by_vehicle_type(VehicleType.HEAVY_TRUCK)
        self.assertGreater(len(heavy_truck_rules), 0, "Should have rules for heavy trucks")
        
        # Verify all returned rules include HEAVY_TRUCK
        for rule in heavy_truck_rules:
            self.assertIn(VehicleType.HEAVY_TRUCK, rule.vehicle_types)
    
    def test_get_rules_by_area(self):
        """Test filtering rules by area"""
        central_rules = self.rules.get_rules_by_area("Central Tehran")
        self.assertGreater(len(central_rules), 0, "Should have rules for Central Tehran")
        
        # Verify all returned rules mention the area or apply to all Tehran
        for rule in central_rules:
            self.assertTrue(
                "Central Tehran" in rule.areas or "All Tehran" in rule.areas,
                f"Rule {rule.rule_id} should apply to Central Tehran"
            )
    
    def test_get_rule_by_id(self):
        """Test retrieving a specific rule by ID"""
        rule = self.rules.get_rule_by_id("TEH-001")
        self.assertIsNotNone(rule, "Rule TEH-001 should exist")
        self.assertEqual(rule.rule_id, "TEH-001")
        self.assertEqual(rule.title, "Restricted Zones in Central Tehran")
    
    def test_get_nonexistent_rule(self):
        """Test retrieving a non-existent rule"""
        rule = self.rules.get_rule_by_id("TEH-999")
        self.assertIsNone(rule, "Non-existent rule should return None")
    
    def test_rule_structure(self):
        """Test that rules have proper structure"""
        all_rules = self.rules.get_all_rules()
        for rule in all_rules:
            self.assertIsInstance(rule, TransportationRule)
            self.assertIsNotNone(rule.rule_id)
            self.assertIsNotNone(rule.title)
            self.assertIsNotNone(rule.description)
            self.assertGreater(len(rule.vehicle_types), 0)
            self.assertIsInstance(rule.time_restriction, TimeRestriction)
            self.assertGreater(len(rule.areas), 0)
    
    def test_weight_restrictions(self):
        """Test rules with weight restrictions"""
        weight_rules = [r for r in self.rules.get_all_rules() if r.max_weight is not None]
        self.assertGreater(len(weight_rules), 0, "Should have rules with weight restrictions")
        
        for rule in weight_rules:
            self.assertIsInstance(rule.max_weight, float)
            self.assertGreater(rule.max_weight, 0)
    
    def test_dimension_restrictions(self):
        """Test rules with dimension restrictions"""
        dimension_rules = [r for r in self.rules.get_all_rules() if r.max_dimensions is not None]
        self.assertGreater(len(dimension_rules), 0, "Should have rules with dimension restrictions")
        
        for rule in dimension_rules:
            self.assertIn("length", rule.max_dimensions)
            self.assertIn("width", rule.max_dimensions)
            self.assertIn("height", rule.max_dimensions)
    
    def test_required_permits(self):
        """Test rules with required permits"""
        permit_rules = [r for r in self.rules.get_all_rules() if len(r.required_permits) > 0]
        self.assertGreater(len(permit_rules), 0, "Should have rules requiring permits")
    
    def test_tanker_specific_rules(self):
        """Test that tanker trucks have specific rules"""
        tanker_rules = self.rules.get_rules_by_vehicle_type(VehicleType.TANKER)
        self.assertGreater(len(tanker_rules), 0, "Should have rules for tanker trucks")
        
        # Check that tanker rules mention hazardous materials or special permits
        has_hazardous_rule = any(
            "hazardous" in rule.description.lower() or "hazardous" in rule.title.lower()
            for rule in tanker_rules
        )
        self.assertTrue(has_hazardous_rule, "Should have hazardous materials rules for tankers")
    
    def test_refrigerated_truck_rules(self):
        """Test that refrigerated trucks have specific rules"""
        refrigerated_rules = self.rules.get_rules_by_vehicle_type(VehicleType.REFRIGERATED)
        self.assertGreater(len(refrigerated_rules), 0, "Should have rules for refrigerated trucks")
    
    def test_weekend_restrictions(self):
        """Test weekend restriction rules"""
        weekend_rules = [
            r for r in self.rules.get_all_rules()
            if r.time_restriction == TimeRestriction.WEEKENDS_ONLY
        ]
        self.assertGreater(len(weekend_rules), 0, "Should have weekend restriction rules")
    
    def test_nighttime_restrictions(self):
        """Test nighttime restriction rules"""
        nighttime_rules = [
            r for r in self.rules.get_all_rules()
            if r.time_restriction == TimeRestriction.NIGHTTIME_ONLY
        ]
        self.assertGreater(len(nighttime_rules), 0, "Should have nighttime restriction rules")


if __name__ == '__main__':
    unittest.main()
