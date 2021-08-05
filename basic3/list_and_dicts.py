def run():
    my_list = [1,"Hello", True , 4.5]
    my_dict = { "one" : "john", "Two":"jairo" }

    super_list = [
        { "one" : "john", "Two":"jairo" },
        { "one" : "a", "Two":"1" },
        { "one" : "b", "Two":"0" },
        { "one" : "b", "Two":"3" },
        { "one" : "d", "Two":"4" },
    ]

    super_dic = {
        "number" : [1,2,3,4,5,6],
        "number2" : [-1,-2,-3,-4]
    }

    for key, value in super_dic.items():
        print(key,"-",value)

if __name__ == '__main__':
    run()