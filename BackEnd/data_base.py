import json
import pathlib
import datetime


class DATA:
    with open("../data/task.json", "r") as _data:
        _task_data: dict = json.load(_data)

    @staticmethod
    def _has_attribute(atr: str) -> bool:
        # TODO: create a function that only can access in this class. to prevent error, while searching for some keys.
        # TODO: if array does not contain any obj, create or skipp.
        pass

    @staticmethod
    def create_a_task():
        # TODO
        pass

    @staticmethod
    def get_task_data() -> dict:
        return DATA._task_data

    @staticmethod
    def save_task_data():
        with open("../data/task.json", "w") as _data:
            _data.write(json.dumps(DATA._task_data, indent=True))

    @staticmethod
    def move_task_to_done(id_) -> bool:
        for index, task in enumerate(DATA._task_data["tasks"]):
            task: dict
            if task.get("id") == id_:
                DATA._task_data["completed"].append(DATA._task_data["tasks"].pop(index))
                DATA.save_task_data()
                return True
        return False

    @staticmethod
    def move_task_to_doing(id_) -> bool:
        for index, task in enumerate(DATA._task_data["tasks"]):
            task: dict
            if task.get("id") == id_:
                DATA._task_data["doing"].append(DATA._task_data["tasks"].pop(index))
                DATA.save_task_data()
                return True
        return False

    @staticmethod
    def move_doing_to_done(id_) -> bool:
        for index, task in enumerate(DATA._task_data["doing"]):
            task: dict
            if task.get("id") == id_:
                DATA._task_data["completed"].append(DATA._task_data["doing"].pop(index))
                DATA.save_task_data()
                return True
        return False

    @staticmethod
    def clear_task():
        DATA._task_data["tasks"].clear()
        DATA.save_task_data()

    @staticmethod
    def clear_done():
        DATA._task_data["completed"].clear()
        DATA.save_task_data()
