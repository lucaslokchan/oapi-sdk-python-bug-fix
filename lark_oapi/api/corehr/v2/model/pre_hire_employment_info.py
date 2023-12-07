# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .enum import Enum
from .job_data_cost_center import JobDataCostCenter


class PreHireEmploymentInfo(object):
    _types = {
        "department_id": str,
        "cost_center_rates": List[JobDataCostCenter],
        "office_location_id": str,
        "work_location_id": str,
        "work_station": str,
        "worker_id": str,
        "compensation_type": Enum,
        "direct_leader_id": str,
        "job_id": str,
        "job_family_id": str,
        "job_level_id": str,
        "job_grade_id": str,
        "job_title": str,
        "employee_type_id": str,
        "employment_type": str,
        "work_email": str,
        "company_id": str,
        "social_security_city_id": str,
        "non_compete_covenant": bool,
        "weekly_working_hours": int,
        "rehire": str,
        "rehire_employment_id": str,
        "working_hours_type": str,
        "weekly_working_hours_v2": float,
    }

    def __init__(self, d=None):
        self.department_id: Optional[str] = None
        self.cost_center_rates: Optional[List[JobDataCostCenter]] = None
        self.office_location_id: Optional[str] = None
        self.work_location_id: Optional[str] = None
        self.work_station: Optional[str] = None
        self.worker_id: Optional[str] = None
        self.compensation_type: Optional[Enum] = None
        self.direct_leader_id: Optional[str] = None
        self.job_id: Optional[str] = None
        self.job_family_id: Optional[str] = None
        self.job_level_id: Optional[str] = None
        self.job_grade_id: Optional[str] = None
        self.job_title: Optional[str] = None
        self.employee_type_id: Optional[str] = None
        self.employment_type: Optional[str] = None
        self.work_email: Optional[str] = None
        self.company_id: Optional[str] = None
        self.social_security_city_id: Optional[str] = None
        self.non_compete_covenant: Optional[bool] = None
        self.weekly_working_hours: Optional[int] = None
        self.rehire: Optional[str] = None
        self.rehire_employment_id: Optional[str] = None
        self.working_hours_type: Optional[str] = None
        self.weekly_working_hours_v2: Optional[float] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PreHireEmploymentInfoBuilder":
        return PreHireEmploymentInfoBuilder()


class PreHireEmploymentInfoBuilder(object):
    def __init__(self) -> None:
        self._pre_hire_employment_info = PreHireEmploymentInfo()

    def department_id(self, department_id: str) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.department_id = department_id
        return self

    def cost_center_rates(self, cost_center_rates: List[JobDataCostCenter]) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.cost_center_rates = cost_center_rates
        return self

    def office_location_id(self, office_location_id: str) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.office_location_id = office_location_id
        return self

    def work_location_id(self, work_location_id: str) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.work_location_id = work_location_id
        return self

    def work_station(self, work_station: str) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.work_station = work_station
        return self

    def worker_id(self, worker_id: str) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.worker_id = worker_id
        return self

    def compensation_type(self, compensation_type: Enum) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.compensation_type = compensation_type
        return self

    def direct_leader_id(self, direct_leader_id: str) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.direct_leader_id = direct_leader_id
        return self

    def job_id(self, job_id: str) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.job_id = job_id
        return self

    def job_family_id(self, job_family_id: str) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.job_family_id = job_family_id
        return self

    def job_level_id(self, job_level_id: str) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.job_level_id = job_level_id
        return self

    def job_grade_id(self, job_grade_id: str) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.job_grade_id = job_grade_id
        return self

    def job_title(self, job_title: str) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.job_title = job_title
        return self

    def employee_type_id(self, employee_type_id: str) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.employee_type_id = employee_type_id
        return self

    def employment_type(self, employment_type: str) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.employment_type = employment_type
        return self

    def work_email(self, work_email: str) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.work_email = work_email
        return self

    def company_id(self, company_id: str) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.company_id = company_id
        return self

    def social_security_city_id(self, social_security_city_id: str) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.social_security_city_id = social_security_city_id
        return self

    def non_compete_covenant(self, non_compete_covenant: bool) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.non_compete_covenant = non_compete_covenant
        return self

    def weekly_working_hours(self, weekly_working_hours: int) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.weekly_working_hours = weekly_working_hours
        return self

    def rehire(self, rehire: str) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.rehire = rehire
        return self

    def rehire_employment_id(self, rehire_employment_id: str) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.rehire_employment_id = rehire_employment_id
        return self

    def working_hours_type(self, working_hours_type: str) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.working_hours_type = working_hours_type
        return self

    def weekly_working_hours_v2(self, weekly_working_hours_v2: float) -> "PreHireEmploymentInfoBuilder":
        self._pre_hire_employment_info.weekly_working_hours_v2 = weekly_working_hours_v2
        return self

    def build(self) -> "PreHireEmploymentInfo":
        return self._pre_hire_employment_info
