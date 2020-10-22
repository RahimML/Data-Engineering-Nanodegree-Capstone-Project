CREATE TABLE public.flights (
	airline varchar(256) NOT NULL,
	FLIGHT_NUMBER int4,
	ORIGIN_AIRPORT varchar(256),
	DESTINATION_AIRPORT varchar(256),
	month int4,
	day int4,
	DAY_OF_WEEK int4,
	SCHEDULED_DEPARTURE int4,
	DEPARTURE_DELAY int4,
	CANCELLED int4,
	CANCELLATION_REASON varchar(256)

);

CREATE TABLE public.airlines (
	IATA_CODE varchar(256) NOT NULL,
	airline varchar(256),
	number_of_flights int4,
	CONSTRAINT IATA1_pkey PRIMARY KEY (IATA_CODE)
);

CREATE TABLE public.airports (
	IATA_CODE varchar(256) NOT NULL,
	AIRPORT varchar(256),
	CITY varchar(256),
	depatured_flights int4,
	arrived_flights int4,
	CONSTRAINT IATA2_pkey PRIMARY KEY (IATA_CODE)
);

CREATE TABLE public.cities (
	CITY varchar(256),
	state_code varchar(256),
	median_age numeric(18,0),
	total_population int4,
	CONSTRAINT city_fkey FORIEGN KEY (CITY) REFERENCES AIRPORTS(CITY)
);





