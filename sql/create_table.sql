create table schools (
    school_id int(10) primary key,
    school_title varchar(100),
    is_active tinyint(4),
    created_at datetime,
    update_at datetime
);

create table students (
    student_id int(10) primary key,
    course_id int(10),
    student_name varchar(50),
    gender varchar(50),
    created_at datetime,
    update_at datetime
);

create table courses (
    course_id int(10),
    courses_title varchar(10),
    created_at datetime,
    update_at datetime
);