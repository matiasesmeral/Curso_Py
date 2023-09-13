from operator import add


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },];

def run():

    #all_python_devs = nombre de todos los que devs saben python
    #all_platzi_workers = nombre de todos los trabajadores de platzi
    #Todo se hace con list_compremshions.

    #todas las personas que son mayores a 18 años filter and map

    #crear una nueva lista indicando true o false si es mayor a 70 años.

    #crear las listas all_python _devs y all_platzi_workers usando filter and map.
    #crear la lista old_people y adults con list comprenshions

    #all_python_devs = [devs ['name'] for devs in DATA if devs["language"]== "python" ];
    #all_platzi_workers = [workers['name'] for workers in DATA if workers["organization"] =='Platzi']
    old_people = list(filter(lambda old: old["age"]>18,DATA))

    old_people = list(map(lambda name: name["name"],old_people))
    
    old_peopleold = list(map(lambda age: age | {"old": age["age"]>70},DATA ));
    
    all_python_devs = list(filter(lambda pydevs: pydevs["language"]=="python",DATA))
    
    all_python_devs = list(map(lambda namedev: namedev["name"],all_python_devs));
    
    old_people2 = [old["name"] for old in DATA if old["age"]>18]
    
    old2 = [ {**old, **{'old': old["age"]>70}} for old in DATA ]
    
    print(old2);


if __name__ == "__main__":
    run()    