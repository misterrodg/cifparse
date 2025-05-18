class ApplicationTable:
    def __init__(self):
        self.standard = (
            "A"  # A standard Continuation containing notes or other formatted data
        )
        self.combined = (
            "B"  # Combined Controlling Agency/Call Sign and formatted Time of Operation
        )
        self.callsign = "C"  # Call Sign/Controlling Agency Continuation
        self.extension = "E"  # Primary Record Extension
        self.limitation = "L"  # VHF Navaid Limitation Continuation
        self.narrative = "N"  # A Sector Narrative Continuation
        self.time = "T"  # A Time of Operations Continuation, “formatted time data”
        self.nar_time = "U"  # A Time of Operations Continuation “Narrative time data”
        self.se_time = "V"  # A Time of Operations Continuation, Start/End Date
        self.planning = "P"  # A Flight Planning Application Continuation
        self.planning_continuation = (
            "Q"  # A Flight Planning Application Primary Data Continuation
        )
        self.simulation = "S"  # Simulation Application Continuation
        self.procedure = "W"  # An Airport or Heliport Procedure Data Continuation with SBAS use authorization information


a_table = ApplicationTable()
