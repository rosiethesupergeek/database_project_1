_Copy this recipe template to design and create a database table from a specification._

## 1. Extract nouns from the user stories or specification

```
As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' titles.

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' genres.

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' release years.


```

```
Nouns:

title, genre, release_year
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| movies                | title, genre, release_year |

Name of the table (always plural): `movies`

Column names: `title`, `genre`, 'release_year'

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

id: SERIAL
title: text
genre: text
release_year: int
```

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

-- file student_directory_1.sql

CREATE TABLE movies (
  id SERIAL PRIMARY KEY,
  title text,
 genre text,
 release_year text
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```
```
psql -h 127.0.0.1 database_name < movies_table.sql
```

note: do you need to be in the directory which contains the seed sql files in order to create the database and seed it?

go into psql

CREATE DATABASE movies_directory;

get out of psql \q

Then, go back into sql and connect the database with the sql file that you want to seed from:
psql -h 127.0.0.1 movies_directory < movies_directo
ry.sql

OR:

createdb movies 
psql -h 127.0.0.1 movies < movies_directory.sql # More useful when inserting items into database me tinks
psql -h 127.0.0.1 movies