import psycopg2

def main():
    try:
        conn = psycopg2.connect("dbname='plaza' user='caesar' host= 'plaza.c2wsmdjwnmys.us-west-2.rds.amazonaws.com' password='Coco4658210.'")
        cur = conn.cursor()
        cur.execute("""
            DROP TABLE IF EXISTS people, vehicles, lessors, policies, bids;

            CREATE TABLE "people" (
                "person_num" int   NOT NULL,
                "first_name" varchar   NOT NULL,
                "last_name" varchar   NOT NULL,
                "address1_addr" varchar   NOT NULL,
                "address2_addr" varchar   NOT NULL,
                "city_addr" varchar   NOT NULL,
                "state_addr" varchar   NOT NULL,
                "zip_addr" varchar   NOT NULL,
                "email_addr" varchar   NOT NULL,
                "phone_num" varchar   NOT NULL,
                "age_num" int   NOT NULL,
                "gender_name" varchar   NOT NULL,
                "marital_status" bool   NOT NULL,
                "driver_license_num" int   NOT NULL,
                "driver_license_state_name" varchar   NOT NULL,
                "driver_license_start_date" date   NOT NULL,
                "driver_license_expire_date" date   NOT NULL,
                "at_fault_claim_status" bool   NOT NULL,
                "at_fault_claim_date" date   NOT NULL,
                CONSTRAINT "pk_people" PRIMARY KEY (
                    "person_num"
                )
            );

            CREATE TABLE "vehicles" (
                "vehicle_num" int   NOT NULL,
                "owner_num" int   NOT NULL,
                "lessor_num" int   NOT NULL,
                "policy_num" int   NOT NULL,
                "ownership_status" varchar   NOT NULL,
                "make_name" varchar   NOT NULL,
                "model_name" varchar   NOT NULL,
                "year_date" int   NOT NULL,
                "vin_num" varchar   NOT NULL,
                "miles_per_year_num" int   NOT NULL,
                CONSTRAINT "pk_vehicles" PRIMARY KEY (
                    "vehicle_num"
                )
            );

            CREATE TABLE "lessors" (
                "lessor_num" int   NOT NULL,
                "lessor_name" varchar   NOT NULL,
                CONSTRAINT "pk_lessors" PRIMARY KEY (
                    "lessor_num"
                )
            );

            CREATE TABLE "policies" (
                "policy_num" int   NOT NULL,
                "insured_driver_num" int   NOT NULL,
                "insured_vehicle_num" int   NOT NULL,
                "policy_name" varchar   NOT NULL,
                "premium_num" money   NOT NULL,
                "coverage_amount_num" int   NOT NULL,
                "coverage_start_date" date   NOT NULL,
                "coverage_end_date" date   NOT NULL,
                CONSTRAINT "pk_policies" PRIMARY KEY (
                    "policy_num"
                )
            );

            CREATE TABLE "bids" (
                "bid_num" int   NOT NULL,
                "person_num" int   NOT NULL,
                "vehicle_num" int   NOT NULL,
                "old_policy_num" int   NOT NULL,
                "premium_num" money   NOT NULL,
                "coverage_amount_num" int   NOT NULL,
                "coverage_start_date" date   NOT NULL,
                "coverage_end_date" date   NOT NULL,
                CONSTRAINT "pk_bids" PRIMARY KEY (
                    "bid_num"
                )
            );

            ALTER TABLE "vehicles" ADD CONSTRAINT "fk_vehicles_owner_num" FOREIGN KEY("owner_num")
            REFERENCES "people" ("person_num");

            ALTER TABLE "vehicles" ADD CONSTRAINT "fk_vehicles_lessor_num" FOREIGN KEY("lessor_num")
            REFERENCES "lessors" ("lessor_num");

            ALTER TABLE "vehicles" ADD CONSTRAINT "fk_vehicles_policy_num" FOREIGN KEY("policy_num")
            REFERENCES "policies" ("policy_num");

            ALTER TABLE "policies" ADD CONSTRAINT "fk_policies_insured_driver_num" FOREIGN KEY("insured_driver_num")
            REFERENCES "people" ("person_num");

            ALTER TABLE "policies" ADD CONSTRAINT "fk_policies_insured_vehicle_num" FOREIGN KEY("insured_vehicle_num")
            REFERENCES "vehicles" ("vehicle_num");

            ALTER TABLE "bids" ADD CONSTRAINT "fk_bids_person_num" FOREIGN KEY("person_num")
            REFERENCES "people" ("person_num");

            ALTER TABLE "bids" ADD CONSTRAINT "fk_bids_vehicle_num" FOREIGN KEY("vehicle_num")
            REFERENCES "vehicles" ("vehicle_num");

            ALTER TABLE "bids" ADD CONSTRAINT "fk_bids_old_policy_num" FOREIGN KEY("old_policy_num")
            REFERENCES "policies" ("policy_num");
        """)
        conn.commit()
        return("Success")
    except:
        return("Fail")

main()