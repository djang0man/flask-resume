from sqlalchemy import Table, Column, Integer, String, Sequence, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship

from .database import Base, engine, session

skills_relationship = Table('relationship_skills', Base.metadata,
    Column('skill_id', Integer, ForeignKey('skill.id')),
    Column('profile_id', Integer, ForeignKey('profile.id'))
)

companies_relationship = Table('relationship_companies', Base.metadata,
    Column('company_id', Integer, ForeignKey('company.id')),
    Column('profile_id', Integer, ForeignKey('profile.id'))
)

schools_relationship = Table('relationship_schools', Base.metadata,
    Column('school_id', Integer, ForeignKey('school.id')),
    Column('profile_id', Integer, ForeignKey('profile.id'))
)

institutions_relationship = Table('relationship_institutions', Base.metadata,
    Column('institution_id', Integer, ForeignKey('institution.id')),
    Column('profile_id', Integer, ForeignKey('profile.id'))
)

entries_relationship = Table('relationship_entries', Base.metadata,
    Column('entry_id', Integer, ForeignKey('entry.id')),
    Column('award_id', Integer, ForeignKey('award.id'))
)

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

'''

Base.metadata.create_all(engine)

stuart = Profile(name="Stuart Kershaw", stack_overflow="https://stackoverflow.com/users/2332112/stuart-kershaw", 
	    github="https://github.com/stuartkershaw", linkedin="https://www.linkedin.com/in/stuartkershaw", 
            email="stuartdkershaw@gmail.com", username="stuartdkershaw", location="Seattle, WA", 
            about="JavaScript and Python")

skills = [
    Skill(name="HTML"),
    Skill(name="CSS"),
    Skill(name="JavaScript"),
    Skill(name="React"),
    Skill(name="AngularJS"),
    Skill(name="Redux"),
    Skill(name="Node.js"),
    Skill(name="Jest"),
    Skill(name="webpack"),
    Skill(name="Babel"),
    Skill(name="Python"),
    Skill(name="Flask"),
    Skill(name="PostgresSQL"),
    Skill(name="MongoDB"),
    Skill(name="Mongoose"),
    Skill(name="HTTP"),
    Skill(name="REST"),
    Skill(name="XML"),
    Skill(name="XSLT"),
    Skill(name="Bash"),
    Skill(name="Git"),
    Skill(name="Github"),
]

companies = [
    Company(name="Knock Rentals", url="https://knockrentals.com/"),
    Company(name="Sabre Hospitality Solutions", url="http://sabrehospitality.com/"),
    Company(name="University of Iowa", url="https://uiowa.edu/")
]

schools = [
    School(name="Code Fellows", url="https://www.codefellows.org/"),
    School(name="University of Washington", url="http://www.washington.edu/"),
    School(name="University of Iowa", url="https://uiowa.edu/")
]

institutions = [
    Institution(name="Interactive Media Awards", url="https://interactivemediaawards.com/"),
    Institution(name="WebAwards", url="http://www.webaward.org/")
]

positions = [
    Position(title="Software Engineer", start_date="Jan 2018", is_current="true", company_id="1", 
        description=""),
    Position(title="Supervisor of Front End Development", start_date="Apr 2012", end_date="Jul 2017", company_id="2", 
        description="<ul>"\
            "<li>Led a team of developers in delivering award-winning websites to top hoteliers.</li> "\
            "<li>Built responsive web applications with HTML, CSS, and JavaScript.</li> "\
            "<li>Reviewed business documents and design compositions for project timeline feasibility.</li> "\
            "<li>Collaborated across teams to create RESTful JSON and XML APIs for new features.</li> "\
            "<li>Optimized responsive UI components for build efficiency, load performance, cross-platform rendering, and accessibility coverage.</li> "\
          "</ul>"),
    Position(title="Front End Developer", start_date="Oct 2009", end_date="Apr 2012", company_id="2", 
        description="<ul>"\
            "<li>Succeeded under tight deadlines with multiple daily deliverables.</li> "\
            "<li>Developed cross-browser, conversion-optimized booking solutions.</li> "\
            "<li>Built editable email templates for hotel and airline marketing campaigns.</li> "\
            "<li>Standardized library markup for content sharing across social network APIs.</li> "\
            "<li>Designed custom booking applications for direct reservations through Facebook.</li> "\
          "</ul>"),
    Position(title="Web Developer and Designer", start_date="Apr 2007", end_date="Feb 2009", company_id="3", 
        description="<ul>"\
            "<li>Built fully custom hand-coded websites for high-traffic university departments.</li> "\
            "<li>Iterated with stakeholders to refine graphic and user interface designs.</li> "\
            "<li>Led website management training sessions with university staff.</li>"\
            "<li>Produced valid XHTML to meet W3C Web Content Accessibility Guidelines (WCAG) and Section 508 compliance.</li> "\
          "</ul>")
]

programs = [
    Program(name="Advanced Software Development", school_id="1", 
            url="https://www.codefellows.org/courses/code-401/advanced-software-development-in-full-stack-javascript/", 
            start_date="Aug 2017", end_date="Nov 2017"),
    Program(name="IT Foundations", type="Certificate", school_id="2", 
            url="https://www.pce.uw.edu/certificates/it-foundations", 
            start_date="Jun 2017", end_date="Dec 2017"),
    Program(name="Python Programming", school_id="2",
            url="https://www.pce.uw.edu/certificates/python-programming",
            start_date="Jan 2018", is_current="true"),
    Program(name="English", type="BA", school_id="3", 
            url="https://english.uiowa.edu/", 
            start_date="2005", end_date="2008")
]

courses = [
    Course(name="Code 301: Intermediate Software Development", program_id="1", 
           url="https://www.codefellows.org/courses/code-301/intermediate-software-development/"),
    Course(name="Code 401: Advanced Software Development in Full-Stack JavaScript", program_id="1", 
           url="https://www.codefellows.org/courses/code-401/advanced-software-development-in-full-stack-javascript/"),
    Course(name="Algorithms & Data Structures", program_id="2", 
           url="https://www.pce.uw.edu/courses/foundations-of-algorithms-and-data-structures"),
    Course(name="Programming Foundations (Python)", program_id="2", 
           url="https://www.pce.uw.edu/courses/foundations-of-programming-python"),
    Course(name="Database Management", program_id="2", 
           url="https://www.pce.uw.edu/courses/foundations-of-database-management"),
    Course(name="Programming in Python", program_id="3", 
           url="https://www.pce.uw.edu/courses/programming-in-python"),
    Course(name="Advanced Programming in Python", program_id="3", 
           url="https://www.pce.uw.edu/courses/advanced-programming-in-python"),
    Course(name="Internet Programming with Python", program_id="3", 
           url="https://www.pce.uw.edu/courses/internet-programming-with-python")
]

projects = [
    Project(name="Mandarin Oriental", url="https://www.mandarinoriental.com/"),
    Project(name="Chanalai Hotels & Resorts", url="https://www.chanalai.com/en"),
    Project(name="Elegant Hotels", url="https://www.eleganthotels.com/"),
    Project(name="Hotel Metropole", url="https://www.metropolehotel.com/"),
    Project(name="Ojai Valley Inn & Spa", url="https://www.ojairesort.com/"),
    Project(name="Palau Pacific Resort", url="http://www.palauppr.com/"),
    Project(name="Prince Resorts Hawaii", url="http://www.princeresortshawaii.com/"),
    Project(name="Wyndham Grand Pittsburgh Downtown", url="http://www.wyndhamgrandpittsburgh.com/")
]

awards = [
    Award(name="Best in Class, 2017",  institution_id="1"),
    Award(name="Outstanding Achievement, 2017",  institution_id="1"),
    Award(name="Best in Class, 2016",  institution_id="1"),
    Award(name="Outstanding Website, 2017",  institution_id="2"),
    Award(name="Hotel and Lodging Standard of Excellence, 2017",  institution_id="2"),
    Award(name="Outstanding Website, 2016",  institution_id="2"),
]

entries= [
    Entry(name="Ojai Valley Inn & Spa", 
          url="http://interactivemediaawards.com/winners/certificate.asp?param=764449&cat=1"),
    Entry(name="Palau Pacific Resort", 
          url="http://interactivemediaawards.com/winners/certificate.asp?param=764435&cat=1"),
    Entry(name="Prince Resorts Hawaii", 
          url="http://interactivemediaawards.com/winners/certificate.asp?param=764456&cat=1"),
    Entry(name="Elegant Hotels", 
          url="http://interactivemediaawards.com/winners/certificate.asp?param=764687&cat=1"),
    Entry(name="Hotel Metropole", 
          url="http://interactivemediaawards.com/winners/certificate.asp?param=764764&cat=1"),
    Entry(name="Wyndham Grand Pittsburgh Downtown", 
          url="http://interactivemediaawards.com/winners/certificate.asp?param=764603&cat=1"),
    Entry(name="Chanalai Hotels and Resorts", 
          url="http://interactivemediaawards.com/winners/certificate.asp?param=606235&cat=1"),
    Entry(name="Palau Pacific Resort", 
          url="http://www.webaward.org/winner/33385/sabre-hospitality-solutions-wins-2017-webaward-for-prince-resorts-hawaii.html"),
    Entry(name="Elegant Hotels", 
          url="http://www.webaward.org/winner/33384/sabre-hospitality-solutions-wins-2017-webaward-for-elegant-hotels.html"),
    Entry(name="Palau Pacific Resort", 
          url="http://www.webaward.org/winner/32731/sabre-hospitality-solutions-wins-2016-webaward-for-palau-pacific-resort.html"),
    Entry(name="Chanalai Hotels and Resorts", 
          url="http://www.webaward.org/winner/32730/sabre-hospitality-solutions-wins-2016-webaward-for-chanalai-hotels-and-resorts.html")
]

stuart.skills = skills
stuart.companies = companies
stuart.schools = schools
stuart.institutions = institutions
stuart.projects = projects

session.add(stuart)

session.commit()

session.bulk_save_objects(positions)
session.bulk_save_objects(programs)
session.bulk_save_objects(courses)

awards[0].entries = [entries[0], entries[1], entries[2], entries[3]]
awards[1].entries = [entries[4], entries[5]]
awards[2].entries = [entries[6]]
awards[3].entries = [entries[7]]
awards[4].entries = [entries[8]]
awards[5].entries = [entries[9], entries[10]]

session.add(awards[0])
session.add(awards[1])
session.add(awards[2])
session.add(awards[3])
session.add(awards[4])
session.add(awards[5])

session.commit()

'''
