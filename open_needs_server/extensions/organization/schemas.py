from pydantic import BaseModel
from open_needs_server.extensions.project.schemas import ProjectSchema


class OrganizationBaseSchema(BaseModel):
    title: str


class OrganizationCreateSchema(OrganizationBaseSchema):
    pass


class OrganizationSchema(OrganizationBaseSchema):
    id: int
    projects: list[ProjectSchema] = []

    class Config:
        orm_mode = True
