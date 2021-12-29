begin;

create type patient_status as enum (
	'occupied',
	'free'
);

create table if not exists patient (
	patient_id serial primary key,
	status patient_status not null default 'free'
);

commit;