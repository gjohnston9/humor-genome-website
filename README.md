### Humor Genome website

Getting started:
- Install PostgreSQL: `sudo apt-get install postgresql libpq-dev postgresql-client postgresql-client-common`
- Switch to the `postgres` superuser: `sudo -i -u postgres`
	- Set your password: `psql`, `\password postgres`, then `\q` to quit
	- Create a new `hgp` Postgres user: `createuser -P hgp` and enter the password when prompted, 
	- Create a Humor Genome database with `hgp` as the owner: `psql`, `CREATE DATABASE hgp OWNER hgp`
	- Exit from the `postgres` account: `exit`
- Export the password you chose for your `hgp` user as `POSTGRES_HGP_PASSWORD`
- Set up the database tables that Django needs with `python manage.py migrate`