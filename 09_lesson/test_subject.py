from sqlalchemy import create_engine, inspect, text


db_connection_string = "postgresql://postgres:2106@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[1] == 'subject'


def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO subject(subject_id, subject_title) VALUES (:new_id, :new_subject_title)")
    connection.execute(sql, {"new_id": 16, "new_subject_title": "Ecology"})

    sql_statement = text("SELECT * FROM subject WHERE subject_id = :new_id")
    result = connection.execute(sql_statement, {"new_id": 16})
    rows = result.mappings().all()
    assert len(rows) == 1
    assert rows[0]["subject_title"] == "Ecology"

    sql = text("DELETE FROM subject WHERE subject_id = :new_id")
    connection.execute(sql, {"new_id": 16})

    transaction.commit()
    connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO subject(subject_id, subject_title) VALUES (:new_id, :new_subject_title)")
    connection.execute(sql, {"new_id": 16, "new_subject_title": "Ecology"})

    sql = text("UPDATE subject SET subject_title = :sub_tit WHERE subject_id = :id")
    connection.execute(sql, {"sub_tit": 'New ecology', "id": 16})

    sql_statement = text("SELECT * FROM subject WHERE subject_id = :id")
    result = connection.execute(sql_statement, {"id": 16})
    rows = result.mappings().all()
    assert len(rows) == 1
    assert rows[0]["subject_title"] == "New ecology"

    sql = text("DELETE FROM subject WHERE subject_id = :id")
    connection.execute(sql, {"id": 16})

    transaction.commit()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    initial_count = connection.execute(
        text("SELECT COUNT(*) FROM subject")).scalar()

    sql = text("INSERT INTO subject(subject_id, subject_title) VALUES (:new_id, :new_subject_title)")
    connection.execute(sql, {"new_id": 16, "new_subject_title": "Ecology"})

    sql = text("DELETE FROM subject WHERE subject_id = :id")
    connection.execute(sql, {"id": 16})

    final_count = (connection.execute
                   (text("SELECT COUNT(*) FROM subject")).scalar())
    assert initial_count == final_count

    transaction.commit()
    connection.close()
