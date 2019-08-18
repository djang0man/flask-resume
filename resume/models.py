from sqlalchemy import Table, Column, Integer, String, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship

from .database import Base, engine, session

skills_relationship = \
    Table('relationship_skills', Base.metadata,
          Column('skill_id', Integer, ForeignKey('skill.id')),
          Column('profile_id', Integer, ForeignKey('profile.id')))

companies_relationship = \
    Table('relationship_companies', Base.metadata,
          Column('company_id', Integer, ForeignKey('company.id')),
          Column('profile_id', Integer, ForeignKey('profile.id')))

schools_relationship = \
    Table('relationship_schools', Base.metadata,
          Column('school_id', Integer, ForeignKey('school.id')),
          Column('profile_id', Integer, ForeignKey('profile.id')))

institutions_relationship = \
    Table('relationship_institutions', Base.metadata,
          Column('institution_id', Integer, ForeignKey('institution.id')),
          Column('profile_id', Integer, ForeignKey('profile.id')))

entries_relationship = \
    Table('relationship_entries', Base.metadata,
          Column('entry_id', Integer, ForeignKey('entry.id')),
          Column('award_id', Integer, ForeignKey('award.id')))


class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    stack_overflow = Column(String(128), unique=True)
    github = Column(String(128), unique=True)
    linkedin = Column(String(128), unique=True)
    email = Column(String(128), unique=True)
    username = Column(String(64), unique=True)
    location = Column(String(128))
    about = Column(Text())

    skills = relationship("Skill", secondary=skills_relationship, backref="profile")
    companies = relationship("Company", secondary=companies_relationship, backref="profile")
    schools = relationship("School", secondary=schools_relationship, backref="profile")
    institutions = relationship("Institution", secondary=institutions_relationship, backref="profile")
    projects = relationship("Project")


class Skill(Base):
    __tablename__ = "skill"
    # many to many (Profile)
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)


class Company(Base):
    __tablename__ = "company"
    # many to many (Profile)
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    url = Column(String(256))
    positions = relationship("Position")


class School(Base):
    __tablename__ = "school"
    # many to many (Profile)
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    url = Column(String(256))
    programs = relationship("Program")


class Institution(Base):
    __tablename__ = "institution"
    # many to many (Profile)
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    url = Column(String(256))
    awards = relationship("Award")


class Position(Base):
    __tablename__ = "position"
    # one to many (Company)
    id = Column(Integer, primary_key=True)
    title = Column(String(128))
    start_date = Column(String(64))
    end_date = Column(String(64), nullable="True")
    is_current = Column(Boolean(), default=False)
    description = Column(Text(), nullable="True")
    company_id = Column(Integer, ForeignKey('company.id'))


class Program(Base):
    __tablename__ = "program"
    # one to many (School)
    id = Column(Integer, primary_key=True)
    type = Column(String(64), nullable="True")
    name = Column(String(128))
    url = Column(String(256))
    start_date = Column(String(64))
    end_date = Column(String(64), nullable="True")
    is_current = Column(Boolean(), default=False)
    school_id = Column(Integer, ForeignKey('school.id'))
    courses = relationship("Course")


class Course(Base):
    __tablename__ = "course"
    # one to many (Program)
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    url = Column(String(256))
    program_id = Column(Integer, ForeignKey('program.id'))


class Award(Base):
    __tablename__ = "award"
    # one to many (Institution)
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    institution_id = Column(Integer, ForeignKey('institution.id'))
    entries = relationship("Entry", secondary=entries_relationship, backref="award")


class Entry(Base):
    __tablename__ = "entry"
    # many to many (Award)
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    url = Column(String(256))


class Project(Base):
    __tablename__ = "project"
    # one to many (Profile)
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    url = Column(String(256))
    profile_id = Column(Integer, ForeignKey('profile.id'))
