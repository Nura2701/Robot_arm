def main(x):
    if x==1:
        
        x=x+1
        print("inside if",x)
    else:
        print("inside else",x)
        x=1




if __name__=='__main__':
    block=1
    main(block)
    print("inside main",block)