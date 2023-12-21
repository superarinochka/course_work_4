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
    print('Отсортировать вакансии по зарплате?')
    ans_1 = input()
    if ans_1.lower() == 'да':
        for top in get_top(list_dict):
            print(top)
    else:
        return
    print('Сохранить результат поиска?')
    ans_2 = input()
    if ans_2.lower() == 'да':
        from_all = JSONSaver()
        from_all.add_vacancies(from_hh)
        from_all.add_vacancies(from_sj)
        from_all.sort_vacancies_by_salary()
        from_all.save_vacancies()
    else:
        print('Благодарим, что воспользовались нашим сервисом.')


if __name__ == '__main__':
    user_interaction()
