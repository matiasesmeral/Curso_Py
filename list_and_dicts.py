
def run():
    mylist = [1,2,True,"false"];
    my_dict = {"firstname":"matias","secondname":"sanguino"}

    super_list = [
    { "firstname":"matias","secondname":"sanguino",
      "firstname":"jannine","secondname":"patricia",
      "firstname":"juana","secondname":"godoy" }
    ]

    super_dic = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-2,-1,0,1,2],
        "floats_nums" : [1.2,1.3,1.4]
    }

    for x in mylist:
        print(x);

    for keys,values in my_dict.items():
        print(keys , " : ", values);

    for key in super_list:
        print(key , " : ");
    
    for keys,values in super_dic.items():
        print(keys , " : ", values);


if __name__ == "__main__":
    run()