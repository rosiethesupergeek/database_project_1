DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS students_id_seq;
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    cohort VARCHAR(255)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO students (name, cohort) VALUES ('Rosie', 'Ness');
INSERT INTO students (name, cohort) VALUES ('Matthew', 'Ore');
INSERT INTO students (name, cohort) VALUES ('Aisha', 'Ness');
INSERT INTO students (name, cohort) VALUES ('James', 'Lomond');
