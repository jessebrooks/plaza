# Create a new AWS API

Guide to create a new AWS API built on:

* AWS RDS PostgreSQL
* AWS Lambda (Python 3.6 + Psycopg2)
* AWS API Gateway instance

## Create an AWS RDS PostgreSQL Database

### Create an AWS account

### Create an AWS Administrator account and log into it

### Create AWS RDS PostgreSQL Database

1. Log into AWS console
2. Select RDS console
3. Select Create Database
4. Select engine: PostgreSQL
5. Click Next
6. Specify DB details:
    1. License Model: postgresql-license
    2. DB engine version: PostgreSQL 9.6.6-R1
    3. DB instance class: db.t2.micro - 1 vCPU, 1 GiB RAM
    4. Allocated storage: 20 GiB
    5. DB instance identifier: test
    6. Master username: test
    7. Master password: test123
7. Click Next
8. Configure advanced settings:
    1. Virtual Private Cloud (VPC): Default VPC (vpc-********)
    2. Subnet group: default
    3. Public accessibility: Yes
    4. Availability zone: No preference
    5. VPC security groups: Create new VPC security group
    6. Database name: test
    7. Port: 5432
    8. DB parameter group: default.postgres9.6
    9. Option group: default: postgres-9-6 (should not be selectable)
    10. Encryption should not be selectable
    11. Backup retention period: 7 days
    12. Backup window: No preference and copy tags to snapshots
    13. Enhanced monitoring: Disable enhanced monitoring
    14. Auto minor version upgrade: Enable auto minor version upgrade
    15. Maintenance window: No preference
9. Click Create database
10. Click View DB instance details

### Configure security settings to allow Lambda to access the database

1. In the View DB instance details page, click the link under security groups
2. Select the Inbound tab
3. Select Edit
4. Select Add Rule
5. Configure with these settings:
    1. Type: PostgreSQL
    2. Protocol: TCP
    3. Port Range: 5432
    4. Source: Anywhere

## Connect to the Database and Configure the Table

### Connect to RDS PostgreSQL instance via PostgreSQL

1. `psql -h test.************.us-west-2.rds.amazonaws.com ip 5432 -n test -u test`
2. Enter password when prompted

### Create test table and insert a test row

1. `CREATE TABLE people(id_num SERIAL PRIMARY KEY, first_name VARCHAR NOT NULL, last_name VARCHAR NOT NULL);`
2. `INSERT INTO people(id_num, first_name, last_name) VALUES (DEFAULT, 'Jesse', 'Brooks');`
3. `SELECT * FROM people`




## Prepare Development Environment

### Update Homebrew and install PostgreSQL

`brew update`
`brew install postgresql`

Reference: https://formulae.brew.sh/formula/postgresql

### Update pip and install Psycopg2

`pip install -U pip`
`pip install psycopg2`

Reference: https://wiki.postgresql.org/wiki/Psycopg2
Reference: https://github.com/psycopg/psycopg2

### Create working directory for Lambda function

`cd path/to/directory`
`mkdir directory`
`cd directory`

### Clone awslambda-psycopg2 into working directory of Lambda function

`git clone https://github.com/jkehler/awslambda-psycopg2.git`

### Copy the desired version of Psycopg2 into working directory 
### Note: using Python 3.6 version here, so should rename Python 3.6 version folder to psycopg2

`cd awslambda-psycopg2`
`cp -r ./psycopg2-3.6 ../psycopg2`

### Remove unneeded files

`rm -r awslambda-psycopg2`




## Deploy the Lambda

### Write the Lambda Function and ZIP it up

1. `vim test.py`
2. Paste in the following code:
    ```python
    import psycopg2

    def get_person():
        result = []
        conn = psycopg2.connect("dbname='plaza' user='caesar' host='plaza.c2wsmdjwnmys.us-west-2.rds.amazonaws.com' password='Coco4658210.'")
        cur = conn.cursor()
        cur.execute("""SELECT * FROM people""")
        for row in cur:
            result.append(list(row))
        print("Data Returned:")
        print(result)
        return(result)

    def main (event, context):
        return get_person()
    ```
3. ESC
4. `:wq`
5. ``zip -r -X test.zip `ls` ``

### Create the Lambda on AWS

1. Log into AWS console
2. Select Lambda console
3. Select Create function
4. Use settings:
    1. Name: test
    2. Runtime: Python 3.6
    3. Role: Create a new role from template(s)
    4. Role name: basic-lambda
    5. Policy templates: Basic Lambda@Edge permissions (for CloudFront trigger)
5. Select Create function

### Configure Lambda

1. Under Function code, use these settings:
    1. Code entry type: upload a .ZIP file
    2. Runtime: Python 3.6
    3. Handler: test.main
    4. Function package: select and upload the ZIP you created earlier
2. Select Save
3. Select Test at the top of the page
4. Create a new test event:
    1. Event template: Hello World
    2. Event name: test
    3. Value: {}
5. Select Create
6. Select Save
7. Select Test
8. The function should return "[[1, "Jesse", "Brooks"]]

## Configure API

### Create new API

1. Log into AWS console
2. Select API Gateway console
3. Select Create API
4. Use settings:
    1. API name: test
    2. Description: test
    3. Endpoint Type: Regional
5. Select Create API

### Create API method

1. Select Actions
2. Select Create Method
3. Select Get
4. Select the checkbox
5. Use settings:
    1. Integration type: Lambda Function
    2. Use Lambda Proxy integration: unchecked
    3. Lambda Region: Same as the Lambda function (us-west-2 for me)
    4. Lambda Function: test
    5. Use Default Timeout: checked
6. Select Save
7. Select OK
8. Select Actions
9. Select Deploy API
10. Use settings:
    1. Deployment stage: [New Stage]
    2. Stage name: test
    3. Stage description: none
    4. Deployment description: none
11. Select Deploy
12. Click the Invoke URL link at the top of the page
13. Should return: "[[1, "Jesse", "Brooks"]]

You're done!
