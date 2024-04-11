import fizzbuzzclass as fbc

class main():
     
    numbers = fbc.FB()
    for i in range(16):
        print(numbers.smart_printer(i))
    
    
if __name__ == '__main__':
    main()