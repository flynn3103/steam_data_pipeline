import Faker

fake = Faker()
# DROP TABLES
school_table_drop = "drop table if exits schools"
student_table_drop = "drop table if exits students"
course_table_drop = "drop table if exits courses"

# CREATE TABLES

school_table_create = ("""create table if not exits schools (
    school_id int(10) serial constraint school_pk primary key,
    school_title varchar(100),
    is_active tinyint(4),
    created_at datetime,
    update_at datetime
)""")

student_table_create = ("""create table students (
    student_id int(10) primary key,
    course_id int(10) references courses(course_id),
    school_id int(10) references schools(school_id)
    student_name varchar(50),
    gender varchar(50),
    created_at datetime,
    update_at datetime
)""")

course_table_create = ("""create table courses (
    course_id int(10) primary key,
    courses_title varchar(10),
    created_at datetime,
    update_at datetime
)""")

# Insert data


# Query list
create_table_queries = [school_table_create,student_table_create,course_table_create]
drop_table_queries = [school_table_drop,student_table_drop,course_table_drop]