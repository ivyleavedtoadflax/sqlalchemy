drop table if exists mtcars;

create table mtcars(
car varchar(30),
mpg real,
wt real
);

\copy mtcars from 'mtcars.csv' delimiter ',' csv;

