from src.vacancy import Vacancy, Vacancies
from src.savers import JSONSaver
from src.job_api import HeadHunterAPI, SuperJobAPI


def user_interaction():
    print('Добро пожаловать! Введите ключевое слово для поиска по профессии')
    keyword = input()
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()
    print('Введите кол-во страниц, по которым будет осуществлен поиск')
    pages = int(input())
    from_hh = hh_api.get_vacancies(keyword, pages)
    from_sj = superjob_api.get_vacancies(keyword, pages)
    print('Найденные вакансии на сайте "HeadHuter":\n')
    for i in from_hh:
        print(i)
    print('Найденные вакансии на сайте "SuperJob":\n')
    for i in from_sj:
        print(i)
    print('Отсортировать данные и записать в файл?')
    ans = input()
    if ans == 'yes':
        from_all = JSONSaver()
        from_all.add_vacancies(from_hh)
        from_all.add_vacancies(from_sj)
        from_all.sort_vacancies_by_salary()
        from_all.save_vacancies()
    else:
        print('Введено неизвестное значение ответа.')


if __name__ == '__main__':
    user_interaction()
