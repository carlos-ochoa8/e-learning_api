from pydantic import Field, BaseModel


class CourseBaseSchema(BaseModel):
    name: str = Field(min_length=5)
    teacher: str = Field(min_length=5, max_length=80)
    description: str = Field(min_length=5)


class CourseCreateSchema(CourseBaseSchema):
    pass


class CourseUpdateSchema(CourseBaseSchema):
    pass


class CourseInDBSchema(CourseBaseSchema):
    id: int

    class Config:
        """
        Use SQLAlchemy to Pydantic
        """
        from_attributes = True


class CoursesInDBSchema(BaseModel):
    courses: list[CourseInDBSchema]
