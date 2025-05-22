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
from sqlite3 import Cursor

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

    def to_db(self, db_cursor: Cursor) -> None:
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

    def find_vhf_navaid(self, vhf_navaid_id: str) -> VHFNavaid:
        return self._vhf_navaids.get_navaid_by_id(vhf_navaid_id)

    def get_ndb_navaids(self) -> list[NDBNavaid]:
        return self._ndb_navaids.records

    def find_ndb(self, ndb_navaid_id: str) -> NDBNavaid:
        return self._ndb_navaids.get_navaid_by_id(ndb_navaid_id)

    def get_enroute_waypoints(self) -> list[Waypoint]:
        return self._enroute_waypoints.records

    def find_enroute_waypoint(self, waypoint_id: str) -> Waypoint:
        return self._enroute_waypoints.get_waypoint_by_id(waypoint_id)

    def get_airway_markers(self) -> list[AirwayMarker]:
        return self._airway_markers.records

    def find_airway_marker(self, airway_marker_id: str) -> AirwayMarker:
        return self._airway_markers.get_marker_by_id(airway_marker_id)

    def get_holds(self) -> list[Hold]:
        return self._holds.records

    def get_airway_points(self) -> list[AirwayPoint]:
        return self._airway_points.records

    def find_airway_points(self, airway_id: str) -> list[AirwayPoint]:
        return self._airway_points.get_airway_points_by_id(airway_id)

    def get_preferred_routes(self) -> list[PreferredRoute]:
        return self._preferred_routes.records

    def find_preferred_route(self, preferred_route_id: str) -> PreferredRoute:
        return self._preferred_routes.get_preferred_route_by_id(preferred_route_id)

    def get_airway_restrictions(self) -> list[AirwayRestriction]:
        return self._airway_restrictions.records

    def find_airway_restriction(self, airway_id: str) -> AirwayRestriction:
        return self._airway_restrictions.get_airway_restrictions_by_id(airway_id)

    def get_enroute_comms(self) -> list[EnrouteComm]:
        return self._enroute_comms.records

    def get_heliports(self) -> list[Heliport]:
        return self._heliports.records

    def find_heliport(self, heliport_id: str) -> Heliport:
        return self._heliports.get_heliport_by_id(heliport_id)

    def get_heli_terminal_waypoints(self) -> list[HeliWaypoint]:
        return self._heli_terminal_waypoints.records

    def find_heli_terminal_waypoint(self, waypoint_id: str) -> HeliWaypoint:
        return self._heli_terminal_waypoints.get_heli_waypoint_by_id(waypoint_id)

    def get_heli_procedures(self) -> list[HeliProcedure]:
        return self._heli_procedures.records

    def find_heli_procedure(self, heliport_id: str, procedure_id: str) -> HeliProcedure:
        return self._heli_procedures.get_heli_procedure_by_id(heliport_id, procedure_id)

    def get_heli_taas(self) -> list[HeliTAA]:
        return self._heli_taas.records

    def find_heli_taa(self, heliport_id: str, iap_id: str) -> HeliTAA:
        return self._taas.get_taa_by_id(heliport_id, iap_id)

    def get_heli_msas(self) -> list[HeliMSA]:
        return self._heli_msas.records

    def find_heli_msas_for_heliport(self, heliport_id: str) -> list[HeliMSA]:
        return self._heli_msas.get_msa_by_id(heliport_id)

    def get_heli_terminal_comms(self) -> list[HeliTerminalComm]:
        return self._heli_terminal_comms.records

    def get_airports(self) -> list[Airport]:
        return self._airports.records

    def find_airport(self, airport_id: str) -> Airport:
        return self._airports.get_airport_by_id(airport_id)

    def get_gates(self) -> list[Gate]:
        return self._gates.records

    def find_gate_by_id(self, airport_id: str, gate_id: str) -> Gate:
        return self._gates.get_gate_by_id(airport_id, gate_id)

    def get_terminal_waypoints(self) -> list[Waypoint]:
        return self._terminal_waypoints.records

    def find_terminal_waypoint(self, terminal_waypoint_id: str) -> Waypoint:
        return self._terminal_waypoints.get_waypoint_by_id(terminal_waypoint_id)

    def get_procedures(self) -> list[ProcedurePoint]:
        return self._procedures.records

    def find_procedure(self, airport_id: str, procedure_id: str) -> ProcedurePoint:
        return self._procedures.get_procedure_by_id(airport_id, procedure_id)

    def get_runways(self) -> list[Runway]:
        return self._runways.records

    def find_runway(self, airport_id: str, runway_id: str) -> Runway:
        return self._runways.get_runway_by_id(airport_id, runway_id)

    def get_loc_gss(self) -> list[LOC_GS]:
        return self._loc_gss.records

    def find_loc_gs(self, airport_id: str, loc_gs_id: str) -> LOC_GS:
        return self._loc_gss.get_loc_gs_by_id(airport_id, loc_gs_id)

    def get_company_routes(self) -> list[CompanyRoute]:
        return self._company_routes.records

    def find_company_routes_by_origin(self, origin_id: str) -> list[CompanyRoute]:
        return self._company_routes.get_company_route_by_origin(origin_id)

    def get_alternate_records(self) -> list[AlternateRecord]:
        return self._alternate_records.records

    def find_alternate_records_by_point(self, point_id: str) -> list[AlternateRecord]:
        return self._alternate_records.get_alternate_records_by_point(point_id)

    def get_taas(self) -> list[TAA]:
        return self._taas.records

    def find_taa(self, airport_id: str, iap_id: str) -> TAA:
        return self._taas.get_taa_by_id(airport_id, iap_id)

    def get_mlss(self) -> list[MLS]:
        return self._mlss.records

    def find_mls(self, facility_id: str, mls_id: str) -> MLS:
        return self._mlss.get_mls_by_id(facility_id, mls_id)

    def get_terminal_markers(self) -> list[TerminalMarker]:
        return self._terminal_markers.records

    def find_terminal_marker(self, facility_id: str, marker_id: str) -> TerminalMarker:
        return self._terminal_markers.get_marker_by_id(facility_id, marker_id)

    def get_path_points(self) -> list[PathPoint]:
        return self._path_points.records

    def get_flight_plannings(self) -> list[FlightPlanning]:
        return self._flight_plannings.records

    def find_flight_plannings_for_airport(
        self, airport_id: str
    ) -> list[FlightPlanning]:
        return self._flight_plannings.get_flight_planning_by_airport_id(airport_id)

    def get_msas(self) -> list[MSA]:
        return self._msas.records

    def find_msas_for_airport(self, airport_id: str) -> list[MSA]:
        return self._msas.get_msa_by_id(airport_id)

    def find_gls(self, facility_id: str, gls_id: str) -> GLS:
        return self._glss.get_gls_by_id(facility_id, gls_id)

    def get_terminal_comms(self) -> list[TerminalComm]:
        return self._terminal_comms.records

    def get_fir_uir(self) -> list[FIRUIR]:
        return self._fir_uirs.records

    def find_fir_uir(self, fir_uir_id: str) -> FIRUIR:
        return self._fir_uirs.get_fir_uir_by_id(fir_uir_id)

    def get_cruise_tables(self) -> list[CruiseTable]:
        return self._cruise_tables.records

    def get_reference_tables(self) -> list[ReferenceTable]:
        return self._reference_tables.records

    def find_reference_table_by_id(self, table_id: str) -> ReferenceTable:
        return self._reference_tables.get_reference_table_by_id(table_id)

    def get_controlled(self) -> list[Controlled]:
        return self._controlleds.records

    def find_controlled(self, center_id: str) -> list[Controlled]:
        return self._controlleds.get_controlled_by_id(center_id)

    def get_restrictive(self) -> list[Restrictive]:
        return self._restrictives.records

    def find_restrictive_match(self, restrictive_name: str) -> list:
        return self._restrictives.get_restrictive_match(restrictive_name)

    def find_restrictive(self, restrictive_id: str) -> list[Restrictive]:
        return self._restrictives.get_restrictive_by_id(restrictive_id)
