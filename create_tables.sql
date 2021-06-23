
CREATE TABLE staging_events (
    artist varchar,
    auth varchar,
    first_name varchar,
    gender char(1),
    item_in_session int,
    last_name varchar,
    length numeric,
    level varchar,
    location varchar,
    method varchar,
    page varchar,
    registration numeric,
    session_id int,
    song varchar,
    status int,
    ts bigint,
    user_agent varchar,
    user_id int
)

CREATE TABLE staging_songs (
    num_songs int,
    artist_id varchar,
    artist_latitude varchar,
    artist_longitude varchar,
    artist_location varchar,
    artist_name varchar,
    song_id varchar,
    title varchar,
    duration numeric,
    year int
)

CREATE TABLE songplays (
    songplay_id INT IDENTITY(0,1) PRIMARY KEY,
    start_time TIMESTAMP WITHOUT TIME ZONE NOT NULL
        REFERENCES time(start_time),
    user_id int NOT NULL
        REFERENCES users(user_id),
    level varchar,
    song_id varchar
        REFERENCES songs(song_id),
    artist_id varchar
            REFERENCES artists(artist_id),
    session_id int,
    location varchar,
    user_agent varchar)

CREATE TABLE users (
    user_id int PRIMARY KEY,
    first_name varchar,
    last_name varchar,
    gender char(1),
    level varchar
)

CREATE TABLE songs (
    song_id varchar PRIMARY KEY,
    title varchar,
    artist_id varchar REFERENCES artists(artist_id),
    year int,
    duration numeric
)

CREATE TABLE artists (
    artist_id varchar PRIMARY KEY,
    name varchar,
    location varchar,
    latitude numeric,
    longitude numeric
)

CREATE TABLE time (
    start_time TIMESTAMP WITHOUT TIME ZONE PRIMARY KEY,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday int
)
