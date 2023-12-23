import json


class Vacancy:
    "Класс для хранения информации о вакансии"

    def __init__(self, job_id, job_url, name, salary_from, salary_to, city):
        self.job_id = job_id
        self.job_url = job_url
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.city = city

    #def __eq__(self, other):
        #return self.salary_from == other.salary_from

    #def __ne__(self, other):
        #return self.salary_from != other.salary_from

    #def __lt__(self, other):
        #return self.salary_from < other.salary_from

    #def __gt__(self, other):
        #return self.salary_from > other.salary_from

    #def __le__(self, other):
        #return self.salary_from <= other.salary_from

    #def __ge__(self, other):
        #return self.salary_from >= other.salary_from

    def __str__(self):
        return f'id: {self.job_id}\n' \
               f'ссылка: {self.job_url}\n' \
               f'профессия: {self.name}\n' \
               f'зарплата от: {self.salary_from}\n' \
               f'зарплата до: {self.salary_to}\n' \
               f'город: {self.city}\n'

    def to_dict(self):
        "Функция представляющая вакансию в виде словаря"
        return {
            'job_id': self.job_id,
            'job_url': self.job_url,
            'name': self.name,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'city': self.city
        }

    @staticmethod
    def from_dict(vacan_dict):
        """Статический метод для перевода словаря в вакансию"""
        return Vacancy(
            vacan_dict['job_id'],
            vacan_dict['job_url'],
            vacan_dict['name'],
            vacan_dict['salary_from'],
            vacan_dict['salary_to'],
            vacan_dict['city']
        )


class Vacancies:
    """Класс для хранения и обработки вакансий"""

    def __init__(self):
        "Создание словаря"
        self.__all_vacancies = []

    def add_vacancies(self, new_vacancies):
        "Добавление вакансии в словарь"
        self.__all_vacancies += new_vacancies

    def delete_vacancies(self, old_vacancies):
        "Удаление вакансии из словаря"
        for i in old_vacancies:
            self.__all_vacancies.remove(i)

    #def sort_vacancies_by_salary(self):
        #"Сортировка в словаре"
        #self.__all_vacancies.sort(reverse=True)

    def sorting (self, poe):
        vacancies_list = []
        vacancies_sort = sorted(list_dict, key=lambda vacancy: vacancy["salary_from"], reverse=True)
        for vacancy in vacancies_sort:
            vacancies_list.append(f"""
            ID вакансии: {vacancy['job_id']}
            Cсылка: {vacancy['job_url']},
            Должность: {vacancy['name']},
            Минимальная оплата:{vacancy['salary_from']},
            Максимальная оплата:{vacancy['salary_to']},
            Город: {vacancy['city']}""")
        with open(f'sort.json', 'w', encoding='UTF-8') as file:
            json.dump(vacancies_sort, file, indent=2, ensure_ascii=False)
        return vacancies_list

    def get_top (self, list_dict, top_count):
        top_list = []
        vacancies_sort = sorted(list_dict, key=lambda vacancy: vacancy["salary_from"], reverse=True)
        top_vacancies = vacancies_sort[0:top_count]
        for vacancy in top_vacancies:
            top_list.append(f"""
            ID вакансии: {vacancy['job_id']}
            Cсылка: {vacancy['job_url']},
            Должность: {vacancy['name']},
            Минимальная оплата:{vacancy['salary_from']},
            Максимальная оплата:{vacancy['salary_to']},
            Город: {vacancy['city']}""")
        with open(f'top.json', 'w', encoding='UTF-8') as file:
            json.dump(top_vacancies, file, indent=2, ensure_ascii=False)
        return top_list


    @property
    def all_vacancies(self):
        return self.__all_vacancies

    def to_list_dict(self):
        a = []
        for i in self.__all_vacancies:
            a.append(i.to_dict())
        return a

