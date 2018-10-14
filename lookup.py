import random
from time import time

class Test:
    arr = []
    def Test(self, elem_amount):
        self.arr = [random.randint(1,elem_amount) for _ in range(elem_amount)]

    def get_init_array(self, elem_amount):
        return 

    # def get_array():
        

def main():
    start_time = time()
    Test()

    end_time = time() - start_time

    print(end_time)


    

if __name__ == '__main__':
    main()