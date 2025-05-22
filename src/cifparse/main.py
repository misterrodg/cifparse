from .records.validity import Validity

from .sections import Sections

from .records.moras import MORA, MORAs
from .records.vhf_navaids import VHFNavaid, VHFNavaids
from .records.ndb_navaids import NDBNavaid, NDBNavaids
from .records.waypoints import Waypoint, Waypoints
from .records.airway_markers import AirwayMarker, AirwayMarkers
from .records.holds import Hold, Holds
from .records.airway_points import AirwayPoint, AirwayPoints
from .records.preferred_routes import PreferredRoute, PreferredRoutes
from .records.airway_restrictions import AirwayRestriction, AirwayRestrictions
from .records.enroute_comms import EnrouteComm, EnrouteComms
from .records.heliports import Heliport, Heliports
from .records.heli_waypoints import HeliWaypoint, HeliWaypoints
from .records.heli_procedures import HeliProcedure, HeliProcedures
from .records.heli_taas import HeliTAA, HeliTAAs
from .records.heli_msas import HeliMSA, HeliMSAs
from .records.heli_terminal_comms import HeliTerminalComm, HeliTerminalComms
from .records.airports import Airport, Airports
from .records.airport_gates import Gate, Gates
from .records.procedures import ProcedurePoint, ProcedurePoints
from .records.runways import Runway, Runways
from .records.loc_gss import LOC_GS, LOC_GSs
from .records.company_routes import CompanyRoute, CompanyRoutes
from .records.alternate_records import AlternateRecord, AlternateRecords
from .records.taas import TAA, TAAs
from .records.mlss import MLS, MLSs
from .records.terminal_markers import TerminalMarker, TerminalMarkers
from .records.path_points import PathPoint, PathPoints
from .records.flight_plannings import FlightPlanning, FlightPlannings
from .records.msas import MSA, MSAs
from .records.glss import GLS, GLSs
from .records.terminal_comms import TerminalComm, TerminalComms
from .records.cruise_tables import CruiseTable, CruiseTables
from .records.reference_tables import ReferenceTable, ReferenceTables
from .records.controlleds import Controlled, Controlleds
from .records.fir_uirs import FIRUIR, FIRUIRs
from .records.restrictives import Restrictive, Restrictives


import os
import re

from datetime import datetime, timedelta
from sqlite3 import connect

CYCLE_LENGTH_DAYS = 28


class CIFP:
    _exists: bool
    _file_path: str
    _cycle_id: str
    _effective_from: str
    _effective_to: str

    _sections: Sections

    _moras: MORAs
    _vhf_navaids: VHFNavaids
    _ndb_navaids: NDBNavaids
    _enroute_waypoints: Waypoints
    _airway_markers: AirwayMarkers
    _holds: Holds
    _airway_points: AirwayPoints
    _preferred_routes: PreferredRoutes
    _airway_restrictions: AirwayRestrictions
    _enroute_comms: EnrouteComms
    _heliports: Heliports
    _heli_terminal_waypoints: HeliWaypoints
    _heli_procedures: HeliProcedures
    _heli_taas: HeliTAAs
    _heli_msas: HeliMSAs
    _heli_terminal_comms: HeliTerminalComms
    _airports: Airports
    _gates: Gates
    _terminal_waypoints: Waypoints
    _procedures: ProcedurePoints
    _runways: Runways
    _loc_gss: LOC_GSs
    _company_routes: CompanyRoutes
    _alternate_records: AlternateRecords
    _taas: TAAs
    _mlss: MLSs
    _markers: TerminalMarkers
    _path_points: PathPoints
    _flight_plannings: FlightPlannings
    _msas: MSAs
    _glss: GLSs
    _terminal_comms: TerminalComms
    _cruise_tables: CruiseTables
    _reference_tables: ReferenceTables
    _controlleds: Controlleds
    _fir_uirs: FIRUIRs
    _restrictives: Restrictives

    def __init__(self, path: str) -> None:
        self._exists = False
        self._file_path = ""
        self._cycle_id = None
        self._effective_from = None
        self._effective_to = None

        self._sections = None

        self._moras = None
        self._vhf_navaids = None
        self._ndb_navaids = None
        self._enroute_waypoints = None
        self._airway_markers = None
        self._holds = None
        self._airway_points = None
        self._preferred_routes = None
        self._airway_restrictions = None
        self._enroute_comms = None
        self._heliports = None
        self._heli_terminal_waypoints = None
        self._heli_procedures = None
        self._heli_taas = None
        self._heli_msas = None
        self._heli_terminal_comms = None
        self._airports = None
        self._gates = None
        self._terminal_waypoints = None
        self._procedures = None
        self._runways = None
        self._loc_gss = None
        self._company_routes = None
        self._alternate_records = None
        self._taas = None
        self._mlss = None
        self._terminal_markers = None
        self._path_points = None
        self._flight_plannings = None
        self._msas = None
        self._glss = None
        self._terminal_comms = None
        self._cruise_tables = None
        self._reference_tables = None
        self._controlleds = None
        self._fir_uirs = None
        self._restrictives = None

        self._set_path(path)

        if self._exists:
            with open(self._file_path) as cifp_file:
                self._sections = Sections(cifp_file)

    def _set_path(self, path: str) -> None:
        self._file_path = path
        if os.path.exists(self._file_path):
            print(f"CIFP Parser :: Found CIFP file at: {path}")
            self._exists = True
        else:
            print(
                f"CIFP Parser :: Unable to find CIFP file at: {path} :: Interpreted as {path}"
            )
        return

    def _verify_date_format(self, text: str) -> bool:
        pattern = r"^(0[1-9]|[12]\d|3[01]) (JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC) \d{4}$"
        return bool(re.match(pattern, text))

    def _set_header(self) -> None:
        line = self._sections.get_header()
        self._cycle_id = line[80:84]
        effective_from_str = line[96:107]
        if self._verify_date_format(effective_from_str):
            effective_from_obj = datetime.strptime(effective_from_str, "%d %b %Y")
            self._effective_from = effective_from_obj.strftime("%Y-%m-%d")
            effective_to_obj = effective_from_obj + timedelta(days=CYCLE_LENGTH_DAYS)
            self._effective_to = effective_to_obj.strftime("%Y-%m-%d")
        return

    def to_db(self, db_file_path: str) -> None:
        if os.path.exists(db_file_path):
            os.remove(db_file_path)

        connection = connect(db_file_path)
        db_cursor = connection.cursor()

        self._set_header()
        validity = Validity(self._cycle_id, self._effective_from, self._effective_to)
        validity.to_db(db_cursor)

        if self._moras:
            self._moras.to_db(db_cursor)

        if self._vhf_navaids:
            self._vhf_navaids.to_db(db_cursor)

        if self._ndb_navaids:
            self._ndb_navaids.to_db(db_cursor)

        if self._enroute_waypoints:
            self._enroute_waypoints.to_db(db_cursor)

        if self._airway_markers:
            self._airway_markers.to_db(db_cursor)

        if self._holds:
            self._holds.to_db(db_cursor)

        if self._airway_points:
            self._airway_points.to_db(db_cursor)

        if self._preferred_routes:
            self._preferred_routes.to_db(db_cursor)

        if self._airway_restrictions:
            self._airway_restrictions.to_db(db_cursor)

        if self._enroute_comms:
            self._enroute_comms.to_db(db_cursor)

        if self._heliports:
            self._heliports.to_db(db_cursor)

        if self._heli_terminal_waypoints:
            self._heli_terminal_waypoints.to_db(db_cursor)

        if self._heli_procedures:
            self._heli_procedures.to_db(db_cursor)

        if self._heli_taas:
            self._heli_taas.to_db(db_cursor)

        if self._heli_msas:
            self._heli_msas.to_db(db_cursor)

        if self._heli_terminal_comms:
            self._heli_terminal_comms.to_db(db_cursor)

        if self._airports:
            self._airports.to_db(db_cursor)

        if self._gates:
            self._gates.to_db(db_cursor)

        if self._terminal_waypoints:
            self._terminal_waypoints.to_db(db_cursor)

        if self._procedures:
            self._procedures.to_db(db_cursor)

        if self._runways:
            self._runways.to_db(db_cursor)

        if self._loc_gss:
            self._loc_gss.to_db(db_cursor)

        if self._company_routes:
            self._company_routes.to_db(db_cursor)

        if self._alternate_records:
            self._alternate_records.to_db(db_cursor)

        if self._taas:
            self._taas.to_db(db_cursor)

        if self._mlss:
            self._mlss.to_db(db_cursor)

        if self._terminal_markers:
            self._terminal_markers.to_db(db_cursor)

        if self._path_points:
            self._path_points.to_db(db_cursor)

        if self._flight_plannings:
            self._flight_plannings.to_db(db_cursor)

        if self._msas:
            self._msas.to_db(db_cursor)

        if self._glss:
            self._glss.to_db(db_cursor)

        if self._terminal_comms:
            self._terminal_comms.to_db(db_cursor)

        if self._cruise_tables:
            self._cruise_tables.to_db(db_cursor)

        if self._reference_tables:
            self._reference_tables.to_db(db_cursor)

        if self._controlleds:
            self._controlleds.to_db(db_cursor)

        if self._fir_uirs:
            self._fir_uirs.to_db(db_cursor)

        if self._restrictives:
            self._restrictives.to_db(db_cursor)

        connection.commit()
        connection.close()
        return

    def parse_moras(self) -> None:
        if self._exists:
            self._moras = MORAs(self._sections.section_a.get_moras())
        return

    def parse_vhf_navaids(self) -> None:
        if self._exists:
            self._vhf_navaids = VHFNavaids(self._sections.section_d.get_vhf())
        return

    def parse_ndb_navaids(self) -> None:
        if self._exists:
            self._ndb_navaids = NDBNavaids(self._sections.section_d.get_ndb())
        return

    def parse_enroute_waypoints(self) -> None:
        if self._exists:
            self._enroute_waypoints = Waypoints(
                self._sections.section_e.get_enroute_waypoints()
            )
        return

    def parse_airway_markers(self) -> None:
        if self._exists:
            self._airway_markers = AirwayMarkers(
                self._sections.section_e.get_airway_markers()
            )
        return

    def parse_holds(self) -> None:
        if self._exists:
            self._holds = Holds(self._sections.section_e.get_holding_patterns())
        return

    def parse_airway_points(self) -> None:
        if self._exists:
            self._airway_points = AirwayPoints(
                self._sections.section_e.get_airway_points()
            )
        return

    def parse_preferred_routes(self) -> None:
        if self._exists:
            self._preferred_routes = PreferredRoutes(
                self._sections.section_e.get_preferred_routes()
            )
        return

    def parse_airway_restrictions(self) -> None:
        if self._exists:
            self._airway_restrictions = AirwayRestrictions(
                self._sections.section_e.get_airway_restrictions()
            )
        return

    def parse_enroute_comms(self) -> None:
        if self._enroute_comms:
            self._enroute_comms = EnrouteComms(
                self._sections.section_e.get_communication()
            )
        return

    def parse_heliports(self) -> None:
        if self._exists:
            self._heliports = Heliports(self._sections.section_h.get_heliports())
        return

    def parse_heli_terminal_waypoints(self) -> None:
        if self._exists:
            self._heli_terminal_waypoints = HeliWaypoints(
                self._sections.section_h.get_terminal_waypoints()
            )
        return

    def parse_heli_procedures(self) -> None:
        if self._exists:
            heli_procedures_lines = []
            heli_procedures_lines.extend(self._sections.section_h.get_sids())
            heli_procedures_lines.extend(self._sections.section_h.get_stars())
            heli_procedures_lines.extend(self._sections.section_h.get_iaps())
            self._heli_procedures = HeliProcedures(heli_procedures_lines)
        return

    def parse_heli_taas(self) -> None:
        if self._exists:
            self._heli_taas = HeliTAAs(self._sections.section_h.get_taas())
        return

    def parse_heli_msas(self) -> None:
        if self._exists:
            self._heli_msas = HeliMSAs(self._sections.section_h.get_msas())
        return

    def parse_heli_terminal_comms(self) -> None:
        if self._exists:
            self._heli_terminal_comms = HeliTerminalComms(
                self._sections.section_h.get_communications()
            )
        return

    def parse_airports(self) -> None:
        if self._exists:
            self._airports = Airports(self._sections.section_p.get_airports())
        return

    def parse_gates(self) -> None:
        if self._gates:
            self._gates = Gates(self._sections.section_p.get_airport_gates())
        return

    def parse_terminal_waypoints(self) -> None:
        if self._exists:
            self._terminal_waypoints = Waypoints(
                self._sections.section_p.get_terminal_waypoints(), True
            )
        return

    def parse_procedures(self) -> None:
        if self._exists:
            procedures_lines = []
            procedures_lines.extend(self._sections.section_p.get_sids())
            procedures_lines.extend(self._sections.section_p.get_stars())
            procedures_lines.extend(self._sections.section_p.get_iaps())
            self._procedures = ProcedurePoints(procedures_lines)
        return

    def parse_runways(self) -> None:
        if self._exists:
            self._runways = Runways(self._sections.section_p.get_runways())
        return

    def parse_loc_gss(self) -> None:
        if self._exists:
            self._loc_gss = LOC_GSs(self._sections.section_p.get_loc_gss())
        return

    def parse_company_routes(self) -> None:
        if self._exists:
            self._company_routes = CompanyRoutes(
                self._sections.section_r.get_company_routes()
            )
        return

    def parse_alternate_records(self) -> None:
        if self._exists:
            self._alternate_records = AlternateRecords(
                self._sections.section_r.get_alternate_records()
            )
        return

    def parse_taas(self) -> None:
        if self._exists:
            self._taas = TAAs(self._sections.section_p.get_taas())
        return

    def parse_mlss(self) -> None:
        if self._exists:
            self._mlss = MLSs(self._sections.section_p.get_mlss())
        return

    def parse_terminal_markers(self) -> None:
        if self._exists:
            self._terminal_markers = TerminalMarkers(
                self._sections.section_p.get_markers()
            )
        return

    def parse_path_points(self) -> None:
        if self._exists:
            self._path_points = PathPoints(self._sections.section_p.get_path_points())
        return

    def parse_flight_plannings(self) -> None:
        if self._exists:
            self._flight_plannings = FlightPlannings(
                self._sections.section_p.get_flight_plannings()
            )
        return

    def parse_msas(self) -> None:
        if self._exists:
            self._msas = MSAs(self._sections.section_p.get_msas())
        return

    def parse_glss(self) -> None:
        if self._exists:
            self._glss = GLSs(self._sections.section_p.get_glss())
        return

    def parse_terminal_comms(self) -> None:
        if self._exists:
            self._terminal_comms = TerminalComms(
                self._sections.section_p.get_communications()
            )
        return

    def parse_cruise_tables(self) -> None:
        if self._exists:
            self._cruise_tables = CruiseTables(
                self._sections.section_t.get_cruise_tables()
            )
        return

    def parse_reference_tables(self) -> None:
        if self._exists:
            self._reference_tables = ReferenceTables(
                self._sections.section_t.get_reference_tables()
            )
        return

    def parse_controlled(self) -> None:
        if self._exists:
            self._controlleds = Controlleds(self._sections.section_u.get_controlled())
        return

    def parse_fir_uir(self) -> None:
        if self._exists:
            self._fir_uirs = FIRUIRs(self._sections.section_u.get_fir_uir())
        return

    def parse_restrictive(self) -> None:
        if self._exists:
            self._restrictives = Restrictives(
                self._sections.section_u.get_restrictive()
            )
        return

    def parse(self) -> None:
        self.parse_moras()
        self.parse_vhf_navaids()
        self.parse_ndb_navaids()
        self.parse_enroute_waypoints()
        self.parse_airway_markers()
        self.parse_holds()
        self.parse_airway_points()
        self.parse_preferred_routes()
        self.parse_airway_restrictions()
        self.parse_enroute_comms()
        self.parse_heliports()
        self.parse_heli_terminal_waypoints()
        self.parse_heli_procedures()
        self.parse_heli_taas()
        self.parse_heli_msas()
        self.parse_heli_terminal_comms()
        self.parse_airports()
        self.parse_gates()
        self.parse_terminal_waypoints()
        self.parse_procedures()
        self.parse_runways()
        self.parse_loc_gss()
        self.parse_company_routes()
        self.parse_alternate_records()
        self.parse_taas()
        self.parse_mlss()
        self.parse_terminal_markers()
        self.parse_path_points()
        self.parse_flight_plannings()
        self.parse_msas()
        self.parse_glss()
        self.parse_terminal_comms()
        self.parse_cruise_tables()
        self.parse_reference_tables()
        self.parse_controlled()
        self.parse_fir_uir()
        self.parse_restrictive()
        return

    def get_moras(self) -> list[MORA]:
        return self._moras.records

    def get_vhf_navaids(self) -> list[VHFNavaid]:
        return self._vhf_navaids.records

    def get_ndb_navaids(self) -> list[NDBNavaid]:
        return self._ndb_navaids.records

    def get_enroute_waypoints(self) -> list[Waypoint]:
        return self._enroute_waypoints.records

    def get_airway_markers(self) -> list[AirwayMarker]:
        return self._airway_markers.records

    def get_holds(self) -> list[Hold]:
        return self._holds.records

    def get_airway_points(self) -> list[AirwayPoint]:
        return self._airway_points.records

    def get_preferred_routes(self) -> list[PreferredRoute]:
        return self._preferred_routes.records

    def get_airway_restrictions(self) -> list[AirwayRestriction]:
        return self._airway_restrictions.records

    def get_enroute_comms(self) -> list[EnrouteComm]:
        return self._enroute_comms.records

    def get_heliports(self) -> list[Heliport]:
        return self._heliports.records

    def get_heli_terminal_waypoints(self) -> list[HeliWaypoint]:
        return self._heli_terminal_waypoints.records

    def get_heli_procedures(self) -> list[HeliProcedure]:
        return self._heli_procedures.records

    def get_heli_taas(self) -> list[HeliTAA]:
        return self._heli_taas.records

    def get_heli_msas(self) -> list[HeliMSA]:
        return self._heli_msas.records

    def get_heli_terminal_comms(self) -> list[HeliTerminalComm]:
        return self._heli_terminal_comms.records

    def get_airports(self) -> list[Airport]:
        return self._airports.records

    def get_gates(self) -> list[Gate]:
        return self._gates.records

    def get_terminal_waypoints(self) -> list[Waypoint]:
        return self._terminal_waypoints.records

    def get_procedures(self) -> list[ProcedurePoint]:
        return self._procedures.records

    def get_runways(self) -> list[Runway]:
        return self._runways.records

    def get_loc_gss(self) -> list[LOC_GS]:
        return self._loc_gss.records

    def get_company_routes(self) -> list[CompanyRoute]:
        return self._company_routes.records

    def get_alternate_records(self) -> list[AlternateRecord]:
        return self._alternate_records.records

    def get_taas(self) -> list[TAA]:
        return self._taas.records

    def get_mlss(self) -> list[MLS]:
        return self._mlss.records

    def get_terminal_markers(self) -> list[TerminalMarker]:
        return self._terminal_markers.records

    def get_path_points(self) -> list[PathPoint]:
        return self._path_points.records

    def get_flight_plannings(self) -> list[FlightPlanning]:
        return self._flight_plannings.records

    def get_msas(self) -> list[MSA]:
        return self._msas.records

    def get_glss(self) -> list[GLS]:
        return self._glss.records

    def get_terminal_comms(self) -> list[TerminalComm]:
        return self._terminal_comms.records

    def get_fir_uir(self) -> list[FIRUIR]:
        return self._fir_uirs.records

    def get_cruise_tables(self) -> list[CruiseTable]:
        return self._cruise_tables.records

    def get_reference_tables(self) -> list[ReferenceTable]:
        return self._reference_tables.records

    def get_controlled(self) -> list[Controlled]:
        return self._controlleds.records

    def get_restrictive(self) -> list[Restrictive]:
        return self._restrictives.records
