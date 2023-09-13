from functools import reduce;

def run():
    #map  - reduce - filter

    my_list = [1,2,3,4,5];
    my_list2 = [22,33,44,55,1,5,8,22,4,12,15,17,18]
    maplist = list(map(lambda x: x**2,my_list));

    print(maplist)
    print("-------------------------------------------------------")

    filterlist = list(filter(lambda x: x<18,my_list2));
    print(filterlist)
    print("-------------------------------------------------------")

    listreduce = reduce(lambda x,y: x*y, my_list);
    print(listreduce)

if __name__ == "__main__":
    run();    