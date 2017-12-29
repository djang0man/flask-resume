import json

from flask import request, Response
from jsonschema import validate, ValidationError
from datetime import date, datetime

from . import models
from . import app
from .database import session

@app.route("/api/<user>", methods=["GET"])
def profile_get(user):
    """ Get resume details"""

    profiles = session.query(models.Profile)
    profile = profiles.filter(models.Profile.username == user).first()

    if profile:

        profile_data = []

        positions = session.query(models.Position)
        positions_at = positions.all()

        programs = session.query(models.Program)
        programs_at = programs.all()

        courses = session.query(models.Course)
        courses_at = courses.all()

        awards = session.query(models.Award)
        awards_at = awards.all()

        entries = session.query(models.Entry)
        entries_at = entries.all()

        skills = profile.skills
        companies = profile.companies
        schools = profile.schools
        institutions = profile.institutions
        projects = profile.projects

        def get_skills(skills_in):
            skills_data = []
            for skill in skills_in:
                skill = {
                    'id': skill.id,
                    'name': skill.name
                }
                skills_data.append(skill)
            return skills_data

        def get_companies(companies_in):
            companies_data = []
            for company in companies_in:
                company = {
                    'id': company.id,
                    'name': company.name,
                    'url': company.url,
                    'positions': get_positions(positions_at, company.id)
                }
                companies_data.append(company)
            return companies_data

        def get_positions(positions_in, company_id):
            positions_data = []
            for position in positions_in:
                if position.company_id == company_id:
                    position = {
                        'id': position.id,
                        'title': position.title,
                        'start_date': position.start_date,
                        'end_date': position.end_date if position.end_date else None,
                        'is_current': position.is_current,
                        'description': position.description
                    }
                    positions_data.append(position)
            return positions_data

        def get_schools(schools_in):
            schools_data = []
            for school in schools:
                school = {
                    'id': school.id,
                    'name': school.name,
                    'url': school.url,
                    'programs': get_programs(programs_at, school.id)
                }
                schools_data.append(school)
            return schools_data

        def get_programs(programs_in, school_id):
            programs_data = []
            for program in programs_in:
                if program.school_id == school_id:
                    program = {
                        'id': program.id,
                        'type': program.type,
                        'name': program.name,
                        'url': program.url,
                        'start_date': program.start_date,
                        'end_date': program.end_date if program.end_date else None,
                        'is_current': program.is_current,
                        'courses': get_courses(courses_at, program.id)
                    }
                    programs_data.append(program)
            return programs_data if len(programs_data) > 0 else None

        def get_courses(courses_in, program_id):
            courses_data = []
            for course in courses_in:
                if course.program_id == program_id:
                    course = {
                        'id': course.id,
                        'name': course.name,
                        'url': course.url
                    }
                    courses_data.append(course)
            return courses_data if len(courses_data) > 0 else None

        def get_projects(projects_in):
            projects_data = []
            for project in projects_in:
                project = {
                    'id': project.id,
                    'name': project.name,
                    'url': project.url
                }
                projects_data.append(project)
            return projects_data

        def get_institutions(institutions_in):
            institutions_data = []
            for institution in institutions_in:
                institution = {
                    'id': institution.id,
                    'name': institution.name,
                    'awards': get_awards(awards_at, institution.id)
                }
                institutions_data.append(institution)
            return institutions_data

        def get_awards(awards_in, institution_id):
            awards_data = []
            for award in awards_in:
                if award.institution_id == institution_id:
                    award = {
                        'id': award.id,
                        'name': award.name,
                        'entries': get_entries(award.entries)
                    }
                    awards_data.append(award)
            return awards_data if len(awards_data) > 0 else None

        def get_entries(entries_in):
            entries_data = []
            for entry in entries_in:
                entry = {
                    'id': entry.id,
                    'name': entry.name,
                    'url': entry.url
                }
                entries_data.append(entry)
            return entries_data if len(entries_data) > 0 else None

        profile = {
            "id": profile.id,
            "username": profile.username,
            "details": {
                "name": profile.name,
                "stack_overflow": profile.stack_overflow,
                "github": profile.github,
                "linkedin": profile.linkedin,
                "email": profile.email,
                "location": profile.location,
                "about": profile.about
            },
            "skills": get_skills(skills),
            "companies": get_companies(companies),
            "schools": get_schools(schools),
            "projects": get_projects(projects),
            "awards": get_institutions(institutions)
        }

        profile_data.append(profile)

    if profile:
        data = json.dumps(profile_data[0], sort_keys=False,
                          indent=4, separators=(',', ': '))
        return Response(data, 200, mimetype="application/json")
    else:
        data = json.dumps([{"error": "username not found :("}], sort_keys=False,
                          indent=4, separators=(',', ': '))
        return Response(data, 404, mimetype="application/json")
