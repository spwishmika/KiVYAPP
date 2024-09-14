import datetime
import json


class DATA:
    _path = "../data/task.json"
    with open(_path, "r") as _data:
        _task_data: dict = json.load(_data)

    _template = {
        "id": 0,
        "title": "",
        "subject": "",
        "category": "",
        "description": "",
        "start_date": [],
        "end_date": [0, 0, 0, 0, 0, 0]
    }

    @staticmethod
    def create_a_task(title: str, subject: str, category: str, end_date: list, description: str = "") -> bool:
        """
        You can create a task using this function.

        NOTE: You should perform all information. except description

        :param title: Little string not too large
        :param subject: Subject
        :param category: Category
        :param end_date: end date is the day will expire this task.You should enter list something like this [year,month,day] or [yyyy,month,day,hour,min,sec]
        :param description: Description is not essential thing, but if you need.. a string..

        :return:  return true if it's done correctly else return false
        """
        template: dict = DATA._template.copy()

        start_date = datetime.datetime.now()
        if len(end_date) == 3:
            end_date = [end_date[0], end_date[1], end_date[2], 0, 0, 0]
            expire_date = datetime.datetime(end_date[0], end_date[1], end_date[2], 0, 0, 0)
        elif len(end_date) == 5:
            end_date = [end_date[0], end_date[1], end_date[2], end_date[3], end_date[4], end_date[5]]
            expire_date = datetime.datetime(*end_date)
        else:
            return False

        expire = expire_date - start_date

        if title == "" or subject == "" or category == "" or expire < datetime.timedelta(seconds=0):
            return False
        else:
            get_id: int = DATA._task_data.get("ids")
            DATA._task_data["ids"] = get_id + 1
            DATA.save_task_data()

            template["id"] = get_id
            template["title"] = title
            template["subject"] = subject
            template["category"] = category
            template["start_date"] = [start_date.year, start_date.month, start_date.day, start_date.hour,
                                      start_date.minute, start_date.second]
            template["end_date"] = end_date
            template["description"] = description

            DATA._task_data["tasks"].append(template)
            DATA.save_task_data()
            return True

    @staticmethod
    def remove_a_task(id_) -> bool:
        """
        remove a task from task section using ID.

        NOTE: Can't be get back.

        :param id_: int
        :return: boolean if it's done correctly, else return false
        """
        for task in DATA._task_data["tasks"]:
            task: dict
            if task.get("id") == id_:
                DATA._task_data["tasks"].remove(task)
                DATA.save_task_data()
                return True
        return False

    @staticmethod
    def get_task_data() -> dict:
        """
        This function returns all JSON database as a dict.

        NOTE: if you change something you should call save_task_data() function to register your changes.
        """
        return DATA._task_data

    @staticmethod
    def save_task_data() -> None:
        """
        This function run automatically when you do something with data. using this DATA object.
        if you try to make a change by you. you must call this function to save data.

        :return: None
        """
        with open(DATA._path, "w") as _data:
            _data.write(json.dumps(DATA._task_data, indent=True))

    @staticmethod
    def move_task_to_done(id_) -> bool:
        """
        Move a task to completed section.

        NOTE: Can't be get back.

        :param id_: int
        :return: boolean if it's done correctly, else return false
        """
        for index, task in enumerate(DATA._task_data["tasks"]):
            task: dict
            if task.get("id") == id_:
                DATA._task_data["completed"].append(DATA._task_data["tasks"].pop(index))
                DATA.save_task_data()
                return True
        return False

    @staticmethod
    def move_task_to_doing(id_) -> bool:
        """
        Move a task to doing section.

        NOTE: Can't be get back.

        :param id_: int
        :return: boolean if it's done correctly, else return false
        """
        for index, task in enumerate(DATA._task_data["tasks"]):
            task: dict
            if task.get("id") == id_:
                DATA._task_data["doing"].append(DATA._task_data["tasks"].pop(index))
                DATA.save_task_data()
                return True
        return False

    @staticmethod
    def move_doing_to_done(id_) -> bool:
        """
        Move a doing task to completed section.

        NOTE: Can't be get back.

        :param id_: int
        :return: boolean if it's done correctly, else return false
        """
        for index, task in enumerate(DATA._task_data["doing"]):
            task: dict
            if task.get("id") == id_:
                DATA._task_data["completed"].append(DATA._task_data["doing"].pop(index))
                DATA.save_task_data()
                return True
        return False

    @staticmethod
    def move_expired_task_to_missed() -> None:
        """
        This function allow to move all expired task to missed_task section.

        NOTE: This functions not automatically run, you should call it fist.

        :return: None
        """
        for index, task in enumerate(DATA._task_data["tasks"]):
            task: dict
            sd: list = task.get("start_date")
            ed: list = task.get("end_date")
            expire = datetime.datetime(ed[0], ed[1], ed[2], ed[3], ed[4], ed[5]) - \
                     datetime.datetime(sd[0], sd[1], sd[2], sd[3], sd[4], sd[5])

            if expire < datetime.timedelta(seconds=0):
                DATA._task_data["missed_task"].append(DATA._task_data["tasks"].pop(index))
                DATA.save_task_data()

    @staticmethod
    def clear_task() -> None:
        """
        Clear tasks from database.
        NOTE: Can't be roll back.
        """
        DATA._task_data["tasks"].clear()
        DATA.save_task_data()

    @staticmethod
    def clear_done() -> None:
        """
        Clear all completed tasks.
        """
        DATA._task_data["completed"].clear()
        DATA.save_task_data()

    @staticmethod
    def reset_all() -> None:
        """
        Rest all Data base.
        """
        DATA._task_data["ids"] = 0
        DATA._task_data["tasks"].clear()
        DATA._task_data["doing"].clear()
        DATA._task_data["missed_task"].clear()
        DATA._task_data["completed"].clear()
        DATA.save_task_data()
