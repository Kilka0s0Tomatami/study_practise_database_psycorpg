import psycopg2

class Connection:
    # Статическая переменная
    connection = None

    @staticmethod
    def get_connection():
        if Connection.connection == None:
            Connection.connection = psycopg2.connect(  # Открытие соединения к базе данных
                database="postgres",
                user="postgres",
                password="1111",
                host="127.0.0.1",
                port="5432"
            )
        return Connection.connection

    @staticmethod
    def close_connection():
        if Connection.connection != None:
            Connection.connection.close()


def subject_exists(subject_name):
    # Открытие курсора
    connection = Connection.get_connection()
    cur = connection.cursor()  # Открытие курсора

    cur.execute(
        f"select count(*) from subjects s where subj_name = '{subject_name}'"
    )

    if cur.fetchone()[0] > 0:
        cur.close()  # Закрытие курсора
        return True
    else:
        cur.close()  # Закрытие курсора
        return False


def subject_get_id(subject_name):
    connection = Connection.get_connection()
    cur = connection.cursor()  # Открытие курсора

    cur.execute(
        f"select subj_id from subjects s where subj_name = '{subject_name}'"
    )

    subject_id = cur.fetchone()

    cur.close()  # Закрытие курсора
    print(subject_id)
    if subject_id:
        return subject_id[0]
    else:
        return 0


def subject_create(subject_name):
    if not subject_exists(subject_name):
        # Открытие курсора
        connection = Connection.get_connection()
        cur = connection.cursor()  # Открытие курсора

        cur.execute(
            f"insert into subjects (subj_id, subj_name) values (nextval('subj_id_seq'), '{subject_name}')"
        )

        cur.close()  # Закрытие курсора

        connection.commit()  # Закрытие транкзации

        print(f"Предмет {subject_name} успешно собран")
    else:
        print(f"Предмет {subject_name} уже существует")


def subject_delete(subject_name):
    if subject_exists(subject_name):
        if not grade_subject_exists(subject_name):
            # Открытие курсора
            connection = Connection.get_connection()
            cur = connection.cursor()  # Открытие курсора

            cur.execute(
                f"delete from subjects where subj_name = '{subject_name}'"
            )

            cur.close()  # Закрытие курсора

            connection.commit()  # Закрытие транкзации
            print(f"Предмет {subject_name} успешно удален")
            return f"Предмет {subject_name} успешно удален"
        else:
            print(f"По предмету {subject_name} проставлены оценки")
            return "Необходимо удалить оценки по предмету"
    else:
        print(f"Предмета {subject_name} не существует")
        return False


def subject_rename(subject_name, new_subject_name):
    if subject_exists(subject_name):
        if not subject_exists(new_subject_name):
            # Открытие курсора
            connection = Connection.get_connection()
            cur = connection.cursor()  # Открытие курсора

            cur.execute(
                f"update subjects set subj_name = '{new_subject_name}' where subj_name = '{subject_name}'"
            )

            cur.close()  # Закрытие курсора

            connection.commit()  # Закрытие транкзации

            print(f"Название предмета {subject_name} изменено на {new_subject_name}")
            return f"Название предмета {subject_name} изменено на {new_subject_name}"
        else:
            print(f"Предмет с названием {new_subject_name} уже существует")
            return f"Предмет с названием {new_subject_name} уже существует"
    else:
        print(f"Предмета с названием {subject_name} не существует")
        return f"Предмета с названием {subject_name} не существует"


def subjects_get_list():
    subjects = []

    # Открытие курсора
    connection = Connection.get_connection()
    cur = connection.cursor()  # Открытие курсора

    cur.execute(
        f"select subj_name from subjects"
    )

    for line in cur.fetchall():
        subjects.append(line[0])

    cur.close()  # Закрытие курсора

    return subjects


def subject_get_list_by_student(stud_id):
    subjects = []

    # Открытие курсора
    connection = Connection.get_connection()
    cur = connection.cursor()  # Открытие курсора

    cur.execute(
        f"select subj_name from grades g, subjects s  where stud_id = '{stud_id}' "
        f"and s.subj_id = g.subj_id  group by s.subj_name"
    )

    for line in cur.fetchall():
        subjects.append(line[0])

    cur.close()  # Закрытие курсора

    return subjects


def student_group_exists(group_name):
    # Открытие курсора
    connection = Connection.get_connection()
    cur = connection.cursor()  # Открытие курсора

    group_id = group_get_id(group_name)

    cur.execute(
        f"select count(*) from students s where group_id = '{group_id}'"
    )

    if cur.fetchone()[0] > 0:
        cur.close()  # Закрытие курсора
        return True
    else:
        cur.close()  # Закрытие курсора
        return False


def student_id_exists(student_id):
    # Открытие курсора
    connection = Connection.get_connection()
    cur = connection.cursor()  # Открытие курсора

    cur.execute(
        f"select count(*) from students s where stud_id = '{student_id}'"
    )

    if cur.fetchone()[0] > 0:
        cur.close()  # Закрытие курсора
        return True
    else:
        cur.close()  # Закрытие курсора
        return False


def student_get_last_id():
    # Открытие курсора
    connection = Connection.get_connection()
    cur = connection.cursor()  # Открытие курсора

    cur.execute(
        f"select last_value from stud_id_seq;"
    )

    student_id = cur.fetchone()[0]

    cur.close()  # Закрытие курсора

    print(student_id)

    return student_id


def student_get_info(student_id):
    if student_id_exists(student_id):
        connection = Connection.get_connection()
        cur = connection.cursor()  # Открытие курсора

        cur.execute(
            f"select * from students s where stud_id = '{student_id}'"
        )

        info = cur.fetchone()

        student_name = info[1]
        group_name = group_get_name(info[2])

        cur.close()  # Закрытие курсора

        print(f"Студбилет {student_id}, студент {student_name} состоит в группе {group_name}")

        return student_name, group_name
    else:
        print(f"Студента с ID {student_id} не существует")


def student_create(student_name, group_name):
    if group_name_exists(group_name):
        # Открытие курсора
        connection = Connection.get_connection()
        cur = connection.cursor()  # Открытие курсора

        group_id = group_get_id(group_name)

        cur.execute(
            f"insert into students (stud_id, name, group_id) values (nextval('stud_id_seq'), '{student_name}', "
            f"'{group_id}')"
        )

        cur.close()  # Закрытие курсора

        connection.commit()  # Закрытие транкзации

        student_id = student_get_last_id()

        print(f"Студент {student_name} добавлен в группу {group_name}")
        print(f"ID студента: {student_id}")
        return f"Студент: {student_name}\nГруппа: {group_name}\nID-номер студента: {student_id}"
    else:
        print(f"Группы {group_name} не существует")
        return f"Группы {group_name} не существует"


def student_delete(student_id):
    if student_id_exists(student_id):

        student_name = student_get_info(student_id)[0]
        group_name = student_get_info(student_id)[1]

        if not grade_student_exists(student_id):

            # Открытие курсора
            connection = Connection.get_connection()
            cur = connection.cursor()  # Открытие курсора

            cur.execute(
                f"delete from students where stud_id = '{student_id}'"
            )

            cur.close()  # Закрытие курсора

            connection.commit()  # Закрытие транкзации
            print(f"Студент {student_name}, студбилет {student_id} из группы {group_name} отчислен")
            return f"Студент {student_name}, студбилет {student_id} из группы {group_name} отчислен"
        else:
            print(f"По студенту {student_name} проставлены оценки")
            return f"По студенту {student_name} проставлены оценки"
    else:
        print(f"Студента с ID {student_id} не существует")
        return f"Студента с ID {student_id} не существует"


def student_rename(student_id, new_student_name):
    if student_id_exists(student_id):
        # Открытие курсора
        connection = Connection.get_connection()
        cur = connection.cursor()  # Открытие курсора

        cur.execute(
            f"update students set name = '{new_student_name}' where stud_id = '{student_id}'"
        )

        cur.close()  # Закрытие курсора

        connection.commit()  # Закрытие транкзации

        group_name = student_get_info(student_id)[1]

        print(f"Информация о студенте {new_student_name}, ID {student_id}, группа {group_name} обновлена")
        return f"Информация о студенте {new_student_name}, ID {student_id}, группа {group_name} обновлена"
    else:
        print(f"Студента с ID {student_id} не существует")
        return f"Студента с ID {student_id} не существует"


def student_group_change(student_id, new_group_name):
    if group_name_exists(new_group_name):
        if student_id_exists(student_id):
            new_group_id = group_get_id(new_group_name)

            student_name = student_get_info(student_id)[0]

            group_name = student_get_info(student_id)[1]

            # Открытие курсора
            connection = Connection.get_connection()
            cur = connection.cursor()  # Открытие курсора

            cur.execute(
                f"update students set group_id = '{new_group_id}' where stud_id = '{student_id}'"
            )

            cur.close()  # Закрытие курсора

            connection.commit()  # Закрытие транкзации
            print(f"Студент {student_name}, студбилет {student_id}, переведен из группы {group_name} в группу "
                  f"{new_group_name}")
            return f"Студент {student_name}, студбилет {student_id}, переведен из группы {group_name} " \
                   f"в группу {new_group_name}"
        else:
            print(f"Студента с ID {student_id} не существует")
            return f"Студента с ID {student_id} не существует"

    else:
        print(f"Группы {new_group_name} не существует")
        return f"Группы {new_group_name} не существует"


def group_name_exists(group_name):
    # Открытие курсора
    connection = Connection.get_connection()
    cur = connection.cursor()  # Открытие курсора

    cur.execute(
        f"select count(*) from groups g where group_name = '{group_name}'"
    )

    if cur.fetchone()[0] > 0:
        cur.close()  # Закрытие курсора
        return True
    else:
        cur.close()  # Закрытие курсора
        return False


def group_id_exists(group_id):
    # Открытие курсора
    connection = Connection.get_connection()
    cur = connection.cursor()  # Открытие курсора

    cur.execute(
        f"select count(*) from groups g where group_id = '{group_id}'"
    )

    if cur.fetchone()[0] > 0:
        cur.close()  # Закрытие курсора
        return True
    else:
        cur.close()  # Закрытие курсора
        return False


def group_get_id(group_name):
    connection = Connection.get_connection()
    cur = connection.cursor()  # Открытие курсора

    cur.execute(
        f"select group_id from groups g where group_name = '{group_name}'"
    )
    group_id = cur.fetchone()

    cur.close()  # Закрытие курсора
    print(group_id)
    if group_id:
        return group_id[0]
    else:
        return 0


def group_get_name(group_id):
    connection = Connection.get_connection()
    cur = connection.cursor()  # Открытие курсора

    cur.execute(
        f"select group_name from groups g where group_id = '{group_id}'"
    )
    group_name = cur.fetchone()

    cur.close()  # Закрытие курсора
    print(group_name[0])
    if group_name:
        return group_name[0]
    else:
        return 0


def group_create(group_name):
    if not group_name_exists(group_name):
        # Открытие курсора
        connection = Connection.get_connection()
        cur = connection.cursor()  # Открытие курсора

        cur.execute(
            f"insert into groups (group_id, group_name) values (nextval('group_id_seq'), '{group_name}')"
        )

        cur.close()  # Закрытие курсора

        connection.commit()  # Закрытие транкзации

        print(f"Группа {group_name} успешно объявлена")
    else:
        print(f"Группа {group_name} уже существует")


def group_delete(group_name):
    if group_name_exists(group_name):
        if not student_group_exists(group_name):
            # Открытие курсора
            connection = Connection.get_connection()
            cur = connection.cursor()  # Открытие курсора

            cur.execute(
                f"delete from groups where group_name = '{group_name}'"
            )

            cur.close()  # Закрытие курсора

            connection.commit()  # Закрытие транкзации
            print(f"Группа {group_name} успешно расформирована")
            return f"Группа {group_name} успешно расформирована"
        else:
            print(f"Группу {group_name} невозможно расформировать - в ней числятся студенты")
            return f"Группу {group_name} невозможно расформировать - в ней числятся студенты"
    else:
        print(f"Группы {group_name} не существует")


def group_delete_students(group_name):
    print("")


def group_get_students_list(group_name):
    if group_name_exists(group_name):
        group_id = group_get_id(group_name)

        Students = []

        # Открытие курсора
        connection = Connection.get_connection()
        cur = connection.cursor()  # Открытие курсора

        cur.execute(
            f"select stud_id, name from students where group_id = '{group_id}'"
        )

        for table in cur.fetchall():
            Students.append(table)

        cur.close()  # Закрытие курсора

        return Students
    else:
        print(f"Группы {group_name} не существует")
        return []


def group_get_students_id(group_name):
    if group_name_exists(group_name):
        group_id = group_get_id(group_name)

        IDs = []

        # Открытие курсора
        connection = Connection.get_connection()
        cur = connection.cursor()  # Открытие курсора

        cur.execute(
            f"select * from students where group_id = '{group_id}'"
        )

        for table in cur.fetchall():
            IDs.append(table[0])

        cur.close()  # Закрытие курсора

        return IDs
    else:
        print(f"Группы {group_name} не существует")


def group_special_string_get(group_name):
    if group_name_exists(group_name):
        group_id = group_get_id(group_name)

        Strings = []

        # Открытие курсора
        connection = Connection.get_connection()
        cur = connection.cursor()  # Открытие курсора

        cur.execute(
            f"select * from students where group_id = '{group_id}'"
        )

        for table in cur.fetchall():
            Strings.append(str(table[1]) + " (" + str(table[0]) + ")")

        cur.close()  # Закрытие курсора

        return Strings
    else:
        print(f"Группы {group_name} не существует")
        return []


def group_rename(group_name, new_group_name):
    if group_name_exists(group_name):
        if not group_name_exists(new_group_name):
            # Открытие курсора
            connection = Connection.get_connection()
            cur = connection.cursor()  # Открытие курсора

            cur.execute(
                f"update groups set group_name = '{new_group_name}' where group_name = '{group_name}'"
            )

            cur.close()  # Закрытие курсора

            connection.commit()  # Закрытие транкзации

            print(f"Название группы {group_name} изменено на {new_group_name}")
            return f"Название группы {group_name} изменено на {new_group_name}"
        else:
            print(f"Группа с названием {new_group_name} уже существует")
            return f"Группа с названием {new_group_name} уже существует"
    else:
        print(f"Группы с названием {group_name} не существует")
        return f"Группы с названием {group_name} не существует"


def group_reform(group_name, new_group_name):
    if group_name_exists(group_name):
        if group_name_exists(new_group_name):
            group_id = group_get_id(group_name)
            new_group_id = group_get_id(new_group_name)

            # Открытие курсора
            connection = Connection.get_connection()
            cur = connection.cursor()  # Открытие курсора

            cur.execute(
                f"update students set group_id = '{new_group_id}' where group_id = '{group_id}'"
            )

            cur.close()  # Закрытие курсора

            connection.commit()  # Закрытие транкзации
            print(f"Студенты группы {group_name} переведены в группу {new_group_name}")
        else:
            print(f"Группы {new_group_name} не существует")
    else:
        print(f"Группы {group_name} не существует")


def groups_get_list():
    groups = []

    # Открытие курсора
    connection = Connection.get_connection()
    cur = connection.cursor()  # Открытие курсора

    cur.execute(
        f"select group_name from groups"
    )

    for line in cur.fetchall():
        groups.append(line[0])

    cur.close()  # Закрытие курсора

    return groups


def get_grades_student(student_id):
    a = []
    if student_id_exists(student_id):
        connection = Connection.get_connection()
        cur = connection.cursor()  # Открытие курсора

        cur.execute(
            f"select * from grades s where stud_id = '{student_id}'"
        )

        for table in cur.fetchall():
            print(table)

        cur.close()  # Закрытие курсора

    else:
        print(f"Студента с ID {student_id} не существует")


def get_grades_student_subject(student_id, subject_name):
    grades = []

    if student_id_exists(student_id):
        if subject_exists(subject_name):

            subject_id = subject_get_id(subject_name)

            connection = Connection.get_connection()
            cur = connection.cursor()  # Открытие курсора

            cur.execute(
                f"select * from grades s where stud_id = '{student_id}' and subj_id = '{subject_id}'"
            )

            for table in cur.fetchall():
                print(table)
                grades.append((table[3], table[2]))

            cur.close()  # Закрытие курсора

            return grades
        else:
            print(f"Предмета {subject_name} не существует")
            return grades

    else:
        print(f"Студента с ID {student_id} не существует")
        return grades


def get_grades_group_subject(group_name, subject_name):
    if subject_exists(subject_name):
        if group_name_exists(group_name):

            subject_id = subject_get_id(subject_name)
            IDs = group_get_students_id(group_name)

            for i in range(len(IDs)):
                connection = Connection.get_connection()
                cur = connection.cursor()  # Открытие курсора

                cur.execute(
                    f"select * from grades s where stud_id = '{IDs[i]}' and subj_id = '{subject_id}'"
                )

                for table in cur.fetchall():
                    print("Оценки ", table)

                cur.close()  # Закрытие курсора
        else:
            print(f"Группы {group_name} не существует")
    else:
        print(f"Предмет {subject_name} не существует")


def grade_single_exists(student_id, subject_name, date):
    if student_id_exists(student_id):
        if subject_exists(subject_name):
            subject_id = subject_get_id(subject_name)

            # Открытие курсора
            connection = Connection.get_connection()
            cur = connection.cursor()  # Открытие курсора

            cur.execute(
                f"select count(*) from grades g where subj_id = '{subject_id}' and stud_id = '{student_id}' and grade_date = '{date}'"
            )

            if cur.fetchone()[0] > 0:
                cur.close()  # Закрытие курсора
                return True
            else:
                cur.close()  # Закрытие курсора
                return False
        else:
            return False
    else:
        return False


def grade_student_exists(student_id):
    if student_id_exists(student_id):
        # Открытие курсора
        connection = Connection.get_connection()
        cur = connection.cursor()  # Открытие курсора

        cur.execute(
            f"select count(*) from grades g where stud_id = '{student_id}'"
        )

        if cur.fetchone()[0] > 0:
            cur.close()  # Закрытие курсора
            return True
        else:
            cur.close()  # Закрытие курсора
            return False
    else:
        return False


def grade_subject_exists(subject_name):
    if subject_exists(subject_name):

        subject_id = subject_get_id(subject_name)

        # Открытие курсора
        connection = Connection.get_connection()
        cur = connection.cursor()  # Открытие курсора

        cur.execute(
            f"select count(*) from grades g where subj_id = '{subject_id}'"
        )

        if cur.fetchone()[0] > 0:
            cur.close()  # Закрытие курсора
            return True
        else:
            cur.close()  # Закрытие курсора
            return False
    else:
        return False


def grade_add(student_id, subject_name, value, date):
    if student_id_exists(student_id):
        if subject_exists(subject_name):
            if not grade_single_exists(student_id, subject_name, date):
                # Открытие курсора
                connection = Connection.get_connection()
                cur = connection.cursor()  # Открытие курсора

                subject_id = subject_get_id(subject_name)

                cur.execute(
                    f"insert into grades (stud_id, subj_id, value, grade_date) values ('{student_id}', '{subject_id}', "
                    f"'{value}', '{date}')"
                )

                cur.close()  # Закрытие курсора

                connection.commit()  # Закрытие транкзации

                print(f"Оценка на студента {student_id}, по предмету {subject_name} со значением {value} добавлена на "
                      f"дату {date}")
                return f"Оценка на студента {student_id}, по предмету {subject_name} со значением {value} " \
                       f"добавлена на дату {date}"

            else:
                print(f"Оценка с параметрами {student_id}, {subject_name}, {date} уже существует")
                return f"Оценка с параметрами {student_id}, {subject_name}, {date} уже существует"
        else:
            print(f"Предмета с названием {subject_name} не существует")
            return f"Предмета с названием {subject_name} не существует"
    else:
        print(f"Студента с ID {student_id} не существует")
        return f"Студента с ID {student_id} не существует"


def grade_value_change(student_id, subject_name, new_value, date):
    if student_id_exists(student_id):
        if subject_exists(subject_name):
            if grade_single_exists(student_id, subject_name, date):

                subject_id = subject_get_id(subject_name)

                # Открытие курсора
                connection = Connection.get_connection()
                cur = connection.cursor()  # Открытие курсора

                subject_id = subject_get_id(subject_name)

                cur.execute(
                    f"update grades set value = {new_value} where stud_id = {student_id} and subj_id = {subject_id} "
                    f"and grade_date = '{date}'"
                )

                cur.close()  # Закрытие курсора

                connection.commit()  # Закрытие транкзации

                print(f"Оценка на студента {student_id}, по предмету {subject_name} за {date} обновлена на {new_value}")
            else:
                print(f"Оценка с параметрами {student_id}, {subject_name}, {date} уже существует")
        else:
            print(f"Предмета с названием {subject_name} не существует")
    else:
        print(f"Студента с ID {student_id} не существует")


def grade_delete(student_id, subject_name, date):
    if student_id_exists(student_id):
        if subject_exists(subject_name):
            if grade_single_exists(student_id, subject_name, date):
                # Открытие курсора
                connection = Connection.get_connection()
                cur = connection.cursor()  # Открытие курсора

                subject_id = subject_get_id(subject_name)

                cur.execute(
                    f"delete from grades where stud_id = '{student_id}' and subj_id = '{subject_id}' "
                    f"and grade_date = '{date}'"
                )

                cur.close()  # Закрытие курсора

                connection.commit()  # Закрытие транкзации
                print(f"Оценка с параметрами {student_id}, {subject_name}, {date} удалена")
                return f"Оценка с параметрами {student_id}, {subject_name}, {date} удалена"
            else:
                print(f"Оценка с параметрами {student_id}, {subject_name}, {date} не существует")
                return f"Оценка с параметрами {student_id}, {subject_name}, {date} не существует"
        else:
            print(f"Предмета с названием {subject_name} не существует")
            return f"Предмета с названием {subject_name} не существует"
    else:
        print(f"Студента с ID {student_id} не существует")
        return f"Студента с ID {student_id} не существует"


def student_delete_grades():
    pass


def subject_delete_grades():
    pass
