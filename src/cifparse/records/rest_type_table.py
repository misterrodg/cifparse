class RestrictionTypeTable:
    def __init__(self):
        self.altitude_exclusion = "AE"  # Altitude Exclusion. The record contains altitudes, normally available, that are excluded from use for the Enroute Airway Segment. May be further restricted by “Time of Operation” information.
        self.cruising_table = "TC"  # Cruising Table Replacement. The record contains only a reference to a Cruising Table Identifier. That Cruise Table will be in force, replacing the Cruise Table Identifier in the Enroute Airway segment records defined in the “Start Fix/End Fix” fields.
        self.seasonal_restriction = "SC"  # Seasonal Restriction. Record is used to close an Airway or portion of an Airway on a seasonal basis.
        self.note_restriction = "NR"  # Note Restrictions. The record contains restrictions that do not fit the pattern of “formatted” information allowed by other “Restriction Record Types.”


rt_table = RestrictionTypeTable()
