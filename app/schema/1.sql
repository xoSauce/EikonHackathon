DROP TABLE IF EXISTS `countries`;
CREATE TABLE countries(
    id  int primary key,
    name varchar(255),
    crime_index double,
    pollution_index double,
    natural_disaster_txt TEXT,
    natural_disaster_index double,
    gdp double,
    import double,
    export double,
    debt double,
    overall_index double
);


