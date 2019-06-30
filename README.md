# jwt_drf_app
JSON Web Token Django Rest Framework test application

## Application demo instructions

1. Application "bot" is intended for use with PostgreSQL. Install PostgreSQL `sudo apt install postgresql libpq-dev`.
1. Clone the project `git clone https://github.com/barfvarf/jwt_drf_app.git`
1. Install application virtualenv/libraries which are specified in requirements.txt `pip install -r requirements.txt`.
1. Give +x permission to init_db_and_server.sh and run_tests.sh `chmod +x init_db_and_server.sh`, `chmod +x run_tests.sh`. Also correct PGPASSWORD has to be specified in init_db_and_server.sh.
1. Run `./init_db_and_server.sh` in application virtualenv.
1. Run `./run_tests.sh` in separate application virtualenv.

**Note:**
* Test which simulates user activity does not destroy database/table so they could be examined later. In order to repeat the test re-launch both init_db_and_server.sh and run_tests.sh again.
