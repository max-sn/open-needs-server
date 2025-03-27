from pydantic import BaseModel
from open_needs_server.extensions.project.schemas import ProjectSchema


class OrganizationBaseSchema(BaseModel):
    title: str


class OrganizationCreateSchema(OrganizationBaseSchema):
    pass


class OrganizationShortSchema(OrganizationBaseSchema):
    id: int

    class Config:
        from_attributes = True


class OrganizationReturnSchema(OrganizationShortSchema):
    id: int
    # projects: list[ProjectSchema] = []

    class Config:
        from_attributes = True
